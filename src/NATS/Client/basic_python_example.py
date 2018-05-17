'''
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Parikshit Dutta
Date: 2017-01-19
'''

try:
    from jpype import *
except ImportError:
    pass
import time
import os

def main():
    print()
    #------------PUT THE FOLLOWING IN EACH PROGRAM--------------------
    os.environ['NATS_CLIENT_HOME'] = "/home/hariiyer/SpringWorkspace/NASA_ULI_InfoFusion/src/NATS/Client/"
    classpath = "/home/hariiyer/SpringWorkspace/NASA_ULI_InfoFusion/src/NATS/Client/dist/nats-client.jar:/home/hariiyer/SpringWorkspace/NASA_ULI_InfoFusion/src/NATS/Client/dist/nats-shared.jar"
    
    startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % classpath)
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
    aircraftInterface.load_aircraft("share/tg/trx/TRX_07132005_noduplicates_cut_crypted_10Flights.trx", "share/tg/trx/TRX_07132005_noduplicatesOSIMaxFltLvl_cut_crypted_10Flights.trx") # Here the parameters specify the file and path on server.  Please don't change it.
    #------------PUT THE ABOVE IN EACH PROGRAM--------------------
    
    
    '''EXPERIMENTATION BEGINS'''
    # curr_ac = 'ULI13-2553603';
    # ac = aircraftInterface.select_aircraft(curr_ac);
    # lats = ac.getFlight_plan_latitude_array()
    # print 'Initial latitude',lats
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
        
        
    
    sim.setupSimulation(7200, 1) # We set 7200 seconds
    
        
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
    print("Outputting trajectory data.  Please wait....")
    # The trajectory output file will be saved on NATS_Server side
    sim.write_trajectories("Sample_output_trajectory_" + str(millis) + ".csv")
        
    aircraftInterface.release_aircraft()
    environmentInterface.release_rap()
    
    shutdownJVM()