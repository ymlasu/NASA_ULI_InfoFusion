from jpype import *
from array import *
from datetime import datetime
import os
import time
import csv

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

entityInterface = natsClient.getEntityInterface()
controllerInterface = entityInterface.getControllerInterface()


if simulationInterface is None:
    print "Can't get SimInterface from server"

else:
    simulationInterface.clear_trajectory()
    environmentInterface.load_rap("share/tg/rap")
    
    traj_ac_id = "ABC123"
    traj_ac_type = "B733"
    traj_start_time = time.time() # UTC time
    traj_origin_airport = "KPHX"
    traj_destination_airport = "KSFO"
    traj_cruise_alt = 33000.0
    traj_cruise_tas_knots = 430.0
    traj_origin_airport_elevation_ft = 13.0
    traj_destination_airport_elevation_ft = 1135.0
    
    # Create the trajectory profile data
    simulationInterface.externalAircraft_create_trajectory_profile(traj_ac_id, traj_ac_type, traj_origin_airport, traj_destination_airport, traj_cruise_alt, traj_cruise_tas_knots)

    simulationInterface.startRealTime_singleUser()
    
    time_step = 1 # sec
    t = 0
    t_end = 500
    
    while (t < t_end):

	#Location of Data.txt within X-Plane directory, where the trajectory data is recorded by X-Plane.
        xPlaneDataFile = open("/home/xplane11/X-Plane 11/Data.txt")
        xPlaneData = list(csv.reader(xPlaneDataFile, delimiter='|'))
        currentState = xPlaneData[-1]

        while(len(currentState) != 32):
            currentState = depArrData[depArrData.index(currentState) - 1]

        traj_lat = float(currentState[-9])
        traj_lon = float(currentState[-8])
        traj_alt = float(currentState[-7])
        traj_rocd = float(currentState[15])/60
        traj_tas_knots = float(currentState[9])
        traj_tas_knots_ground = float(currentState[10])
        traj_course_deg = float(currentState[-11])
        traj_fpa_deg = 0.0
        traj_sector_index = 5
        traj_flight_phase = str(FLIGHT_PHASE_CRUISE)
        # Inject real-time trajectory state data
	t = int(round(time.time() * 1000))
        simulationInterface.externalAircraft_inject_trajectory_state_data(traj_ac_id, traj_lat, traj_lon, traj_alt, traj_rocd, traj_tas_knots, traj_tas_knots_ground, traj_course_deg, traj_fpa_deg, traj_sector_index, traj_flight_phase, t)
        t = t + time_step
        print "Sending trajectory data at t = ", t
        time.sleep(time_step)
    
    # Stop simulation
    simulationInterface.stop()
    
    # Use a while loop to constantly check server status.  When server simulation finishes, continue to output the trajectory data
    while True:
        server_runtime_sim_status = simulationInterface.get_runtime_sim_status()
        if (server_runtime_sim_status == NATS_SIMULATION_STATUS_ENDED) :
            break
        else:
            time.sleep(1)

    millis = int(round(time.time() * 1000))
    print "Outputting trajectory data.  Please wait...."
    # The trajectory output file will be saved on NATS_Server side
    simulationInterface.write_trajectories("Test_ExternalSimulator_" + str(millis) + ".csv")


    aircraftInterface.release_aircraft()
    environmentInterface.release_rap()

shutdownJVM()
