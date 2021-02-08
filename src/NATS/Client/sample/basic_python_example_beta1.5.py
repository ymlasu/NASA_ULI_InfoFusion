'''
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Parikshit Dutta
Date: 2017-01-19
Update: 2019.06.19
'''

import sys
import os

curDir = os.path.dirname(os.path.abspath(__file__))

try:
    from jpype import *
except ImportError:
    pass
import time

sys.path.insert(0, curDir + '/DEMO_MC_Simulation')
from NATS_header import *

# Get NATSClient instance
NATSClientFactory = JClass('NATSClientFactory')
natsClient = NATSClientFactory.getNATSClient()

# Get SimulationInterface
sim = natsClient.getSimulationInterface();
# Get EquipmentInterface
equipmentInterface = natsClient.getEquipmentInterface();
# Get AircraftInterface
aircraftInterface = equipmentInterface.getAircraftInterface();

# Get EnvironmentInterface
environmentInterface = natsClient.getEnvironmentInterface();
# Get AirportInterface
airportInterface = environmentInterface.getAirportInterface()
# Get TerminalAreaInterface
terminalAreaInterface = environmentInterface.getTerminalAreaInterface()

# Login
natsClient.login("admin")

# Clear trajectory data
sim.clear_trajectory()

# Load wind data
environmentInterface.load_rap("share/tg/rap") # Here the parameters specify the file and path on server.  Please don't change it.

# Load aircraft data
aircraftInterface.load_aircraft("share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx", "share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx") # Here the parameters specify the file and path on server.  Please don't change it.
#------------PUT THE ABOVE IN EACH PROGRAM--------------------

    
# Set up simulation
# Set total simulation time to 11000 seconds, time step is 10 seconds
sim.setupSimulation(12000, 10)

# Start simulation
sim.start()

# --------- PUT THE FOLLOWING IN EACH PROGRAM ---------
# This while loop block is to check the simulation status.  Due to aircraft data size and different simulation time, there is no method to forsee how much time the simulation will take.  Therefore, we constantly check simulation status.  When the simulation status is ENDED, we can continue.
while True:
    server_runtime_sim_status = sim.get_runtime_sim_status()
    if (server_runtime_sim_status == NATS_SIMULATION_STATUS_ENDED) :
        break
    else:
        time.sleep(1)
# ------- PUT THE ABOVE IN EACH PROGRAM ---------

# Write trajectory result to a file
millis = int(round(time.time() * 1000))
print "Outputting trajectory data.  Please wait...."
# The trajectory output file will be saved on NATS_Server side
sim.write_trajectories("Sample_output_trajectory_" + str(millis) + ".csv")

# Release aircraft data
aircraftInterface.release_aircraft()

# Release wind data
environmentInterface.release_rap()

# Close connection from NATS Server
natsClient.disConnect()

# Shut down Java environment
shutdownJVM()
