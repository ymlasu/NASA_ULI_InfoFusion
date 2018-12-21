import os
import time
from sys import argv

from multiprocessing import Pool
from multiprocessing import cpu_count
from typing import Union
from functools import partial

import pyxb
import sqlite3
import psycopg2

from smes3 import smes3
from smes4 import smes4

from extracted import Extracted_SMES, Extracted_ASDEX
import exceptions

class DatabaseManager(object):
    def __init__(self, db):
        self.conn = psycopg2.connect(db)
        self.cur = self.conn.cursor()

    def query(self, arg):
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur

    def __del__(self):
        self.conn.close()

def process_smes(message: Union[smes3.CTD_ANON, smes4.CTD_ANON]):
    if type(message) == smes3.CTD_ANON:
        print("SMES3")
    else:
        print("SMES4")

    data = Extracted_SMES(
        callsign = message.callsign,
        track = message.track,
        stid = message.stid,
        time = message.time,
        event = message.event,
        position = (message.position.latitude, message.position.longitude),
        altitude = message.altitude,
        status = message.status,
    )
    
    return data


# x_report because all the basic report containers have the same contents
def process_basic_report(x_report, airport):
    basic_report = x_report.report.basicReport
    
    try:
        data = Extracted_ASDEX(
            airport = airport, 
            track = basic_report.track,
            time = basic_report.time,
            is_position_report = False,
            position = (basic_report.position.lat,basic_report.position.lon),
        )
    except:
        data = Extracted_ASDEX(
            airport = airport,
            track = basic_report.track,
            time = basic_report.time,
            is_position_report = False,
        )
    return data
    
def process_position_report(position_report, airport):
    try:
        data = Extracted_ASDEX(
            airport = airport, 
            track = position_report.track,
            time = position_report.time,
            is_position_report = True,
            stid = position_report.stid,
            position = (position_report.position.lat,position_report.position.lon),
        )
    except:
        data = Extracted_ASDEX(
            airport = airport,
            track = position_report.track,
            time = position_report.time,
            is_position_report = True,
            stid = position_report.stid,
        )
    return data

ASDEX_TYPES = {"mlatReport": process_basic_report,
               "adsbReport": process_basic_report,
               "smrReport": process_basic_report,
               "positionReport": process_position_report}

def process_asdex(message: Union[smes3.CTD_ANON_, smes4.CTD_ANON_]):

    # find which report type it is, and process if any exist
    results = []
    for msg_type in ASDEX_TYPES:
        msg_list = getattr(message, msg_type)
        if len(msg_list) > 0:
            with_airport = partial(ASDEX_TYPES[msg_type], airport=message.airport)
            # calling list to force the evaluation, even though we don't need the return value
            results = list(map(with_airport, msg_list))
    return results


# global mapping from message types to processing functions
MESSAGE_TYPES = {smes3.CTD_ANON: process_smes,
                 smes4.CTD_ANON: process_smes,
                 smes3.CTD_ANON_: process_asdex,
                 smes4.CTD_ANON_: process_asdex}


def process_file(filename: str):
    with open(filename) as f:
        xml = f.read()

    # http://pyxb.sourceforge.net/userref_validating.html
    contents = None
    i = 0
    results = [[]]
    try:
        contents = smes3.CreateFromDocument(xml)
    except (pyxb.ValidationError, pyxb.UnrecognizedDOMRootNodeError):
        try:
            contents = smes4.CreateFromDocument(xml)
        except (pyxb.ValidationError, pyxb.UnrecognizedDOMRootNodeError):
            #pass
            print(filename)

    if contents is not None:
        if type(contents) in MESSAGE_TYPES:
            results = MESSAGE_TYPES[(type(contents))](contents)
            if type(contents) in [smes3.CTD_ANON, smes4.CTD_ANON]:
                results = [results]
        else:
            print("UNCATEGORIZED")
            raise exceptions.UnknownXMLContentException("Filename: {filename}")
            results = []
    else:
        print("UNKNOWN")
        results = []
        # raise exceptions.UnknownXMLContentException(f"Filename: {filename}")
    if type(results) is not list:
        results = [results]
    return results

def makeDb(dbName,results):
    dbmgr = DatabaseManager('dbname=paraatm user=paraatm_user password=paraatm_user')
    #dbmgr.query('DROP TABLE IF EXISTS asdex')
    #dbmgr.query('CREATE TABLE asdex (airport CHAR(4), track INTEGER, stid INTEGER,time TIMESTAMP,lat REAL,lon REAL);')
    #dbmgr.query('DROP TABLE IF EXISTS smes')
    #dbmgr.query('CREATE TABLE smes (callsign VARCHAR, track INTEGER, stid INTEGER,time TIMESTAMP,lat REAL,lon REAL,alt REAL,status VARCHAR,event VARCHAR);')

    flat_list = [item for sublist in results for item in sublist if sublist is not None]
    for data in flat_list:
        if isinstance(data,Extracted_ASDEX):
            cmd = "SELECT time FROM asdex WHERE time='{}' and airport='{}' and track='{}';".format(data.time,data.airport,data.track)
            dbmgr.cur.execute(cmd)
            contents = dbmgr.cur.fetchall()
            if contents:
                print(contents)
            sql_command = "INSERT INTO asdex (airport,track,time) VALUES('{}',{},'{}');".format(data.airport,data.track,data.time)
            dbmgr.query(sql_command)
            try:
                sql_command = "UPDATE asdex SET stid={} WHERE time='{}' AND track='{}' AND airport='{}';".format(data.stid,data.time,data.track,data.airport)
                dbmgr.query(sql_command)
            except:
                dbmgr.query('rollback')
            try:
                sql_command = "UPDATE asdex SET lat={},lon={} WHERE time='{}' AND track='{}' AND airport='{}';".format(data.position[0],data.position[1],data.time,data.track,data.airport)
                dbmgr.query(sql_command)
            except:
                dbmgr.query('rollback')
        if isinstance(data,Extracted_SMES):
            cmd = "SELECT time FROM smes WHERE time='{}' and lat='{}' and lon='{}';".format(data.time,data.position[0],data.position[1])
            dbmgr.cur.execute(cmd)
            contents = dbmgr.cur.fetchall()
            if contents:
                continue
            sql_command = "INSERT INTO smes (callsign,track,time,event,lat,lon,alt,status) VALUES('{}',{},'{}','{}',{},{},{},'{}');".format(data.callsign,data.track,data.time,data.event,data.position[0],data.position[1],data.altitude,data.status)
            dbmgr.query(sql_command)

    del dbmgr

def main(argv):
    
    
    os.chdir(argv[1])
    start = time.time()
    
    #with Pool(cpu_count()) as p:
    with Pool(1) as p:
        results=p.map(process_file, (item for item in sorted(os.listdir('.')) if os.path.isfile(item)))
        
    end = time.time()
    print("Time elapsed: ", end - start)

    makeDb('PARA_ATM_Database_Public',results)

if __name__ == "__main__":
    main(argv)
