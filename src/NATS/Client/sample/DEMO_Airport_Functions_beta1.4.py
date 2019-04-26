# NATS sample
#
# Optimal Synthesis Inc.
#
# Oliver Chen
# 03.25.2019
#
# Samples of airport-related functions

from jpype import *

import os
import time

classpath = "dist/nats-client.jar:dist/nats-shared.jar:dist/json.jar:dist/rmiio-2.1.2.jar:dist/commons-logging-1.2.jar"

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
    print "Airport Full Name =", airportName

    print "************************************************"

    runways = airportInterface.getAllRunways("KSFO")
    if not(runways is None) :
        for j in range(0, len(runways)) :
            print "Runway = ", runways[j][0], ", waypoing id = ", runways[j][1]
    else :
        print "No runway data"

    print "************************************************"
    
    runwayExits = airportInterface.getRunwayExits("KABQ", "RW26")
    if not(runwayExits is None) :
        for j in range(0, len(runwayExits)) :
            print "Runway exit of airport KABQ = ", runwayExits[j]
    else :
        print "No runway exit data"
    
    print "************************************************"

    allSids = terminalAreaInterface.getAllSids("KSFO")
    if not(allSids is None) :
        for j in range(0, len(allSids)) :
            print "KSFO --> avail sid = ", allSids[j]

    print "************************************************"
    
    allStars = terminalAreaInterface.getAllStars("KSFO")
    if not(allStars is None) :
        for j in range(0, len(allStars)) :
            print "KSFO --> avail star = ", allStars[j]
    
    print "************************************************"
    
    allApproaches = terminalAreaInterface.getAllApproaches("KSFO")
    if not(allApproaches is None) :
        for j in range(0, len(allApproaches)) :
            print "KSFO --> avail approach = ", allApproaches[j]
            
    print "************************************************"
    
    departureRunway = airportInterface.getDepartureRunway("SWA1897")
    print "departureRunway = ", departureRunway
 
    arrivalRunway = airportInterface.getArrivalRunway("SWA1897")
    print "arrivalRunway = ", arrivalRunway

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

    aircraftInterface.release_aircraft()
    environmentInterface.release_rap()

# Close connection from NATS Server
natsClient.disConnect()

shutdownJVM()