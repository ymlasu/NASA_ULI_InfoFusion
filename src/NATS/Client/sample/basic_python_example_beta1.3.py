'''
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Parikshit Dutta
Date: 2017-01-19
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


NATSClientFactory = JClass('NATSClientFactory')
natsClient = NATSClientFactory.getNATSClient()
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


sim.clear_trajectory()
environmentInterface.load_rap("share/tg/rap") # Here the parameters specify the file and path on server.  Please don't change it.
aircraftInterface.load_aircraft("share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx", "share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx") # Here the parameters specify the file and path on server.  Please don't change it.
# aircraftInterface.load_aircraft("share/tg/trx/GOOD_77rec_TRX_20180908.trx", "share/tg/trx/GOOD_77rec_MFL_20180908.trx") 
#------------PUT THE ABOVE IN EACH PROGRAM--------------------


'''EXPERIMENTATION BEGINS'''
# curr_ac = "SWA1897";
# curr_ac = "ULI-3AFAB4BC27";
# ac = aircraftInterface.select_aircraft(curr_ac);
# lats = ac.getFlight_plan_latitude_array();
# print 'Flight latitude',lats
# lons = ac.getFlight_plan_longitude_array();
# print 'Flight longitude',lons
# new_val = lats[0]+1;
# print 'value to be set',new_val
# ac.setFlight_plan_latitude_deg(1,new_val); 
# print ac.getFlight_plan_waypoint_name_array()
# ac = aircraftInterface.select_aircraft(curr_ac);
# print 'new latitude',ac.getFlight_plan_latitude_array()
#terminal area
# sids =  terminalAreaInterface.getAllApproaches("KATL")
# for s in sids:
#     print s
'''EXPERIMENTATION ENDS'''
    
    

sim.setupSimulation(11000, 10)

    
sim.start()
time.sleep(2)

#--------- PUT THE FOLLOWING IN EACH PROGRAM---------------------
while True:
    server_runtime_sim_status = sim.get_runtime_sim_status()
    if (server_runtime_sim_status == NATS_SIMULATION_STATUS_ENDED) :
        break
    else:
        time.sleep(1)
#-------PUT THE ABOVE IN EACH PROGRAM----------------
        
millis = int(round(time.time() * 1000))
print "Outputting trajectory data.  Please wait...."
# The trajectory output file will be saved on NATS_Server side
sim.write_trajectories("Sample_output_trajectory_" + str(millis) + ".csv")
    
aircraftInterface.release_aircraft()
environmentInterface.release_rap()

# Close connection from NATS Server
natsClient.disConnect()

shutdownJVM()
