# NATS sample
#
# Optimal Synthesis Inc.
#
# Oliver Chen
# 06.26.2019
#
# Demo of changing aircraft state
#
# This program starts the simulation for a period of time then NATS pause automatically.
# When the simulation is at pause status, we change the aircraft state.
# When the simulation resumes, it continues to run the rest of the simulation until it finishes.
#
# Users can compare the trajectory data to see the change of aircraft state.

from jpype import *
from array import *

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

natsClient.login("admin")

if simulationInterface is None:
    print "Can't get SimulationInterface from server"

else:
    simulationInterface.clear_trajectory()
    environmentInterface.load_rap("share/tg/rap")
    
    aircraftInterface.load_aircraft("share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx", "share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx")
    
    simulationInterface.setupSimulation(11000, 30)

    simulationInterface.start(1020)
    
    # Check simulation status.  Continue to next code when it is at PAUSE status
    # !!!!
    #      Why we do this?
    #      NATS_Server and Client are running on different machines or system
    #      processes.
    #      The actuall execution time on NATS_Server is not predictable(could be fast or slow).
    #      The accurate way for NATS_Client to know the simulation status is to
    #      call simulationInterface.get_runtime_sim_status() and check its
    #      value.
    # !!!!
    while True:
        server_runtime_sim_status = simulationInterface.get_runtime_sim_status()
        if (server_runtime_sim_status == NATS_SIMULATION_STATUS_PAUSE) :
            break
        else:
            time.sleep(1)
    
    # =====================================================
    
    # Required
    # Every time at pause, get the latest aircraft data
    curAircraft = aircraftInterface.select_aircraft("SWA1897")
    if not (curAircraft is None):
        print "Setting new state to aircraft SWA1897"
        
        # Set new state value
        #curAircraft.setCruise_tas_knots(450)
        #curAircraft.setCruise_alt_ft(35000)
    
        curAircraft.setLatitude_deg(36.0)
        curAircraft.setLongitude_deg(-120.0)
    
    # =====================================================
    
    simulationInterface.resume(7110) # Resume and continue the simulation
    
    while True:
        server_runtime_sim_status = simulationInterface.get_runtime_sim_status()
        if (server_runtime_sim_status == NATS_SIMULATION_STATUS_PAUSE) :
            break
        else:
            time.sleep(1)
    
    # =====================================================
    
    # Required
    # Every time at pause, get the latest aircraft data
    curAircraft = aircraftInterface.select_aircraft("SWA1897")
    
    # Set new state value
    #curAircraft.setCruise_tas_knots(450)
    #curAircraft.setCruise_alt_ft(35000)
    
    curAircraft.setLatitude_deg(36.0)
    curAircraft.setLongitude_deg(-120.0)
    curAircraft.setAltitude_ft(32000.0)
    curAircraft.setTas_knots(400.0)
    curAircraft.setCourse_rad(110.0 * 3.1415926 / 180)
    curAircraft.setRocd_fps(50.0)
    
    # =====================================================
    
    simulationInterface.resume()
    
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
    simulationInterface.write_trajectories(os.path.splitext(os.path.basename(__file__))[0] + "_trajectory_" + str(millis) + ".csv")

    aircraftInterface.release_aircraft()
    environmentInterface.release_rap()


# Close connection from NATS Server
natsClient.disConnect()

shutdownJVM()
