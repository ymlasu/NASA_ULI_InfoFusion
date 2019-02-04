# -*- coding: utf-8 -*-
'''
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Hari Iyer
Date: 06/11/2018
'''

import os
import re
import csv
import sys
import glob
import random
import datetime
from math import *
from jpype import *


#NATS dependencies and definitions
#-------------------------------------------------------------------------------------------------------------------------#
classpath = "dist/nats-client.jar:dist/nats-shared.jar"

startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % classpath)
FLIGHT_PHASE_PREDEPARTURE = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_PREDEPARTURE;
FLIGHT_PHASE_ORIGIN_GATE = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_ORIGIN_GATE;
FLIGHT_PHASE_PUSHBACK = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_PUSHBACK;
FLIGHT_PHASE_RAMP_DEPARTING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_RAMP_DEPARTING;
FLIGHT_PHASE_TAXI_DEPARTING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TAXI_DEPARTING;
FLIGHT_PHASE_RUNWAY_THRESHOLD_DEPARTING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_RUNWAY_THRESHOLD_DEPARTING;
FLIGHT_PHASE_TAKEOFF = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TAKEOFF;
FLIGHT_PHASE_CLIMBOUT = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_CLIMBOUT;
FLIGHT_PHASE_CLIMB_TO_CRUISE_ALTITUDE = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_CLIMB_TO_CRUISE_ALTITUDE;
FLIGHT_PHASE_TOP_OF_CLIMB = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TOP_OF_CLIMB;
FLIGHT_PHASE_CRUISE = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_CRUISE;
FLIGHT_PHASE_TOP_OF_DESCENT = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TOP_OF_DESCENT;
FLIGHT_PHASE_INITIAL_DESCENT = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_INITIAL_DESCENT;
FLIGHT_PHASE_APPROACH = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_APPROACH;
FLIGHT_PHASE_FINAL_APPROACH = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_FINAL_APPROACH;
FLIGHT_PHASE_GO_AROUND = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_GO_AROUND;
FLIGHT_PHASE_TOUCHDOWN = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TOUCHDOWN;
FLIGHT_PHASE_LAND = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_LAND;
FLIGHT_PHASE_EXIT_RUNWAY = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_EXIT_RUNWAY;
FLIGHT_PHASE_TAXI_ARRIVING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TAXI_ARRIVING;
FLIGHT_PHASE_RUNWAY_CROSSING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_RUNWAY_CROSSING;
FLIGHT_PHASE_RAMP_ARRIVING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_RAMP_ARRIVING;
FLIGHT_PHASE_DESTINATION_GATE = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_DESTINATION_GATE;
FLIGHT_PHASE_LANDED = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_LANDED;
FLIGHT_PHASE_HOLDING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_HOLDING;

NATS_SIMULATION_STATUS_READY = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_READY
NATS_SIMULATION_STATUS_START = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_START
NATS_SIMULATION_STATUS_PAUSE = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_PAUSE
NATS_SIMULATION_STATUS_RESUME = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_RESUME
NATS_SIMULATION_STATUS_STOP = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_STOP
NATS_SIMULATION_STATUS_ENDED = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_ENDED

NATSClientFactory = JClass('NATSClientFactory')
natsClient = NATSClientFactory.getNATSClient()

#Change this to local installation of NATS_Server (eg. home/user/NATS/NATS_Server/)
NATS_SERVER = "../Server/"

#-------------------------------------------------------------------------------------------------------------------------#

#Initialize NATS interfaces, and aircrafts from TRX file
environmentInterface = natsClient.getEnvironmentInterface()
airportInterface = environmentInterface.getAirportInterface()
equipmentInterface = natsClient.getEquipmentInterface()
aircraftInterface = equipmentInterface.getAircraftInterface()
#This TRX location can be changed.
aircraftInterface.load_aircraft("share/tg/trx/TRX_DEMO_SFO_PHX.trx", "share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx")
terminalAreaInterface = environmentInterface.getTerminalAreaInterface()

#Airport scope
definedAirports = ["KABQ", "KATL", "KBDL", "KBOI", "KBOS", "KBUR", "KBWI", "KCLE", "KCLT", "KCVG", "KDCA", "KDEN", "KDFW", "KDTW", "KEWR", "KGYY", "KHPN", "KIAD", "KIAH", "KISP", "KJAX", "KJFK", "KLAS", "KLAX", "KLGA", "KLGB", "KMCO", "KMDW", "KMEM", "KMHT", "KMIA", "KMSP", "KOAK", "KONT", "KPBI", "KPDK", "KPDX", "KPHL", "KPHX", "KPIT", "KSAN", "KSDF", "KSFO", "KSJC", "KSLC", "KSNA", "KSTL", "KSWF", "KTEB", "KTPA", "KVGT", "PHNL", "PANC", "KORD", "KPVD", "KSEA", "KDAL"]

#Scanned FAA flight plans callsigns
indexedFlights = list(aircraftInterface.getAllAircraftId())

#Get airport runway & procedure data
depArrDataFile = open(NATS_SERVER + "/share/FlightPlanData/dep_arr_runway_data.csv",newline='',encoding='utf-8')
depArrData = list(csv.reader(depArrDataFile, delimiter=','))

time = str(datetime.datetime.now())
newTrx = open(NATS_SERVER + "/share/FlightPlanData/FlightPlans/" + time + "_updated_trx.trx", "a+")
mflFile = open(NATS_SERVER + "/share/FlightPlanData/FlightPlans/" + time + "_mfl.trx", "a+")
#--------------------Flight Parameters---------------------#
FLIGHT_DEPARTED = False
FLIGHT_TRACK_TIME = 0
FLIGHT_CALLSIGN = ""
FLIGHT_EQUIPMENT = ""
FLIGHT_CURRENT_POSITION = []
FLIGHT_TRUE_AIRSPEED = 0.0
FLIGHT_CURRENT_ALTITUDE_LEVEL = 0
FLIGHT_HEADING = 0
FLIGHT_ROUTE = ""
FLIGHT_DEPARTURE_AIRPORT = ""
FLIGHT_ARRIVAL_AIRPORT = ""
FLIGHT_DEPARTURE_RUNWAY = ""
FLIGHT_DEPARTURE_GATE = ""
FLIGHT_DEPARTURE_GROUND_TAXI= []
FLIGHT_ARRIVAL_GROUND_TAXI = []
FLIGHT_TURN_TO_SID = []
FLIGHT_SID_WAYPOINTS = []
FLIGHT_SID_PROCEDURE = ""
FLIGHT_STAR_PROCEDURE = ""
FLIGHT_APPROACH_PROCEDURE = ""
FLIGHT_STAR_WAYPOINTS = []
FLIGHT_ENROUTE_WAYPOINTS = []
FLIGHT_APPROACH_WAYPOINTS = []
FLIGHT_ARRIVAL_RUNWAY = ""
FLIGHT_ARRIVAL_GATE = ""
FLIGHT_GATE_TO_GATE_PLAN = []
departure_gate = []
arrival_gate = []
#----------------------------------------------------------#

def calculate_distance(xLat, xLon, yLat, yLon):
    """
    Calculates distance in nautical miles between two geographical points.
    """
    R = 6373.0
    xLat = radians(xLat)
    xLon = radians(xLon)
    yLat = radians(yLat)
    yLon = radians(yLon)
    dlon = yLon - xLon
    dlat = yLat - xLat
    a = sin(dlat / 2)**2 + cos(xLat) * cos(yLat) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance*0.539957


def decToDMS(degreeDecimal):
   """
   Converts decimal degrees to DMS format.
   """
   minutes,seconds = divmod(degreeDecimal*3600,60)
   degrees,minutes = divmod(minutes,60)
   return degrees,minutes,seconds


def closest_waypoint(waypointOptions, targetWaypoint):
    """
    Fetches closest waypoint from a set, aimed at a target.
    """
    optimalWaypoint = waypointOptions.index(min(waypointOptions, key=lambda point: calculate_distance(targetWaypoint['lat'],targetWaypoint['lon'],point['lat'],point['lon'])))
    return [index for index,wp in enumerate(waypointOptions) if wp == waypointOptions[optimalWaypoint]]



def read_trx(filename):
    """
    Reads the TRX file and returns raw text.
    """
    trxFile = open(filename)
    trxData = trxFile.read()
    trxFile.close()
    return trxData


def get_lat_lon(waypoints):
    """
    Generates and returns geo-cordinates of a set of waypoints.
    """
    latLon = []
    for waypoint in waypoints:
        try:
            location = terminalAreaInterface.getWaypoint_Latitude_Longitude_deg(waypoint)
            latLon.append({'lat': location[0], 'lon': location[1]})
        except:
            latLon.append({'lat': 0.0, 'lon': 0.0})
    return latLon


def radialLatLon(waypoint):
    """
    Calculates the referred waypoint.
    """
    radialFixPattern = re.compile("[A-Z]*\d{6}")
    if re.match(radialFixPattern, waypoint):
        distance = int(waypoint[-3:]) * 1852
        bearing = int(waypoint[-6:-3]) * 0.0175
        refWaypoint = waypoint[:-6]
        refWaypointLocation = terminalAreaInterface.getWaypoint_Latitude_Longitude_deg(refWaypoint)
        startLat = refWaypointLocation[0]
        startLon = refWaypointLocation[1]
        dx = distance * cos(bearing)
        dy = distance * sin(bearing)
        latitudeShift = dx/(111320 * cos(startLat))
        longitudeShift = dy/110540
        latitude = startLat + latitudeShift
        longitude = startLon + longitudeShift
    return {'name': waypoint, 'lat': latitude, 'lon': longitude}


def process_waypoints(waypoint):
    """
    Convert waypoint to standard {name, lat, lon} format
    """
    waypointList = waypoint.split(".")
    waypointData = []
    latitude = 0.0
    longitude = 0.0

    #Pattern matching for waypoints
    radialFixPattern = re.compile("[A-Z]+\d{6}")
    airwayPattern = re.compile("[A-Z]{1}\d+")

    for waypoint in waypointList:
        #Waypoint Pattern -> 12323N/12312W
        if '/' in waypoint:
            latitude = waypoint.split("/")[0][:-1]
            longitude = waypoint.split("/")[1][:-1]
            latitudeHeading = waypoint.split("/")[0][-1]
            longitudeHeading = waypoint.split("/")[1][-1]
            latitudeDegrees = latitude[0:2]
            latitudeMinutes = latitude[2:4]
            try:
                latitudeSeconds = latitude[4:]
            except:
                pass

            if latitudeSeconds == "":
                latitudeSeconds = 0.0

            longitudeDegrees = longitude[0:2]
            longitudeMinutes = longitude[2:4]
            try:
                longitudeSeconds = longitude[4:]
            except:
                pass
            if longitudeSeconds == "":
                longitudeSeconds = 0.0

            latitude = float(latitudeDegrees) + float(latitudeMinutes)/60 + float(latitudeSeconds)/3600
            longitude = float(longitudeDegrees) + float(longitudeMinutes)/60 + float(longitudeSeconds)/3600

            if latitudeHeading == "S":
                latitude = latitude * -1
            if longitudeHeading == "W":
                longitude = longitude * -1

            waypointData.append({'name': waypoint, 'lat': latitude, 'lon': longitude})

        #Waypoint pattern -> AAA123123
        elif re.match(radialFixPattern, waypoint):
            waypointData.append(radialLatLon(waypoint))

        #Waypoint pattern -> MIZAR
        elif waypoint.isalpha():
            waypointLocation = terminalAreaInterface.getWaypoint_Latitude_Longitude_deg(waypoint)
            if waypointLocation:
                waypointData.append({'name': waypoint, 'lat': waypointLocation[0], 'lon': waypointLocation[1]})
            else:
                waypointData.append({'name': waypoint, 'lat': 0.0, 'lon': 0.0})

        #Waypoint pattern -> HBU.J146.GIJ
        elif re.match(airwayPattern, waypoint):
            waypointData[-1]['name'] = waypointData[-1]['name'] + "." + (waypoint) + "." + waypointList[waypointList.index(waypoint) + 1]

    return waypointData


def generate_save_flight_plan(flightData, trxLineSplit):
    """
    Creates flight plan, saves as CSV, with additional flight parameters.
    """

    #Get flight parameter reference
    global FLIGHT_DEPARTED
    global FLIGHT_TRACK_TIME
    global FLIGHT_CALLSIGN
    global FLIGHT_EQUIPMENT
    global FLIGHT_CURRENT_POSITION
    global FLIGHT_TRUE_AIRSPEED
    global FLIGHT_CURRENT_ALTITUDE_LEVEL
    global FLIGHT_HEADING
    global FLIGHT_ROUTE
    global FLIGHT_SID_PROCEDURE
    global FLIGHT_STAR_PROCEDURE
    global FLIGHT_APPROACH_PROCEDURE
    global FLIGHT_DEPARTURE_AIRPORT
    global FLIGHT_ARRIVAL_AIRPORT
    global FLIGHT_DEPARTURE_RUNWAY
    global FLIGHT_SID_WAYPOINTS
    global FLIGHT_STAR_WAYPOINTS
    global FLIGHT_DEPARTURE_GROUND_TAXI
    global FLIGHT_ARRIVAL_GROUND_TAXI
    global FLIGHT_ENROUTE_WAYPOINTS
    global FLIGHT_TURN_TO_SID
    global FLIGHT_APPROACH_WAYPOINTS
    global FLIGHT_ARRIVAL_RUNWAY
    global FLIGHT_GATE_TO_GATE_PLAN
    global FLIGHT_DEPARTURE_GATE
    global FLIGHT_ARRIVAL_GATE
    global departure_gate
    global arrival_gate


    #Set flight track time from FAA flight plan
    flightParameters = flightData.split("\n")
    for trxLine in trxLineSplit[0:trxLineSplit.index(flightParameters[-2])]:
        if(trxLine.startswith("TRACK_TIME")):
            FLIGHT_TRACK_TIME = trxLine.split(" ")[1]

    #Get flight route waypoints
    flightInstrumentData = flightParameters[-2].split(" ")
    flightRoute = flightParameters[-1].split(" ")

    #Set basic flight identification and instrument data
    FLIGHT_CALLSIGN = flightInstrumentData[1]
    FLIGHT_EQUIPMENT = flightInstrumentData[2]
    FLIGHT_CURRENT_POSITION = [flightInstrumentData[3], flightInstrumentData[4]]
    FLIGHT_TRUE_AIRSPEED = flightInstrumentData[5]
    FLIGHT_CURRENT_ALTITUDE_LEVEL = flightInstrumentData[6]
    FLIGHT_HEADING = flightInstrumentData[7]
    FLIGHT_DEPARTED = ('/' in flightRoute[5][0:10])
    FLIGHT_ROUTE = flightRoute[5].split(".")
    FLIGHT_DEPARTURE_AIRPORT = ("K" + FLIGHT_ROUTE[0])[-4:]
    FLIGHT_ARRIVAL_AIRPORT = ("K" + re.sub("[^A-Z]","", FLIGHT_ROUTE[-1]))[-4:]

    #Fetch departure and arrival airport location
    depAirportLoc = airportInterface.getLocation(FLIGHT_DEPARTURE_AIRPORT)
    arrAirportLoc = airportInterface.getLocation(FLIGHT_DEPARTURE_AIRPORT)

    #PHNL(Honolulu) and PANC(Anchorage) airport exceptions
    if "HNL" in FLIGHT_ROUTE[0]:
        FLIGHT_DEPARTURE_AIRPORT = "PHNL"
    if "HNL" in FLIGHT_ROUTE[-1]:
        FLIGHT_ARRIVAL_AIRPORT = "PHNL"
    if "ANC" in FLIGHT_ROUTE[0]:
        FLIGHT_DEPARTURE_AIRPORT = "PANC"
    if "ANC" in FLIGHT_ROUTE[-1]:
        FLIGHT_ARRIVAL_AIRPORT = "PANC"

    #Clean up flight plan and generate En route waypoints
    for entry in FLIGHT_ROUTE:
        if(entry is "/" or entry is ""):
            FLIGHT_ROUTE.remove(entry)
    FLIGHT_ROUTE = flightRoute[5].split("..")
    if('./.' in FLIGHT_ROUTE[0]):
        FLIGHT_ENROUTE_WAYPOINTS.append(FLIGHT_ROUTE[0].split("./.")[1])
    else:
        FLIGHT_ENROUTE_WAYPOINTS.append(FLIGHT_ROUTE[0].split(".")[-1])

    FLIGHT_ENROUTE_WAYPOINTS.extend(FLIGHT_ROUTE[1:])
    if not flightRoute[5].endswith(FLIGHT_ROUTE[-1].split('.')[0]):
        FLIGHT_ENROUTE_WAYPOINTS[-1] = FLIGHT_ROUTE[-1].split('.')[0]
    else:
        FLIGHT_ENROUTE_WAYPOINTS = FLIGHT_ENROUTE_WAYPOINTS[:-1]
    FLIGHT_ENROUTE_WAYPOINTS_COPY = FLIGHT_ENROUTE_WAYPOINTS
    #print(FLIGHT_ENROUTE_WAYPOINTS)
    FLIGHT_ENROUTE_WAYPOINTS = []
    if FLIGHT_ENROUTE_WAYPOINTS_COPY:
        if FLIGHT_ARRIVAL_AIRPORT[-3:] not in FLIGHT_ENROUTE_WAYPOINTS_COPY[-1]:
            FLIGHT_ROUTE = [FLIGHT_DEPARTURE_AIRPORT] + FLIGHT_ENROUTE_WAYPOINTS_COPY + [FLIGHT_ARRIVAL_AIRPORT]
            for waypoint in FLIGHT_ROUTE[1:-1]:
                FLIGHT_ENROUTE_WAYPOINTS.extend(process_waypoints(waypoint))

    #print(FLIGHT_ENROUTE_WAYPOINTS)

    departureRunwayOptions = []
    departureGateOptions = []
    arrivalRunwayOptions = []
    arrivalGateOptions = []

    for row in depArrData:
        if row[0] == FLIGHT_DEPARTURE_AIRPORT and row[-1] == "departure":
            departureRunwayOptions.append(row[1])
        if row[0] == FLIGHT_ARRIVAL_AIRPORT and row[-1] == "arrival":
            arrivalRunwayOptions.append(row[1])


    #---------------------------------------------------------------DEPARTURE PROCEDURES FOR ON-GROUND FLIGHTS BEGINS---------------------------------------------------------------#
    if not FLIGHT_DEPARTED:

        #Get departure airport layout from NATS
        departureAirportLayoutFile = open(NATS_SERVER + "/share/libairport_layout/Airport_Rwy/" + FLIGHT_DEPARTURE_AIRPORT + "_Nodes_Def.csv")
        departureAirportLayoutData = list(csv.reader(departureAirportLayoutFile, delimiter=','))

        for row in departureAirportLayoutData:
            if row[0].lower().startswith(("gate","park")):
                departureGateOptions.append(row[0].split("_")[1] + "_" + row[0].split("_")[2])

        while 1:
            #Get departure gate and runway inputs
            #FLIGHT_DEPARTURE_GATE = raw_input("\nPlease provide departure gate at " + FLIGHT_DEPARTURE_AIRPORT + "[" + ','.join(departureGateOptions) + "]: ")
            #FLIGHT_DEPARTURE_RUNWAY = raw_input("Please provide departure runway at " + FLIGHT_DEPARTURE_AIRPORT + "[" + ','.join(departureRunwayOptions) + "]: ")
            
            if not departure_gate:
                departure_gate = list(range(len(departureGateOptions)))
                random.shuffle(departure_gate)
            print(departure_gate)
            FLIGHT_DEPARTURE_GATE = departureGateOptions[departure_gate[0]]
            departure_gate.pop(0)
            FLIGHT_DEPARTURE_RUNWAY = departureRunwayOptions[random.randint(0,len(departureRunwayOptions))]

            if FLIGHT_DEPARTURE_GATE in departureGateOptions or FLIGHT_DEPARTURE_RUNWAY in departureRunwayOptions:
                break

        for row in departureAirportLayoutData:
            if((row[6] == FLIGHT_DEPARTURE_RUNWAY) and (row[7] == "Entry")):
                departureRunwayEntryPoint = row[0]
                departureRunwayEntryPointLoc = [float(row[2]), float(row[3])]

            if((row[8] == FLIGHT_DEPARTURE_RUNWAY) and (row[9] == "End")):
                departureRunwayTakeoffPoint = row[0]
                departureRunwayTakeoffPointLoc = [float(row[2]), float(row[3])]

            if(row[0].lower().startswith(("gate","park")) and row[0].endswith(FLIGHT_DEPARTURE_GATE)):
                FLIGHT_DEPARTURE_GATE = row[0]

        #Point till which aircraft maintains runway heading
        FLIGHT_TURN_TO_SID = [{'lat': -2 * departureRunwayEntryPointLoc[0] + 3 * departureRunwayTakeoffPointLoc[0], 'lon':-2 * departureRunwayEntryPointLoc[1] + 3 * departureRunwayTakeoffPointLoc[1], 'name': "TURN_TO_SID"}]

        #------Airports with no defined SID Legs------#
        if FLIGHT_DEPARTURE_AIRPORT in ["KMDW", "KORD"]:
            FLIGHT_SID_WAYPOINTS = ["ACITO"]
        elif FLIGHT_DEPARTURE_AIRPORT == "KPIT":
            FLIGHT_SID_WAYPOINTS = ["REVLOC"]
        elif FLIGHT_DEPARTURE_AIRPORT == "KPHL":
            FLIGHT_SID_WAYPOINTS = ["DQO"]
        elif FLIGHT_DEPARTURE_AIRPORT == "KPVD":
            FLIGHT_SID_WAYPOINTS = []
        #------Airports with no defined SID Legs------#

        #Select SID leading to flight plan
        else:
            sidProcedures = []
            for row in depArrData:
                if (row[0] == FLIGHT_DEPARTURE_AIRPORT) and (row[1] == FLIGHT_DEPARTURE_RUNWAY) and (row[3] == "departure"):
                    sidProcedures = row[2].split(",")

            collectiveSidLegs = []
            for sidProcedure in sidProcedures:
                try:
                    sidLegs = list(terminalAreaInterface.getProcedure_leg_names("SID", sidProcedure, FLIGHT_DEPARTURE_AIRPORT))
                    for leg in sidLegs[:]:
                        leg = str(leg)
                        if leg.startswith("RW"):
                            sidLegs.remove(leg)
                    collectiveSidLegs.append({'sidProc': sidProcedure, 'sidLegs': sidLegs})
                except:
                    pass

            sidNameLog = []
            sidLegsLog = []
            sidLegLastPoints = []
            sidLegFirstPoints = []
            for sid in collectiveSidLegs:
                sidProcName = sid['sidProc']
                for sidLeg in sid['sidLegs']:
                    sidLegLastPoints.append(list(terminalAreaInterface.getWaypoints_in_procedure_leg("SID", sidProcName, FLIGHT_DEPARTURE_AIRPORT, sidLeg))[-1])
                    sidLegFirstPoints.append(list(terminalAreaInterface.getWaypoints_in_procedure_leg("SID", sidProcName, FLIGHT_DEPARTURE_AIRPORT, sidLeg))[0])
                    sidNameLog.append(sidProcName)
                    sidLegsLog.append(sidLeg)

            if len(FLIGHT_ENROUTE_WAYPOINTS) > 0:
                #Calculate closest SID leg to first point on en route plan
                optimalIndices = closest_waypoint(get_lat_lon(sidLegLastPoints), FLIGHT_ENROUTE_WAYPOINTS[0])
                updatedSidFirstPoints = []
                for index in optimalIndices:
                    updatedSidFirstPoints.append(sidLegFirstPoints[index])

                optimalIndex = optimalIndices[closest_waypoint(get_lat_lon(updatedSidFirstPoints), FLIGHT_TURN_TO_SID[0])[0]]
                sidProcedure = sidNameLog[optimalIndex]
                selectedSidLeg = sidLegsLog[optimalIndex]
                FLIGHT_SID_WAYPOINTS = list(terminalAreaInterface.getWaypoints_in_procedure_leg("SID", sidProcedure, FLIGHT_DEPARTURE_AIRPORT, selectedSidLeg))
                FLIGHT_SID_PROCEDURE = sidProcedure
            else:
                sidProcedure = sidNameLog[0]
                FLIGHT_SID_WAYPOINTS = list(terminalAreaInterface.getWaypoints_in_procedure_leg("SID", sidProcedure, FLIGHT_DEPARTURE_AIRPORT, sidLegsLog[0]))
                FLIGHT_SID_PROCEDURE = sidProcedure

        #Standardize SID to waypoint format, with location 
        for waypoint in FLIGHT_SID_WAYPOINTS:
            waypointLocation = terminalAreaInterface.getWaypoint_Latitude_Longitude_deg(waypoint)
            if waypointLocation:
                FLIGHT_SID_WAYPOINTS[FLIGHT_SID_WAYPOINTS.index(waypoint)] = {'name': waypoint, 'lat': waypointLocation[0], 'lon': waypointLocation[1]}

        FLIGHT_SID_WAYPOINTS = FLIGHT_TURN_TO_SID + FLIGHT_SID_WAYPOINTS
        FLIGHT_DEPARTURE_GROUND_TAXI = list(airportInterface.get_taxi_route_from_A_To_B(FLIGHT_CALLSIGN, FLIGHT_DEPARTURE_AIRPORT, FLIGHT_DEPARTURE_GATE, departureRunwayEntryPoint))
        for waypoint in FLIGHT_DEPARTURE_GROUND_TAXI:
            for row in departureAirportLayoutData:
                if(row[0] == waypoint):
                    FLIGHT_DEPARTURE_GROUND_TAXI[FLIGHT_DEPARTURE_GROUND_TAXI.index(waypoint)] = {'lat': row[2], 'lon': row[3], 'name': waypoint}

        departureAirportLayoutFile.close()


    #---------------------------------------------------------------DEPARTURE PROCEDURES FOR ON-GROUND FLIGHTS ENDS-----------------------------------------------------------------#


    #------------------------------------------------------------------ARRIVAL PROCEDURES FOR ALL FLIGHTS BEGINS--------------------------------------------------------------------#

    #Get arrival airport layout from NATS
    arrivalAirportLayoutFile = open(NATS_SERVER + "/share/libairport_layout/Airport_Rwy/" + FLIGHT_ARRIVAL_AIRPORT + "_Nodes_Def.csv")
    arrivalAirportLayoutData = list(csv.reader(arrivalAirportLayoutFile, delimiter=','))

    for row in arrivalAirportLayoutData:
        if row[0].lower().startswith(("gate","park")):
            arrivalGateOptions.append(row[0].split("_")[1] + "_" + row[0].split("_")[2])

    while 1:
        #Get arrival gate and runway inputs
        #FLIGHT_ARRIVAL_GATE = raw_input("\nPlease provide arrival gate at " + FLIGHT_ARRIVAL_AIRPORT + "[" + ','.join(arrivalGateOptions) + "]: ")
        #FLIGHT_ARRIVAL_RUNWAY = raw_input("Please provide arrival runway at " + FLIGHT_ARRIVAL_AIRPORT + "[" + ','.join(arrivalRunwayOptions) + "]: ")

        if not arrival_gate:
            arrival_gate = list(range(len(arrivalGateOptions)))
            random.shuffle(arrival_gate)
        print(arrival_gate)
        FLIGHT_ARRIVAL_GATE = arrivalGateOptions[arrival_gate[0]]
        arrival_gate.pop(0)
        FLIGHT_ARRIVAL_RUNWAY = arrivalRunwayOptions[random.randint(0,len(arrivalRunwayOptions))]

        if FLIGHT_ARRIVAL_GATE in arrivalGateOptions or FLIGHT_ARRIVAL_RUNWAY in arrivalRunwayOptions:
            break


    #Get arrival runway and gate mapping from NATS
    arrivalRunwayExitPointLoc = []
    arrivalRunwayEntryPointLoc = []
    arrivalRunwayExitPoint = ""
    for row in arrivalAirportLayoutData:
        if((row[8].replace(" ", "") == FLIGHT_ARRIVAL_RUNWAY) and (row[9] == "End")):
            arrivalRunwayExitPoint = row[0]
            arrivalRunwayExitPointLoc = [float(row[2]), float(row[3])]
        if((row[7].replace(" ", "") == FLIGHT_ARRIVAL_RUNWAY) and (row[8] == "Entry")):
            arrivalRunwayEntryPoint = row[0]
            arrivalRunwayEntryPointLoc = {'lat': float(row[2]), 'lon': float(row[3]), 'name': str(row[7])}
        if(row[0].lower().startswith(("gate","park")) and row[0].endswith(FLIGHT_ARRIVAL_GATE)):
                FLIGHT_ARRIVAL_GATE = row[0]

    #Build ILS final approach path
    if FLIGHT_ARRIVAL_RUNWAY[-1] in ['L', 'R', 'C']:
        approachProcedure = "I" + FLIGHT_ARRIVAL_RUNWAY[-3:]
    else:
        approachProcedure = "I" + FLIGHT_ARRIVAL_RUNWAY[-2:]

    approachProcedureLegs = list(terminalAreaInterface.getProcedure_leg_names("APPROACH", approachProcedure, FLIGHT_ARRIVAL_AIRPORT))
    appProcLegLoc = get_lat_lon(approachProcedureLegs)
    #First available ILS approach leg for landing
    closestApproachLeg = approachProcedureLegs[0]
    FLIGHT_APPROACH_PROCEDURE = approachProcedure
    FLIGHT_APPROACH_WAYPOINTS = list(terminalAreaInterface.getWaypoints_in_procedure_leg("APPROACH", approachProcedure, FLIGHT_ARRIVAL_AIRPORT, closestApproachLeg))

    for approachWp in FLIGHT_APPROACH_WAYPOINTS:
        if FLIGHT_ARRIVAL_RUNWAY in approachWp:
       	    lastIndexApproach = FLIGHT_APPROACH_WAYPOINTS.index(approachWp)
    try:
        FLIGHT_APPROACH_WAYPOINTS = FLIGHT_APPROACH_WAYPOINTS[:(lastIndexApproach + 1)]
    except:
        pass

    for waypoint in FLIGHT_APPROACH_WAYPOINTS:
        try:
            waypointLocation = terminalAreaInterface.getWaypoint_Latitude_Longitude_deg(waypoint)
        except:
            waypointLocation = terminalAreaInterface.getWaypoint_Latitude_Longitude_deg(waypoint['name'])
        if waypointLocation:
            FLIGHT_APPROACH_WAYPOINTS[FLIGHT_APPROACH_WAYPOINTS.index(waypoint)] = {'name': waypoint, 'lat': waypointLocation[0], 'lon': waypointLocation[1]}


    starProcedures = []
    for row in depArrData:
        if (row[0] == FLIGHT_ARRIVAL_AIRPORT) and (row[3] == "arrival") and (row[1] == FLIGHT_ARRIVAL_RUNWAY):
            starProcedures = row[2].split(",")

    collectiveStarLegs = []
    for starProcedure in starProcedures:
        try:
            starLegs = list(terminalAreaInterface.getProcedure_leg_names("STAR", starProcedure, FLIGHT_ARRIVAL_AIRPORT))
            for leg in starLegs[:]:
                leg = str(leg)
                if leg.startswith("RW"):
                    starLegs.remove(leg)
            collectiveStarLegs.append({'starProc': starProcedure, 'starLegs': starLegs})
        except:
            pass

    starNameLog = []
    starLegLastPoints = []
    starLegFirstPoints = []
    starLegLog = []
    for star in collectiveStarLegs:
        starProcName = star['starProc']
        for starLeg in star['starLegs']:
            starLegLastPoints.append(list(terminalAreaInterface.getWaypoints_in_procedure_leg("STAR", starProcName, FLIGHT_ARRIVAL_AIRPORT, starLeg))[-1])
            starLegFirstPoints.append(list(terminalAreaInterface.getWaypoints_in_procedure_leg("STAR", starProcName, FLIGHT_ARRIVAL_AIRPORT, starLeg))[0])
            starNameLog.append(starProcName)
            starLegLog.append(starLeg)

    #Calculate closest STAR leg to first point on en route plan
    if len(FLIGHT_ENROUTE_WAYPOINTS) > 0:
        optimalIndices = closest_waypoint(get_lat_lon(starLegLastPoints), FLIGHT_ENROUTE_WAYPOINTS[-1])

        updatedStarFirstPoints = []
        for index in optimalIndices:
            updatedStarFirstPoints.append(starLegFirstPoints[index])

        optimalIndex = optimalIndices[closest_waypoint(get_lat_lon(updatedStarFirstPoints), FLIGHT_APPROACH_WAYPOINTS[0])[0]]
        starProcedure = starNameLog[optimalIndex]
        selectedStarLeg = starLegLog[optimalIndex]

        FLIGHT_STAR_WAYPOINTS = list(terminalAreaInterface.getWaypoints_in_procedure_leg("STAR", starProcedure, FLIGHT_ARRIVAL_AIRPORT, selectedStarLeg))
        FLIGHT_STAR_PROCEDURE = starProcedure

    else:
        starProcedure = starNameLog[0]
        FLIGHT_STAR_WAYPOINTS = list(terminalAreaInterface.getWaypoints_in_procedure_leg("STAR", starProcedure, FLIGHT_ARRIVAL_AIRPORT, starLegLog[0]))
        FLIGHT_STAR_PROCEDURE = starProcedure

    #Standardize STAR to waypoint format, with location
    for waypoint in FLIGHT_STAR_WAYPOINTS:
        waypointLocation = terminalAreaInterface.getWaypoint_Latitude_Longitude_deg(waypoint)
        if waypointLocation:
            FLIGHT_STAR_WAYPOINTS[FLIGHT_STAR_WAYPOINTS.index(waypoint)] = {'name': waypoint, 'lat': waypointLocation[0], 'lon': waypointLocation[1]}

    FLIGHT_ARRIVAL_GROUND_TAXI = list(airportInterface.get_taxi_route_from_A_To_B(FLIGHT_CALLSIGN, FLIGHT_ARRIVAL_AIRPORT, arrivalRunwayExitPoint, FLIGHT_ARRIVAL_GATE))

    for waypoint in FLIGHT_ARRIVAL_GROUND_TAXI:
        for row in arrivalAirportLayoutData:
            if(row[0] == waypoint):
                FLIGHT_ARRIVAL_GROUND_TAXI[FLIGHT_ARRIVAL_GROUND_TAXI.index(waypoint)] = {'lat': float(row[2]), 'lon': float(row[3]), 'name': waypoint}

    arrivalAirportLayoutFile.close()

    #Assemble Gate to Gate Flight Plan
    FLIGHT_GATE_TO_GATE_PLAN = list(FLIGHT_DEPARTURE_GROUND_TAXI) + list(FLIGHT_SID_WAYPOINTS) + list(FLIGHT_ENROUTE_WAYPOINTS) + list(FLIGHT_STAR_WAYPOINTS) + list(FLIGHT_APPROACH_WAYPOINTS) + list(FLIGHT_ARRIVAL_GROUND_TAXI)

    #Add Hold Short points
    for waypoint in FLIGHT_GATE_TO_GATE_PLAN:
        isRunwayNode = waypoint['name'].lower().startswith("rwy")
        previousNodeIndex = FLIGHT_GATE_TO_GATE_PLAN.index(waypoint) - 1
        holdPoint = {'name': 'HOLD_SHORT', 'lat': FLIGHT_GATE_TO_GATE_PLAN[previousNodeIndex]['lat'], 'lon': FLIGHT_GATE_TO_GATE_PLAN[previousNodeIndex]['lon']}
        if isRunwayNode and FLIGHT_GATE_TO_GATE_PLAN[previousNodeIndex]['name'].lower().startswith(("ramp", "txy", "park")):
            FLIGHT_GATE_TO_GATE_PLAN.insert(previousNodeIndex + 1, holdPoint)

    '''
    #Write flight plan in CSV format for plotting
    with open(NATS_SERVER + "/share/FlightPlanData/FlightPlans/FP_" + FLIGHT_CALLSIGN + ".csv", "wb") as pathCSV:
        for waypointSet in FLIGHT_GATE_TO_GATE_PLAN:
            if waypointSet != "NO_WP_NO_TRANS_ID":
                waypointName = waypointSet['name']
                latitude = waypointSet['lat']
                longitude = waypointSet['lon']
                try:
                    pathCSV.write(str(latitude) + ", " + str(longitude) + ", " + waypointName + "\n")
                except:
                    pathCSV.write(str(latitude) + ", " + str(longitude) + ", " + waypointName['name'] + "\n")


    pathCSV.close()
    '''

    #Generate updated flight path by joining components
    for wp in FLIGHT_DEPARTURE_GROUND_TAXI:
        FLIGHT_DEPARTURE_GROUND_TAXI[FLIGHT_DEPARTURE_GROUND_TAXI.index(wp)] = str("{\"id\": \"" + wp['name'] + "\"}")

    for wp in FLIGHT_ARRIVAL_GROUND_TAXI:
        FLIGHT_ARRIVAL_GROUND_TAXI[FLIGHT_ARRIVAL_GROUND_TAXI.index(wp)] = str("{\"id\": \"" + wp['name'] + "\"}")

    for wp in FLIGHT_ENROUTE_WAYPOINTS:
        FLIGHT_ENROUTE_WAYPOINTS[FLIGHT_ENROUTE_WAYPOINTS.index(wp)] = str(wp['name'])

    if not FLIGHT_DEPARTED:
        if len(FLIGHT_SID_PROCEDURE) > 0:
            FLIGHT_SID_PROCEDURE = FLIGHT_SID_PROCEDURE + "."
        trxFp = FLIGHT_DEPARTURE_AIRPORT + ".<" + ', '.join(FLIGHT_DEPARTURE_GROUND_TAXI) + ">." + FLIGHT_DEPARTURE_RUNWAY + "." + FLIGHT_SID_PROCEDURE + '..'.join(FLIGHT_ENROUTE_WAYPOINTS) + "." + FLIGHT_STAR_PROCEDURE + "." + FLIGHT_APPROACH_PROCEDURE + "." + FLIGHT_ARRIVAL_RUNWAY + ".<" + ', '.join(FLIGHT_ARRIVAL_GROUND_TAXI) + ">." + FLIGHT_ARRIVAL_AIRPORT
    else:
        if len(FLIGHT_STAR_PROCEDURE) > 0:
            FLIGHT_STAR_PROCEDURE = "." + FLIGHT_STAR_PROCEDURE
        trxFp = FLIGHT_DEPARTURE_AIRPORT + ".<>.." + '..'.join(FLIGHT_ENROUTE_WAYPOINTS) + FLIGHT_STAR_PROCEDURE + "." + FLIGHT_APPROACH_PROCEDURE + "." + FLIGHT_ARRIVAL_RUNWAY + ".<" + ', '.join(FLIGHT_ARRIVAL_GROUND_TAXI) + ">." + FLIGHT_ARRIVAL_AIRPORT

    if len(FLIGHT_ENROUTE_WAYPOINTS) > 0:

        newTrx.write("TRACK_TIME " + str(FLIGHT_TRACK_TIME) + "\n")

        flightParams = flightParameters[-2].split(" ")

        if not FLIGHT_DEPARTED:
            airport = airportInterface.select_airport(FLIGHT_DEPARTURE_AIRPORT);
            apt_elv = airport.getElevation();
            flightParams[6] = str(int(apt_elv/100))

        flightParams[1] = FLIGHT_CALLSIGN

        newTrx.write(" ".join(flightParams) + "\n")

        newTrx.write("    FP_ROUTE " + trxFp +"\n\n")

        mflFile.write(flightParams[1] + " " + str(int(aircraftInterface.select_aircraft(FLIGHT_CALLSIGN).getCruise_alt_ft()/100)) + "\n")


    #Clear all buffers for next flight
    FLIGHT_DEPARTED = False
    FLIGHT_TRACK_TIME = 0
    FLIGHT_CALLSIGN = ""
    FLIGHT_EQUIPMENT = ""
    FLIGHT_CURRENT_POSITION = []
    FLIGHT_TRUE_AIRSPEED = 0.0
    FLIGHT_CURRENT_ALTITUDE_LEVEL = 0
    FLIGHT_SID_PROCEDURE = ""
    FLIGHT_STAR_PROCEDURE = ""
    FLIGHT_APPROACH_PROCEDURE = ""
    FLIGHT_HEADING = 0
    FLIGHT_ROUTE = ""
    FLIGHT_DEPARTURE_AIRPORT = ""
    FLIGHT_ARRIVAL_AIRPORT = ""
    FLIGHT_DEPARTURE_RUNWAY = ""
    FLIGHT_DEPARTURE_GROUND_TAXI= []
    FLIGHT_ARRIVAL_GROUND_TAXI = []
    FLIGHT_TURN_TO_SID = []
    FLIGHT_SID_WAYPOINTS = []
    FLIGHT_STAR_WAYPOINTS = []
    FLIGHT_ENROUTE_WAYPOINTS = []
    FLIGHT_APPROACH_WAYPOINTS = []
    FLIGHT_ARRIVAL_RUNWAY = ""
    FLIGHT_GATE_TO_GATE_PLAN = []

def gate_to_gate_flight_plan(trxName = None):
    """
    Preprocessing TRX Data.
    """
    trxData = read_trx(trxName)
    trxLineSplit = trxData.split("\n")
    trxFlights = trxData.split("\n\n")[:-1]
    for flightData in trxFlights:

        if(flightData.split("\n")[-2].split(" ")[1] not in indexedFlights):
            continue

        trxDepartureAirport = re.compile('[A-Z]+').findall(flightData.split("\n")[-1].split(" ")[5])[0]
        trxArrivalAirport = re.compile('[A-Z]+').findall(flightData.split("\n")[-1].split(" ")[5])[-1]

        #Exception cases for Anchorage (PANC) and Honolulu (PHNL)
        if len(trxDepartureAirport) == 3:
            if trxDepartureAirport == "HNL":
                trxDepartureAirport = "PHNL"
            elif trxDepartureAirport == "ANC":
                trxDepartureAirport = "PANC"
            else:
                trxDepartureAirport = "K" + trxDepartureAirport

        if len(trxArrivalAirport) == 3:
            if trxArrivalAirport == "HNL":
                trxArrivalAirport = "PHNL"
            elif trxArrivalAirport == "ANC":
                trxArrivalAirport = "PANC"
            else:
                trxArrivalAirport = "K" + trxArrivalAirport

        if trxArrivalAirport in definedAirports and trxDepartureAirport in definedAirports:
            #Only for airports defined within NATS
            if flightData.split("\n")[-2].split(" ")[1] in indexedFlights:
                #Verifying that FAA flight plan was accepted by NATS
                print("Flight: " + flightData.split("\n")[-2].split(" ")[1])
                generate_save_flight_plan(flightData, trxLineSplit)
                print("Flight Plan Saved for " + flightData.split("\n")[-2].split(" ")[1] + "\n")

    newTrx.close()
    mflFile.close()
    depArrDataFile.close()

#Call method with location for the original TRX file containing FAA flight plans
gate_to_gate_flight_plan(NATS_SERVER + "/share/tg/trx/TRX_DEMO_SFO_PHX.trx")
