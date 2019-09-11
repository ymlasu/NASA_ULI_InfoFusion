'''
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Hari Iyer
Date: 08/03/2019
Update: 2019.06.20

Gate to Gate flight plan generation module. Please refer to documentation under NATS_Client/sample/GateToGateFpReadme.pdf for details.
'''

from jpype import *
from array import *
import PathVisualizer
import os
import time

env_NATS_CLIENT_HOME = os.environ.get('NATS_CLIENT_HOME')

str_NATS_CLIENT_HOME = ""

if not(env_NATS_CLIENT_HOME is None) :
    str_NATS_CLIENT_HOME = env_NATS_CLIENT_HOME + "/"

classpath = str_NATS_CLIENT_HOME + "dist/nats-client.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/nats-shared.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/json.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/rmiio-2.1.2.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/commons-logging-1.2.jar"

startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % classpath)

NATSClientFactory = JClass('NATSClientFactory')
natsClient = NATSClientFactory.getNATSClient()
simulationInterface = natsClient.getSimulationInterface()
equipmentInterface = natsClient.getEquipmentInterface()
aircraftInterface = equipmentInterface.getAircraftInterface()
safetyMetricsInterface = natsClient.getSafetyMetricsInterface()
environmentInterface = natsClient.getEnvironmentInterface()
airportInterface = environmentInterface.getAirportInterface()
terminalAreaInterface = environmentInterface.getTerminalAreaInterface()
entityInterface = natsClient.getEntityInterface()
controllerInterface = entityInterface.getControllerInterface()
pilotInterface = entityInterface.getPilotInterface()

natsClient.login("admin")

# Load environment data
environmentInterface.load_rap("share/tg/rap")

#Custom TRX can be set here
aircraftInterface.load_aircraft("share/tg/trx/TRX_DEMO_LAS_LAX.trx", "share/tg/trx/TRX_DEMO_LAS_LAX_mfl.trx")


# Get callsigns of all flights in the TRX
callsignList = aircraftInterface.getAllAircraftId()

# Iterate through flights to generate Gate to Gate flight plans and store them in the TRX file.
for callsign in callsignList:
    
    print("Augmented flight plan generation for aircraft: " + callsign)
    print("-----------------------------------------------------------")
    
    # Get flight initial status
    while 1:
        flightTakenOff = raw_input("Has the aircraft already taken off? (Please answer yes/no): ")
        flightTakenOff = flightTakenOff.lower()
        if flightTakenOff not in ['yes','no']:
            print("\nInvalid input, please try again.")
        else: 
            print("\n")
            break
        
    # Get flight instance for the callsign name
    flight = aircraftInterface.select_aircraft(callsign)
    
    # Get arrival and destination airports
    departureAirport = airportInterface.getDepartureAirport(callsign)
    arrivalAirport = airportInterface.getArrivalAirport(callsign)

    # Get arrival and departure airport gates
    departureGates = []
    if (flightTakenOff == "no"):
        departureGates = list(airportInterface.getAllGates(departureAirport))
    arrivalGates = list(airportInterface.getAllGates(arrivalAirport))
    
    # Get arrival and departure airport runways
    departureRunways = {}
    if (flightTakenOff == "no"):
        departureRunways = {key.replace(" ", ""): value.replace(" ", "") for (key, value) in  airportInterface.getAllRunways(departureAirport)}
    arrivalRunways =  {key.replace(" ", ""): value.replace(" ", "") for (key, value) in airportInterface.getAllRunways(arrivalAirport)}
    
    selectedDepartureGate = ""
    selectedDepartureRunway = ""
    if flightTakenOff == "no":
        while 1:
            selectedDepartureGate = raw_input("Please choose a departure gate at " + departureAirport + " among [" + ",".join(departureGates) + "]: ")
            if selectedDepartureGate not in departureGates:
                print("\nInvalid gate selected, please try again.")
            else: 
                print("\n")
                break
        
        while 1:
            selectedDepartureRunway = raw_input("Please choose a departure runway at " + departureAirport + " among [" + ",".join(departureRunways.keys()) + "]: ")
            if selectedDepartureRunway not in departureRunways.keys():
                print("\nInvalid runway selected, please try again.")
            else:
                print("\n")
                break
        
    while 1:
        selectedArrivalGate = raw_input("Please choose an arrival gate at " + arrivalAirport + " among [" + ",".join(arrivalGates) + "]: ")
        if selectedArrivalGate not in arrivalGates:
            print("\nInvalid gate selected, please try again.")
        else: 
            print("\n")
            break
        
    while 1:
        selectedArrivalRunway = raw_input("Please choose an arrival runway at " + arrivalAirport + " among [" + ",".join(arrivalRunways.keys()) + "]: ")
        if selectedArrivalRunway not in arrivalRunways.keys():
            print("\nInvalid runway selected, please try again.")
        else: 
            print("\n")
            break


    departureRunwayID = selectedDepartureRunway
    arrivalRunwayID = selectedArrivalRunway
    
    if selectedDepartureRunway:
        selectedDepartureRunway = departureRunways[selectedDepartureRunway]
        
    runwayEnds = airportInterface.getRunwayEnds(arrivalAirport, selectedArrivalRunway)
    if not runwayEnds:
        runwayEnds = airportInterface.getRunwayEnds(arrivalAirport, selectedArrivalRunway + " ")
    selectedArrivalRunway = list(runwayEnds)[1]
    
    
    departureTaxi = []
    if (flightTakenOff == "no"):
        departureTaxi = airportInterface.get_taxi_route_from_A_To_B(callsign, departureAirport, selectedDepartureGate, selectedDepartureRunway)

    arrivalTaxi = airportInterface.get_taxi_route_from_A_To_B(callsign, arrivalAirport, selectedArrivalRunway, selectedArrivalGate)
    
    sidProcedures = []
    selectedSidProcedure = []
    if (flightTakenOff == "no"):
        
        # Get all SID procedures for departure airport
        sidProcedures = terminalAreaInterface.getAllSids(departureAirport)
        if not sidProcedures:
            print(departureAirport + " has no SID procedures.\n")
            selectedSidProcedure = ""
            
        else:
            while 1:
                selectedSidProcedure = raw_input("Please choose a SID procedure for departure from " + departureAirport + " among [" + ",".join(sidProcedures) + "]: ")
                if selectedSidProcedure not in sidProcedures:
                    print("\nInvalid SID procedure selected, please try again.\n")
                else: 
                    print("\n")
                    break


    # Get Enroute waypoints in flight plan
    enrouteWaypoints = raw_input("Please enter enroute waypoints in flight plan separated by ',' (Eg. BOILE,LOSHN,BLH): ")
    
    # Get all STAR procedures for arrival airport
    starProcedures = terminalAreaInterface.getAllStars(arrivalAirport)
    while 1:
        selectedStarProcedure = raw_input("\nPlease choose a STAR procedure for arrival into " + arrivalAirport + " among [" + ",".join(starProcedures) + "]: ")
        if selectedStarProcedure not in starProcedures:
            print("\nInvalid STAR procedure selected, please try again.\n")
        else: 
            print("\n")
            break

    # Get all APPROACH procedures for arrival airport
    approachProcedures = terminalAreaInterface.getAllApproaches(arrivalAirport)
    while 1:
        selectedApproachProcedure = raw_input("Please choose an Approach procedure for arrival into " + arrivalAirport + " among [" + ",".join(approachProcedures) + "]: ")
        if selectedApproachProcedure not in approachProcedures:
            print("\nInvalid Approach procedure selected, please try again.\n")
        else: 
            print("\n")
            break

    
    # Flight plan string generation
    if (not departureTaxi and flightTakenOff == "no"):
        print("No default departure taxi route available, please refer to functions getLayout_node_map(String airport_code) and getLayout_node_data(String airport_code) in API Documentation for airport ground nodes to build a taxi plan.\n")
        departureTaxi = []
    if (not arrivalTaxi):
        print("No default arrival taxi route available, please refer to functions getLayout_node_map(String airport_code) and getLayout_node_data(String airport_code) in API Documentation for airport ground nodes to build a taxi plan.\n")
        arrivalTaxi = []
    
    if (flightTakenOff == "no") :
        augmentedFlightPlan = departureAirport + ".<"
    else :
        augmentedFlightPlan = departureAirport + "./"
    
    for airportGroundNode in departureTaxi:
        augmentedFlightPlan = augmentedFlightPlan + "{\"id\": \"" + airportGroundNode + "\"}, "
        
    if (len(departureTaxi) > 0 and selectedSidProcedure is not ""):
        augmentedFlightPlan = augmentedFlightPlan[:-2]
        augmentedFlightPlan += ">." + departureRunwayID + "." + selectedSidProcedure + "." + enrouteWaypoints.replace(",", "..") + "." + selectedStarProcedure + "." + selectedApproachProcedure + "." + arrivalRunwayID + ".<"
    
    elif (len(departureTaxi) > 0 and selectedSidProcedure is ""):
        augmentedFlightPlan = augmentedFlightPlan[:-2]
        augmentedFlightPlan += ">." + departureRunwayID + "." + enrouteWaypoints.replace(",", "..") + "." + selectedStarProcedure + "." + selectedApproachProcedure + "." + arrivalRunwayID + ".<"
    else:
        augmentedFlightPlan += "." + enrouteWaypoints.replace(",", "..") + "." + selectedStarProcedure + "." + selectedApproachProcedure + "." + arrivalRunwayID + ".<"

    for airportGroundNode in arrivalTaxi:
        augmentedFlightPlan = augmentedFlightPlan + "{\"id\": \"" + airportGroundNode + "\"}, "
    
    if(len(arrivalTaxi) > 0):
        augmentedFlightPlan = augmentedFlightPlan[:-2]
    augmentedFlightPlan += ">." + arrivalAirport
    
    print("The augmented flight plan for flight " + callsign + " is as follows. FP_ROUTE value in the original TRX can be replaced by this flight plan.")
    print(augmentedFlightPlan)
    print("\n\n")
        
aircraftInterface.release_aircraft()
environmentInterface.release_rap()

natsClient.disConnect()
shutdownJVM()
