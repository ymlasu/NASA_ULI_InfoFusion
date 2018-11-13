import os
import time

from multiprocessing import Pool
from multiprocessing import cpu_count

from databaseManager import DatabaseManager

import pyxb
import sqlite3

# we have to import all of the different namespaces so the parser knows what to do,
# even if they're technically "unused"
import fdps
import fixm
import nas

from extracted import Extracted_FDPS
import exceptions

def process_th(message: nas.FlightMessageType):
    # typing the submessage to make it easier to pull out fields with autocomplete (not strictly required)
    flight: nas.NasFlightType = message.flight
    # this is the minimal set of everything that exists in the current set of files
    data = Extracted_FDPS(
        source=flight.source,
        aircraft_id=flight.flightIdentification.aircraftIdentification,
        center=flight.centre,
        system=flight.system,
        timestamp=flight.timestamp,
        actual_time=flight.enRoute.position.positionTime,
    )
    print(data)
    return data
    # TODO: process the things that only show up sometimes


# global mapping from message types to processing functions
MESSAGE_TYPES = {"TH": process_th}

def process_file(filename: str):
    with open(filename) as f:
        xml = f.read()

    # http://pyxb.sourceforge.net/userref_validating.html
    contents = None
    try:
        contents = fdps.CreateFromDocument(xml)
    # TODO: some files are schema invalid, decide how to handle those
    except pyxb.ValidationError as e:
        pass
        # print(filename)
        # print(e.details())

    results = []
    if contents is not None:
        if isinstance(contents, nas.MessageCollectionType):
            for message in contents.message:
                source = message.flight.source
                processing_function = MESSAGE_TYPES.get(source)
                if processing_function:
                    results.append(processing_function(message))
                else:
                    # turn this on to get an error when you see a new type (which you then need to implement)
                    # raise exceptions.UnknownFDPSSourceException(f"Message type not found: { source }")
                    pass
        # this anonymous type is the "FDPSMsg" type
        elif isinstance(contents, fdps.CTD_ANON):
            # TODO: write a processor for this
            results.append([])
            pass
        else:
            raise exceptions.UnknownXMLContentException(f"Filename: {filename}")
    return results

def makeDb(dbName,results):
    dbmgr = DatabaseManager('{}.db'.format(dbName))
    dbmgr.query('DROP TABLE IF EXISTS th')
    dbmgr.query('CREATE TABLE th (aircraft, center, system ,time);')
   
    flat_list = [item for sublist in results for item in sublist]
    print(flat_list)
    for data in flat_list:
        if isinstance(data,Extracted_FDPS):
            sql_command = "INSERT INTO th (aircraft, center, system ,time) VALUES('{}','{}','{}','{}');".format(data.aircraft_id, data.center, data.system, data.timestamp)
            dbmgr.query(sql_command)
    dbmgr.close()                    

    dbmgr = DatabaseManager('{}.db'.format(dbName))
    for row in dbmgr.query('SELECT * FROM th'):
        print(row)

def main():
    os.chdir('../fdps/bin/data/2018-08-16')
    start = time.time()

    #with Pool(cpu_count()) as p:
    with Pool(1) as p:
        results=p.map(process_file, (item for item in os.listdir('.')[1000:1020] if os.path.isfile(item)))

    end = time.time()
    print("Time elapsed: ", end - start)

    os.chdir('../../../../fdps-extractor')
    makeDb('swim',results)

if __name__ == "__main__":
    main()
