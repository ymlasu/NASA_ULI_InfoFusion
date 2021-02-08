'''
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Hari Iyer
Date: 05/04/2019
Update: 2019.06.25

Custom Gate to Gate flight plan generation module, with no requirement for FAA TRX flight plans.
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

# Get callsigns of all flights in the TRX
callsigns = raw_input("Please enter all the flight callsigns separated by ',' (Eg. ABC123,DEF456,GHI789):")
callsignList = callsigns.split(",")

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
        
    
    # Get arrival and destination airports
    departureAirport = ""
    arrivalAirport = ""
    airportList = airportInterface.getAllAirportCodesInNATS();
    while 1:
        departureAirport = raw_input("Please enter departure airport code among (" + ",".join(airportList) + "): ")
        arrivalAirport = raw_input("\nPlease enter arrival airport code among (" + ",".join(airportList) + "): ")

        if(departureAirport not in airportList or arrivalAirport not in airportList):
            print("\nInvalid airport(s) selected, please try again.")
        else:
            print("\n")
            break


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

    # =========================================================================

    departureTaxi = []
    if (flightTakenOff == "no"):
        if (departureAirport != "") and (selectedDepartureGate != "") and (selectedDepartureRunway != "") :
            design_taxi_plan = airportInterface.get_taxi_route_from_A_To_B("DUMMY", departureAirport, selectedDepartureGate, selectedDepartureRunway)
            if not(design_taxi_plan is None) and (1 < len(design_taxi_plan)):
                departureTaxi = design_taxi_plan
                for i in range(0, len(design_taxi_plan)) :
                    print "Departing taxi_plan waypoint id = ", design_taxi_plan[i]
                    
        if (departureTaxi is None) or (len(departureTaxi) < 2) :
            print("\nPlease refer to functions getLayout_node_map(String airport_code) and getLayout_node_data(String airport_code) in API Documentation for airport ground nodes to build following taxi plans.")
    
            departureTaxiString = raw_input("\nEnter nodes for departure taxi, from gate to the runway threshold separated by ',' (Eg. Gate_01_001, Ramp_01_001,.....,Txy_A_009, Rwy_01_001): ")
            departureTaxi = departureTaxiString.split(",")

    # =========================================================================
    
    design_taxi_plan = None # Reset
    arrivalTaxi = []

    if (departureAirport != "") and (selectedArrivalGate != "") and (selectedArrivalRunway != "") :
        design_taxi_plan = airportInterface.get_taxi_route_from_A_To_B("DUMMY", arrivalAirport, selectedArrivalRunway, selectedArrivalGate)
        if not(design_taxi_plan is None) and (1 < len(design_taxi_plan)) :
            arrivalTaxi = design_taxi_plan
            for i in range(0, len(design_taxi_plan)) :
                print "Arriving taxi_plan waypoint id = ", design_taxi_plan[i]

    if (arrivalTaxi is None) or (len(arrivalTaxi) < 2) :
        arrivalTaxiString = raw_input("\nEnter nodes for arrival taxi, from runway end to the gate separated by ',' (Eg. Rwy_01_001, Txy_A_009,.....,Ramp_01_001, Gate_01_001): ")
        arrivalTaxi = arrivalTaxiString.split(",")
    
    # =========================================================================

    sidProcedures = []
    selectedSidProcedure = ""
    if (flightTakenOff == "no"):
        
        # Get all SID procedures for departure airport
        sidProcedures = terminalAreaInterface.getAllSids(departureAirport)
        if not sidProcedures:
            print(departureAirport + " has no SID procedures.\n")
            selectedSidProcedure = ""
            
        else:
            while 1:
                selectedSidProcedure = raw_input("\nPlease choose a SID procedure for departure from " + departureAirport + " among [" + ",".join(sidProcedures) + "]: ")
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

    # =========================================================================
    
    # Flight plan string generation
    if (departureTaxi == [""] and flightTakenOff == "no"):
        print("No departure taxi route provided.\n")
        departureTaxi = []

    if (arrivalTaxi == [""]):
        print("No arrival taxi route provided.\n")
        arrivalTaxi = []
    
    augmentedFlightPlan = departureAirport
    if (departureTaxi is None) or (len(departureTaxi) == 0) :
        augmentedFlightPlan += "./"
    else :
        augmentedFlightPlan += ".<"
    
    for airportGroundNode in departureTaxi:
        augmentedFlightPlan = augmentedFlightPlan + "{\"id\": \"" + airportGroundNode + "\"}, "
    
    
    if (len(departureTaxi) > 0) :
        augmentedFlightPlan = augmentedFlightPlan[:-2]
        augmentedFlightPlan += ">"

    if not(departureRunwayID is None) and (departureRunwayID != "") :
        augmentedFlightPlan += "." + departureRunwayID

    if not(selectedSidProcedure is None) and (selectedSidProcedure != "") :
        augmentedFlightPlan += "." + selectedSidProcedure

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