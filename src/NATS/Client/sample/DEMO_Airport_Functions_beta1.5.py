# NATS sample
#
# Optimal Synthesis Inc.
#
# Oliver Chen
# 06.26.2019
#
# Samples of airport-related functions

from jpype import *

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


# Flight phase value definition
# You can detect and know the flight phase by checking its value
FLIGHT_PHASE_PREDEPARTURE = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_PREDEPARTURE;
FLIGHT_PHASE_ORIGIN_GATE = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_ORIGIN_GATE;
FLIGHT_PHASE_PUSHBACK = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_PUSHBACK;
FLIGHT_PHASE_RAMP_DEPARTING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_RAMP_DEPARTING;
FLIGHT_PHASE_TAXI_DEPARTING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TAXI_DEPARTING;
FLIGHT_PHASE_RUNWAY_THRESHOLD_DEPARTING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_RUNWAY_THRESHOLD_DEPARTING;
FLIGHT_PHASE_TAKEOFF = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TAKEOFF;
FLIGHT_PHASE_CLIMBOUT = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_CLIMBOUT;
FLIGHT_PHASE_HOLD_IN_DEPARTURE_PATTERN = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_HOLD_IN_DEPARTURE_PATTERN;
FLIGHT_PHASE_CLIMB_TO_CRUISE_ALTITUDE = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_CLIMB_TO_CRUISE_ALTITUDE;
FLIGHT_PHASE_TOP_OF_CLIMB = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TOP_OF_CLIMB;
FLIGHT_PHASE_CRUISE = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_CRUISE;
FLIGHT_PHASE_HOLD_IN_ENROUTE_PATTERN = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_HOLD_IN_ENROUTE_PATTERN;
FLIGHT_PHASE_TOP_OF_DESCENT = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TOP_OF_DESCENT;
FLIGHT_PHASE_INITIAL_DESCENT = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_INITIAL_DESCENT;
FLIGHT_PHASE_HOLD_IN_ARRIVAL_PATTERN = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_HOLD_IN_ARRIVAL_PATTERN
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

AIRCRAFT_CLEARANCE_PUSHBACK = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_PUSHBACK
AIRCRAFT_CLEARANCE_TAXI_DEPARTING = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_TAXI_DEPARTING
AIRCRAFT_CLEARANCE_TAKEOFF = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_TAKEOFF
AIRCRAFT_CLEARANCE_ENTER_ARTC = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_ENTER_ARTC
AIRCRAFT_CLEARANCE_DESCENT_FROM_CRUISE = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_DESCENT_FROM_CRUISE
AIRCRAFT_CLEARANCE_ENTER_TRACON = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_ENTER_TRACON
AIRCRAFT_CLEARANCE_APPROACH = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_APPROACH
AIRCRAFT_CLEARANCE_TOUCHDOWN = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_TOUCHDOWN
AIRCRAFT_CLEARANCE_TAXI_LANDING = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_TAXI_LANDING
AIRCRAFT_CLEARANCE_RAMP_LANDING = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_RAMP_LANDING

# NATS simulation status definition
# You can get simulation status from the server and know what it refers to
NATS_SIMULATION_STATUS_READY = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_READY
NATS_SIMULATION_STATUS_START = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_START
NATS_SIMULATION_STATUS_PAUSE = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_PAUSE
NATS_SIMULATION_STATUS_RESUME = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_RESUME
NATS_SIMULATION_STATUS_STOP = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_STOP
NATS_SIMULATION_STATUS_ENDED = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_ENDED


NATSClientFactory = JClass('NATSClientFactory')
natsClient = NATSClientFactory.getNATSClient()
simulationInterface = natsClient.getSimulationInterface()
equipmentInterface = natsClient.getEquipmentInterface()
aircraftInterface = equipmentInterface.getAircraftInterface()

environmentInterface = natsClient.getEnvironmentInterface()
airportInterface = environmentInterface.getAirportInterface()
terminalAreaInterface = environmentInterface.getTerminalAreaInterface()

natsClient.login("admin")

if simulationInterface is None:
    print "Can't get SimulationInterface from server"

else:
    simulationInterface.clear_trajectory()
    environmentInterface.load_rap("share/tg/rap")
    aircraftInterface.load_aircraft("share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx", "share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx")

    airportName = airportInterface.getFullName("KSFO")
    print "KSFO airport full name =", airportName

    print "************************************************"

    # Get all runways
    runways = airportInterface.getAllRunways("KSFO")
    if not(runways is None) :
        for j in range(0, len(runways)) :
            print "Runway in KSFO = ", runways[j][0], ", waypoing id = ", runways[j][1]
    else :
        print "No runway data"

    print "************************************************"
    
    # Get runway exits of the airport
    runwayExits = airportInterface.getRunwayExits("KABQ", "RW26")
    if not(runwayExits is None) :
        for j in range(0, len(runwayExits)) :
            print "Exit point on runway RW26 at airport KABQ = ", runwayExits[j]
    else :
        print "No runway exit data"
    
    print "************************************************"

    # Get all SID procedures of the airport
    allSids = terminalAreaInterface.getAllSids("KSFO")
    if not(allSids is None) :
        for curProc in allSids :
            # Get procedure leg names
            arrayLegNames = terminalAreaInterface.getProcedure_leg_names("SID", curProc, "KSFO")
            if not (arrayLegNames is None) :
                for curLegName in arrayLegNames :
                    # Get waypoints of the leg
                    arrayWaypoints = terminalAreaInterface.getWaypoints_in_procedure_leg("SID", curProc, "KSFO", curLegName)
                    if not (arrayWaypoints is None) :
                        for curWaypoint in arrayWaypoints :
                            print "KSFO --> SID:", curProc, ". leg = ", curLegName, ", wp = ", curWaypoint

    print "************************************************"
    
    # Get all STAR procedures of the airport
    allStars = terminalAreaInterface.getAllStars("KSFO")
    if not(allStars is None) :
        for curProc in allStars :
            # Get procedure leg names
            arrayLegNames = terminalAreaInterface.getProcedure_leg_names("STAR", curProc, "KSFO")
            if not (arrayLegNames is None) :
                for curLegName in arrayLegNames :
                    # Get waypoints of the leg
                    arrayWaypoints = terminalAreaInterface.getWaypoints_in_procedure_leg("STAR", curProc, "KSFO", curLegName)
                    if not (arrayWaypoints is None) :
                        for curWaypoint in arrayWaypoints :
                            print "KSFO --> STAR:", curProc, ". leg = ", curLegName, ", wp = ", curWaypoint
    
    print "************************************************"
    
    allApproaches = terminalAreaInterface.getAllApproaches("KSFO")
    if not(allApproaches is None) :
        for curProc in allApproaches :
            # Get procedure leg names
            arrayLegNames = terminalAreaInterface.getProcedure_leg_names("APPROACH", curProc, "KSFO")
            if not (arrayLegNames is None) :
                for curLegName in arrayLegNames :
                    # Get waypoints of the leg
                    arrayWaypoints = terminalAreaInterface.getWaypoints_in_procedure_leg("APPROACH", curProc, "KSFO", curLegName)
                    if not (arrayWaypoints is None) :
                        for curWaypoint in arrayWaypoints :
                            print "KSFO --> APPROACH:", curProc, ". leg = ", curLegName, ", wp = ", curWaypoint
    
    print "************************************************"
    
    departureRunway = airportInterface.getDepartureRunway("SWA1897")
    print "SWA1897 departureRunway = ", departureRunway
 
    arrivalRunway = airportInterface.getArrivalRunway("SWA1897")
    print "SWA1897 arrivalRunway = ", arrivalRunway

    print "************************************************"
    
    # Calculate a route from point A to B
    # The resulted route is not loaded in NATS.  It only outputs the array of waypoint ids.
    design_taxi_plan_KSFO = airportInterface.get_taxi_route_from_A_To_B("SWA1897", "KSFO", "Gate_F_086", "Rwy_02_002")
    if not(design_taxi_plan_KSFO is None) :
        for i in range(0, len(design_taxi_plan_KSFO)) :
            print "design_taxi_plan_KSFO waypoint id = ", design_taxi_plan_KSFO[i]

    print "************************************************"

    # Calculate a route from point A to B
    # The resulted route is not loaded in NATS.  It only outputs the array of waypoint ids.
    design_taxi_plan_KPHX = airportInterface.get_taxi_route_from_A_To_B("SWA1897", "KPHX", "Rwy_03_009", "Gate_04_C16") 
    if not(design_taxi_plan_KPHX is None) :
        for i in range(0, len(design_taxi_plan_KPHX)) :
            print "design_taxi_plan_KPHX waypoint id = ", design_taxi_plan_KPHX[i]

    print "************************************************"

    # Show airport layout node data
    array_node_data = airportInterface.getLayout_node_data("KABQ")
    if not(array_node_data is None) :
        for i in range(0, len(array_node_data)) :
            print "KABQ node data = ", array_node_data[i][0], ", ", array_node_data[i][2], ", ", array_node_data[i][3], ", ", array_node_data[i][4], ", ", array_node_data[i][5], ", ", array_node_data[i][6]

    aircraftInterface.release_aircraft()
    environmentInterface.release_rap()

# Close connection from NATS Server
natsClient.disConnect()

shutdownJVM()