from jpype import *
from array import *
from path import Path
import os
import time

def main():
    parentPath = str(Path(__file__).parent.parent.parent.parent)
    #------------PUT THE FOLLOWING IN EACH PROGRAM--------------------
    os.environ['NATS_CLIENT_HOME'] = str(parentPath) + "/src/NATS/Client/"
    classpath = str(parentPath) + "/src/NATS/Client/dist/nats-client.jar:" + str(parentPath) + "/src/NATS/Client/dist/nats-shared.jar"
    
    startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % classpath)
    
    # Flight mode value definition
    # You can detect and know the flight mode by checking its value
    FLIGHT_MODE_PREDEPARTURE = JPackage('com').osi.util.Constants.FLIGHT_MODE_PREDEPARTURE
    FLIGHT_MODE_CLIMB = JPackage('com').osi.util.Constants.FLIGHT_MODE_CLIMB
    FLIGHT_MODE_CRUISE = JPackage('com').osi.util.Constants.FLIGHT_MODE_CRUISE
    FLIGHT_MODE_DESCENT = JPackage('com').osi.util.Constants.FLIGHT_MODE_DESCENT
    FLIGHT_MODE_LANDED = JPackage('com').osi.util.Constants.FLIGHT_MODE_LANDED
    FLIGHT_MODE_HOLDING = JPackage('com').osi.util.Constants.FLIGHT_MODE_HOLDING
    
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
    
    i = 0
    j = 0
    
    if simulationInterface is None:
        print("Can't get SimInterface from server")
    
    else:
        simulationInterface.clear_trajectory()
        environmentInterface.load_rap("share/tg/rap")
        aircraftInterface.load_aircraft("share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx", "share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx")
    
        # Generate departing taxi plan using NATS shortest-path algorithm
        airportInterface.generate_surface_taxi_plan("SWA1897", "KSFO", "Gate_04_010", "Rwy_02_001", "Rwy_02_007", None)
    
        # Example: Define customized departing taxi route
        # Define user customized taxi route
        #user_defined_waypoint_ids_departing = ["Gate_07_005", "Ramp_07_006", "Txy_B_B5", "Txy_B_B2", "Txy_B_B1", "Txy_B_003", "Txy_B_K", "Txy_B_D", "Txy_E_B", "Txy_A_009", "Txy_A_F1", "Txy_A_M", "Txy_A_003", "Txy_A_002", "Txy_A_A1", "Txy_A_001", "Rwy_02_001", "Rwy_02_007"]
        # Set user-defined taxi plan
        #airportInterface.setUser_defined_surface_taxi_plan("SWA1897", "KSFO", user_defined_waypoint_ids_departing)
    
        # Generate landing taxi plan using NATS shortest-path algorithm
        airportInterface.generate_surface_taxi_plan("SWA1897", "KPHX", "Rwy_03_009", "Gate_10_006", None, "Rwy_03_001")
        
        # Example: Define customized landing taxi route
        # Define user customized taxi route
        #user_defined_waypoint_ids_landing = ["Rwy_03_001", "Rwy_03_009", "Txy_G7_001", "Txy_F_009", "Txy_F_010", "Txy_F_011", "Txy_F_012", "Txy_F11_001", "Rwy_02_015", "Rwy_02_017", "Txy_E12_001", "Txy_E_021", "Txy_E_022", "Txy_D13_001", "Ramp_10_005", "Ramp_10_006", "Gate_10_006"]
        # Set user-defined taxi plan
        #airportInterface.setUser_defined_surface_taxi_plan("SWA1897", "KPHX", user_defined_waypoint_ids_landing)
        
    #     # Show landing taxi plan
    #     landingTaxiPlan = airportInterface.getSurface_taxi_plan("SWA1897", "KPHX")
    #     if not(landingTaxiPlan is None) :
    #         for i in range(0, len(landingTaxiPlan)) :
    #             print "landingTaxiPlan waypoint id = ", landingTaxiPlan[i]
        
        simulationInterface.setupSimulation(7000, 1)
        simulationInterface.start()
      
        # Use a while loop to constantly check server status.  When server simulation finishes, continue to output the trajectory data
        while True:
            server_runtime_sim_status = simulationInterface.get_runtime_sim_status()
            if (server_runtime_sim_status == NATS_SIMULATION_STATUS_ENDED) :
                break
            else:
                time.sleep(1)
       
        millis = int(round(time.time() * 1000))
        print ("Outputting trajectory data.  Please wait....")
        # The trajectory output file will be saved on NATS_Server side
        simulationInterface.write_trajectories("DEMO_Gate_To_Gate_SFO_PHX_trajectory.csv")
        
        aircraftInterface.release_aircraft()
        environmentInterface.release_rap()
    
    shutdownJVM()