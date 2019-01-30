# This sample program demonstrates some Aircraft function.
#
# Oliver Chen
# 01.11.2019
#
# Users can learn how to obtain aircraft instance, show related aircraft information, start/pause/resume simulation and output result trajectory file.

from jpype import *
from array import *

import os
import time
import datetime

from shutil import copyfile
from shutil import rmtree

import PostProcessor as pp

classpath = "dist/nats-client.jar:dist/nats-shared.jar"

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

planned_dirname = ""
output_filename = ""

if simulationInterface is None:
    print "Can't get SimulationInterface from server"

else:
    simulationInterface.clear_trajectory()
    
    environmentInterface.load_rap("share/tg/rap")
    aircraftInterface.load_aircraft("share/tg/trx/TRX_DEMO_beta1.0_100rec.trx", "share/tg/trx/TRX_DEMO_beta1.0_100rec_mfl.trx")
    
    if not(aircraftInterface is None):
        aircraftIdArray_withinZone = aircraftInterface.getAircraftIds(float(30.0), float(35.0), float(-115.0), float(-90.0), float(-1.0), float(-1.0))
        if (not(aircraftIdArray_withinZone is None) and (len(aircraftIdArray_withinZone) > 0)) :
            i = 0
            for i in range(0, len(aircraftIdArray_withinZone)):
                curAcId = aircraftIdArray_withinZone[i]
                print "Aircraft id in selected zone = ", curAcId
        
        print "****************************************"
        
        curAircraft = aircraftInterface.select_aircraft("ULI-3AFSD3DC24")
        if not(curAircraft is None):
            airborne_flight_plan_waypoint_name_array = curAircraft.getFlight_plan_waypoint_name_array()
            for j in range(0, len(airborne_flight_plan_waypoint_name_array)) :
                print "ULI-3AFSD3DC24 airborne flight plan waypoint name = ", airborne_flight_plan_waypoint_name_array[j]
            print ""

        aircraft_3E6A0495F1 = aircraftInterface.select_aircraft("ULI-3E6A0495F1")
        aircraft_3E6A0495F1.delay_departure(100) # Delay the departure time for 100 sec
        
    simulationInterface.setupSimulation(10000, 10)
    
    # Start the simulation for 1000 secs then pause
    simulationInterface.start(1000)

    while True:
        server_runtime_sim_status = simulationInterface.get_runtime_sim_status()
        print "Time:", datetime.datetime.now(), ", simulation continuing.... "
        if (server_runtime_sim_status == NATS_SIMULATION_STATUS_PAUSE) :
            break
        else:
            time.sleep(1)

    aircraft_3E6A0495F1 = aircraftInterface.select_aircraft("ULI-3E6A0495F1")
    if not(aircraft_3E6A0495F1 is None):
        print "****************************************"
        print "ULI-3E6A0495F1 (pausing at", simulationInterface.get_curr_sim_time(), "sec), latitude = ", aircraft_3E6A0495F1.getLatitude_deg(), ", longitude = ", aircraft_3E6A0495F1.getLongitude_deg(), ", altitude = ", aircraft_3E6A0495F1.getAltitude_ft()
        print "****************************************"
    
    # Resume and continue the simulation
    simulationInterface.resume()
    
    # Use a while loop to constantly check server status.  When server simulation finishes, continue to output the trajectory data
    while True:
        server_runtime_sim_status = simulationInterface.get_runtime_sim_status()
        print "Time:", datetime.datetime.now(), ", simulation continuing.... "
        if (server_runtime_sim_status == NATS_SIMULATION_STATUS_ENDED) :
            break
        else:
            time.sleep(1)

    millis = int(round(time.time() * 1000))
    print "Outputting trajectory data.  Please wait...."
    
    planned_dirname = os.path.splitext(os.path.basename(__file__))[0] + "_" + str(millis)
    output_filename = planned_dirname + ".csv"
    
    # The trajectory output file will be saved on NATS_Server side
    simulationInterface.write_trajectories(output_filename)
    
    aircraftInterface.release_aircraft()
    environmentInterface.release_rap()

# Close connection from NATS Server
natsClient.disConnect()

# =========================================================

# The following statements read the result trajectory files and display plotting.
# Notice!!!!
# The following statements assume that NATS_Client and NATS_Server are installed on the same machine.
# If NATS_Server is installed on another machine, the following Python codes will not work due to inability to access the server files.

# Create temp directory on NATS_Server side and copy the result trajectory file into it
planned_dirname = "tmp_" + planned_dirname
os.makedirs("../NATS_Server/" + planned_dirname)
copyfile("../NATS_Server/" + output_filename, "../NATS_Server/" + planned_dirname + "/" + output_filename)

post_process = pp.PostProcessor(file_path = "../NATS_Server/" + planned_dirname,
                                ac_name = 'ULI-3E6A0495F1');
post_process.plotSingleAircraftTrajectory();

# Delete temp directory
print "Deleting directory:", planned_dirname
rmtree("../NATS_Server/" + planned_dirname) 

shutdownJVM()