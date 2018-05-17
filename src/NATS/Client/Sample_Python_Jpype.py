# NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
# Copyright 2018 by Optimal Synthesis Inc. All rights reserved
#
# Author: Oliver Chen
# Date: 2018-03-23

from jpype import *

import os
import time

classpath = "dist/nats-client.jar:dist/nats-shared.jar"

startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % classpath)

# Flight mode value definition
# You can detect and know the flight mode by checking its value
FLIGHT_MODE_PREDEPARTURE = JPackage('com').osi.util.Constants.FLIGHT_MODE_PREDEPARTURE
FLIGHT_MODE_CLIMB = JPackage('com').osi.util.Constants.FLIGHT_MODE_CLIMB
FLIGHT_MODE_CRUISE = JPackage('com').osi.util.Constants.FLIGHT_MODE_CRUISE
FLIGHT_MODE_DESCENT = JPackage('com').osi.util.Constants.FLIGHT_MODE_DESCENT
FLIGHT_MODE_LANDED = JPackage('com').osi.util.Constants.FLIGHT_MODE_LANDED
FLIGHT_MODE_HOLDING = JPackage('com').osi.util.Constants.FLIGHT_MODE_HOLDING
FLIGHT_MODE_GROUND_DEPARTING = JPackage('com').osi.util.Constants.FLIGHT_MODE_GROUND_DEPARTING
FLIGHT_MODE_GROUND_LANDING = JPackage('com').osi.util.Constants.FLIGHT_MODE_GROUND_LANDING

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

i = 0

if sim is None:
    print "Can't get SimInterface from server"

else:
    sim.clear_trajectory()
    
    environmentInterface.load_rap("share/tg/rap") # Here the parameters specify the file and path on server.  Please don't change it.
    aircraftInterface.load_aircraft("share/tg/trx/TRX_07132005_noduplicates_cut_crypted.trx", "share/tg/trx/TRX_07132005_noduplicatesOSIMaxFltLvl_cut_crypted.trx") # Here the parameters specify the file and path on server.  Please don't change it.
    sim.setupSimulation(7200, 1) # We set 7200 seconds
    
    if not(aircraftInterface is None):
        # Obtain all aircraft ids
        allAircraftIdArray = aircraftInterface.getAllAircraftId()
        if (not(allAircraftIdArray is None) and (len(allAircraftIdArray) > 0)) :
            i = 0
            for i in range(0, len(allAircraftIdArray)):
                curAcId = allAircraftIdArray[i]
                print "Sample_Python --> allAircraftIdArray --> Aircraft Id = ", curAcId
    
    #sim.start()
    sim.start(600)
    time.sleep(2)
    #sim.pause()
    if not(aircraftInterface is None):
        server_runtime_sim_status = sim.get_runtime_sim_status();
        if ((server_runtime_sim_status != NATS_SIMULATION_STATUS_READY) and (server_runtime_sim_status != NATS_SIMULATION_STATUS_STOP)):
            # Collect qualified aircraft Id array by setting latitude, longitude and/or altitude parameters
            collectedAircraftIdArray = aircraftInterface.getAircraftIds(float(30.0), float(35.0), float(-115.0), float(-90.0), float(-1.0), float(-1.0))
            if (not(collectedAircraftIdArray is None) and (len(collectedAircraftIdArray) > 0)) :
                i = 0
                for i in range(0, len(collectedAircraftIdArray)):
                    curAcId = collectedAircraftIdArray[i]
                    print "Sample_Python --> Collected Aircraft Id = ", curAcId
        else:
            print "Sample_Python --> Server sim status not running"
        
        # Manually select an aircraft and modify value
        curAircraft = aircraftInterface.select_aircraft("ULI16-33855")
        if not(curAircraft is None):
            curAircraft.setAltitude_ft(float(36000.0))
                    
    time.sleep(2)
    #sim.resume()
    sim.resume(500)
    time.sleep(2)
    sim.resume() # Be sure to have a resume command to avoid infinite loop on NATS_Server
    # Use a while loop to constantly check server status.  When server simulation finishes, continue to output the trajectory data
    while True:
        server_runtime_sim_status = sim.get_runtime_sim_status()
        if (server_runtime_sim_status == NATS_SIMULATION_STATUS_ENDED) :
            break
        else:
            time.sleep(1)
    millis = int(round(time.time() * 1000))
    print "Outputting trajectory data.  Please wait...."
    # The trajectory output file will be saved on NATS_Server side
    sim.write_trajectories("output_trajectory_" + str(millis) + ".CSV")
    
    aircraftInterface.release_aircraft()
    environmentInterface.release_rap()

shutdownJVM()