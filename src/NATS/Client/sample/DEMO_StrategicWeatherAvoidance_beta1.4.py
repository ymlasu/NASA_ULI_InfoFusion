# NATS sample
#
# Optimal Synthesis Inc.
#
# Oliver Chen
# 03.25.2019
#
# Demo of Strategic Weather Avoidance during simulation
#
# 1. The program will run two simulation(without and with strategic weather avoidance) and output a result trajectory file, respectively.
# 2. Finally, you can see the difference of the two trajectories in plotting.

from jpype import *
from array import *

import os
import time

from shutil import copyfile
from shutil import rmtree

import PostProcessor as pp

NATS_SERVER_DIR = "PLEASE_SPECIFY_PATH"

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
weatherInterface = environmentInterface.getWeatherInterface()

entityInterface = natsClient.getEntityInterface()
controllerInterface = entityInterface.getControllerInterface()
pilotInterface = entityInterface.getPilotInterface()

planned_dirname = ""
output_filename_before = ""
output_filename_after = ""

if not (os.path.isdir(NATS_SERVER_DIR)) :
    print "Directory NATS_SERVER_DIR does not exist"
else :
    natsClient.login("admin")

    if simulationInterface is None:
        print "Can't get SimulationInterface from server"
    
    else:
        # Download weather data files(not the severe traffic-blocking weather definition)
        # This function is only needed to be called when new weather files are required
        #weatherInterface.downloadWeatherFiles();
        
        simulationInterface.clear_trajectory()
        environmentInterface.load_rap("share/tg/rap")
    
        print ""
        print "************************************************"
        print "First simulation: No strategic weather avoidance"
        print "************************************************"
        print ""
    
        aircraftInterface.load_aircraft("share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx", "share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx")
    
        simulationInterface.setupSimulation(11000, 30) # SFO - PHX
        
        simulationInterface.start()
    
        while True:
            server_runtime_sim_status = simulationInterface.get_runtime_sim_status()
            if (server_runtime_sim_status == NATS_SIMULATION_STATUS_ENDED) :
                break
            else:
                time.sleep(1)
    
        millis = int(round(time.time() * 1000))
        print "Outputting trajectory data.  Please wait...."
        
        planned_dirname = os.path.splitext(os.path.basename(__file__))[0] + "_" + str(millis)
        output_filename_before = planned_dirname + ".csv"
    
        # The trajectory output file will be saved on NATS_Server side
        simulationInterface.write_trajectories(output_filename_before)
    
        aircraftInterface.release_aircraft()
    
        # =========================================================
        
        print ""
        print "*****************************************************"
        print "Second simulation: Enable strategic weather avoidance"
        print "*****************************************************"
        print ""
    
        simulationInterface.clear_trajectory()
    
        aircraftInterface.load_aircraft("share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx", "share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx")
    
        simulationInterface.setupSimulation(11000, 30) # SFO - PHX
        
        # Set polygon file for Strategic Weather Avoidance
        # Detail path and filename are required if you would like to use a specific file.  Example: share/rg/polygons/YYYYMMDD_HHMMSS.dat
        #
        # If inputing "", NATS engine will look for the latest file with name format YYYYMMDD_HHMMSS.dat
        #
        # Notice!!!!
        # If Sigmet file is used, polygon file will be ignored
        controllerInterface.setStrategicWeatherAvoidance_polygonFile("share/rg/polygons/MACS_scenario.dat")
        #controllerInterface.setStrategicWeatherAvoidance_polygonFile("") # NATS automatically pick latest file
        #controllerInterface.setStrategicWeatherAvoidance_polygonFile("NONE") # Disable file
    
    
        # Set sigmet file for Strategic Weather Avoidance
        # Detail path and filename are required if you would like to use a specific file.  Example: share/rg/polygons/YYYYMMDD_HHMMSS.dat
        #
        # If inputing "", NATS engine will look for the latest file with name format YYYYMMDD_HHMMSS.sigmet
        #
        # Notice!!!!
        # If Sigmet file is used, polygon file will be ignored
        #controllerInterface.setStrategicWeatherAvoidance_sigmetFile("") # NATS automatically pick latest file
        #controllerInterface.setStrategicWeatherAvoidance_sigmetFile("NONE") # Disable file
    
        # Enable strategic weather avoidance capability
        # This function must be called before setting up simulation so NATS Server can load required database files.
        controllerInterface.enableStrategicWeatherAvoidance(True)
        
        simulationInterface.start()
    #    simulationInterface.start(3610)
    
    #     while True:
    #         server_runtime_sim_status = simulationInterface.get_runtime_sim_status()
    #         if (server_runtime_sim_status == NATS_SIMULATION_STATUS_PAUSE) :
    #             break
    #         else:
    #             time.sleep(1)
    #     
    #     weatherInterface.enableStrategicWeatherAvoidance(False)
    #     
    #     simulationInterface.resume()
        
        while True:
            server_runtime_sim_status = simulationInterface.get_runtime_sim_status()
            if (server_runtime_sim_status == NATS_SIMULATION_STATUS_ENDED) :
                break
            else:
                time.sleep(1)
    
        millis = int(round(time.time() * 1000))
        print "Outputting trajectory data.  Please wait...."
        
        planned_dirname = os.path.splitext(os.path.basename(__file__))[0] + "_" + str(millis)
        output_filename_after = planned_dirname + ".csv"
    
        # The trajectory output file will be saved on NATS_Server side
        simulationInterface.write_trajectories(output_filename_after)
    
        aircraftInterface.release_aircraft()
    
    
        environmentInterface.release_rap()
    
    
    # =========================================================
    
    # The following statements read the result trajectory files and display plotting.
    # Notice!!!!
    # The following statements assume that NATS_Client and NATS_Server are installed on the same machine.
    # If NATS_Server is installed on another machine, the following Python codes will not work due to inability to access the server files.
    
    # Create temp directory on NATS_Server side and copy the result trajectory file into it
    planned_dirname = "tmp_" + planned_dirname
    os.makedirs(NATS_SERVER_DIR + "/" + planned_dirname)
    copyfile(NATS_SERVER_DIR + "/" + output_filename_before, NATS_SERVER_DIR + "/" + planned_dirname + "/" + output_filename_before)
    copyfile(NATS_SERVER_DIR + "/" + output_filename_after, NATS_SERVER_DIR + "/" + planned_dirname + "/" + output_filename_after)
    
    post_process = pp.PostProcessor(file_path = NATS_SERVER_DIR + "/" + planned_dirname,
                                    ac_name = 'SWA1897');
    post_process.plotSingleAircraftTrajectory();
    
    # Delete temp directory
    print "Deleting directory:", planned_dirname
    rmtree(NATS_SERVER_DIR + "/" + planned_dirname)
    
# Close connection from NATS Server
natsClient.disConnect()

shutdownJVM()
