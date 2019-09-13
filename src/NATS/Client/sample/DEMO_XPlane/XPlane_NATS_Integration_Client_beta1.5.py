# NATS sample
#
# Optimal Synthesis Inc.
#
# Oliver Chen
# 06.21.2019
#
# This program read data file generated from XPlane simulator and send it to NATS Server
#
# Notice!
# This sample file must be executed on XPlane machine so the latest XPlane data can be constantly updated.
# If the data file is not updated, the aircraft state data won't change and the final trajectory result also won't show any change.

from jpype import *
from array import *
from datetime import datetime
import math
import os
import time
import csv

XPLANE_PATH = "PLEASE_ENTER_XPLANE_PATH_HERE"

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

# NATS simulation status definition
# You can get simulation status from the server and know what it refers to
NATS_SIMULATION_STATUS_READY = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_READY
NATS_SIMULATION_STATUS_START = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_START
NATS_SIMULATION_STATUS_PAUSE = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_PAUSE
NATS_SIMULATION_STATUS_RESUME = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_RESUME
NATS_SIMULATION_STATUS_STOP = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_STOP
NATS_SIMULATION_STATUS_ENDED = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_ENDED

if not os.path.exists(XPLANE_PATH) :
    print "Directory XPLANE_PATH does not exist"
else :
    NATSClientFactory = JClass('NATSClientFactory')
    natsClient = NATSClientFactory.getNATSClient()
    simulationInterface = natsClient.getSimulationInterface()
    equipmentInterface = natsClient.getEquipmentInterface()
    aircraftInterface = equipmentInterface.getAircraftInterface()
    
    environmentInterface = natsClient.getEnvironmentInterface()
    airportInterface = environmentInterface.getAirportInterface()
    terminalAreaInterface = environmentInterface.getTerminalAreaInterface()
    
    entityInterface = natsClient.getEntityInterface()
    controllerInterface = entityInterface.getControllerInterface()
    

    natsClient.login("admin")
    
    if simulationInterface is None:
        print "Can't get SimInterface from server"
    
    else:
        simulationInterface.startRealTime()
        traj_ac_id = 'ULI-111111'
        traj_ac_type = "B733"
        traj_start_time = time.time() # UTC time
        traj_origin_airport = "KPHX"
        traj_destination_airport = "KSFO"
        traj_cruise_alt = 33000.0
        traj_cruise_tas_knots = 430.0
        traj_origin_airport_elevation_ft = 13.0
        traj_destination_airport_elevation_ft = 1135.0

        time_step = 0 # sec
        
        cnt_loop = 0
        max_cnt_loop = 5 # Number of loop to be processed
        
        num_valid_state = 27 # Number of fields of a valid state record
        
        array_index = -1
        
        if (not(traj_ac_id is None) and (traj_ac_id != '')) :
            # Get time step of real-time simulation
            time_step = simulationInterface.get_realTime_simulation_time_step()
            time_step = 30.0
    
            while (cnt_loop < max_cnt_loop):
                # Data.txt is a trajectory output file generated by XPlane application
                # Please locate the path and filename so the program can open it.
                xPlaneDataFile = open(XPLANE_PATH + "/Data.txt")

                xPlaneData = list(csv.reader(xPlaneDataFile, delimiter='|'))
    
                array_index = array_index + 1
                
                if (array_index >= len(xPlaneData)) :
                    array_index = len(xPlaneData) - 1
                
                currentState = None
                
                tmpState = xPlaneData[array_index]
                if (len(tmpState) == num_valid_state) :
                    currentState = tmpState
                
                if (not(tmpState is None)) :
                    if (len(tmpState) == 0) or (tmpState[0].startswith('  _real,_time ')) :
                        array_index = array_index + 1
                    
                    while ((array_index < (len(xPlaneData) - 1)) or (len(tmpState) != num_valid_state)):
                        array_index = array_index + 1
                        if (array_index <= (len(xPlaneData) - 1)) :
                            tmpState = xPlaneData[array_index]
                            if (len(tmpState) == num_valid_state) :
                                currentState = tmpState
                            if (array_index == (len(xPlaneData) - 1)) :
                                break
                    
                    if (not(currentState is None)) and (len(currentState) == num_valid_state) :
                        traj_lat = float(currentState[-9])
                        traj_lon = float(currentState[-8])
                        traj_alt = float(currentState[-7])
                        traj_rocd = float(currentState[15])/60
                        traj_tas_knots = float(currentState[9])
                        traj_course_deg = float(currentState[-11])
                        traj_flight_phase = str(FLIGHT_PHASE_CRUISE) #Placeholder for now, dynamic flight phase from X Plane would be added to the simulation eventually.
                        
                        # Get epoch time in milli-seconds
                        t = int(round(time.time() * 1000))
                        
                        if (traj_ac_id not in list(aircraftInterface.getAllAircraftId())) :
                            # Create the trajectory profile data
                            simulationInterface.externalAircraft_create_trajectory_profile(traj_ac_id, traj_ac_type, traj_origin_airport, traj_destination_airport, traj_cruise_alt, traj_cruise_tas_knots, traj_lat, traj_lon, traj_alt, traj_rocd, traj_tas_knots, traj_course_deg, traj_flight_phase)
                            print "Creating external aircraft profile data"
    
                        else :
                            simulationInterface.externalAircraft_inject_trajectory_state_data(traj_ac_id, traj_lat, traj_lon, traj_alt, traj_rocd, traj_tas_knots, traj_course_deg, traj_flight_phase, t)
                            print "Sending external aircraft trajectory data to NATS Server at UTC time = ", t
                
                cnt_loop = cnt_loop + 1
                
                time.sleep(time_step)
    
    simulationInterface.stop()
    
    millis = int(round(time.time() * 1000))
    print "Outputting trajectory data.  Please wait...."
    # The trajectory output file will be saved on NATS_Server side
    simulationInterface.write_trajectories("DEMO_XPlane_" + str(millis) + ".csv")

    # Close connection from NATS Server
    natsClient.disConnect()

shutdownJVM()

