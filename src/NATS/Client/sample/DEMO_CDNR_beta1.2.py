# This program demonstrates Conflict Detection and Resolution during trajectory simulation


from jpype import *
from array import *

import os
import time
import PostProcessor as pp
import matplotlib.pyplot as plt
import copy
import numpy as np
RADIUS_EARTH_FT = 20925524.9;

def compute_distance_gc(lat1,lon1,lat2,lon2,alt):
    lat1_rad = lat1*np.pi/180.;
    lon1_rad = lon1*np.pi/180.;
    lat2_rad = lat2*np.pi/180.;
    lon2_rad = lon2*np.pi/180.;

    sin_half_dlat = np.sin( .5*(lat1_rad - lat2_rad) );
    sin_half_dlon = np.sin( .5*(lon1_rad - lon2_rad) );
    cos_lat1 = np.cos(lat1_rad);
    cos_lat2 = np.cos(lat2_rad);
    x = sin_half_dlat*sin_half_dlat + cos_lat1 * cos_lat2 * sin_half_dlon*sin_half_dlon;
    return 2*(RADIUS_EARTH_FT + alt)*np.arcsin(np.sqrt(x));

def post_process_CDNR():
    
    ac_list = ["SWA1897","SWA6516"];
    
    AllTrajs = {}
    for ac in ac_list:
        AllTrajs[ac] = [];
        
    for ac in ac_list:
        post_process = pp.PostProcessor(file_path = "../NATS_Server", \
                                    ac_name = ac);
#     post_process.plotRoutine();
#         post_process.plotSingleAircraftTrajectory();
        AllTrajs[ac].extend(post_process.LatLonAltSamp)
    
    nfiles = len(AllTrajs[ac_list[0]])
    fig,axs = plt.subplots(nrows =1, ncols = 1)
    lv = []
    for file in range(nfiles):
        traj1 = copy.deepcopy(AllTrajs[ac_list[0]][file])
        traj2 = copy.deepcopy(AllTrajs[ac_list[1]][file])
        
        if len(traj1) > len(traj2):
            
            ntime = len(traj2)
            T = []
            RD = []
            
            for k in range(ntime):
                val1 = [a for a in traj2[k]]
                idx = -1
                for j in range(len(traj1)):
                    if abs(traj1[j][0]-val1[0]) <1e-3:
                        idx = j
                        break;
                
                
                if idx >=0:
                    val2 = [a for a in traj1[idx]]
                    T.append(val2[0]);
                    reldist = compute_distance_gc(val1[1], val1[2], val2[1], val2[2], (val1[3]+val2[3])/2.)
                    RD.append(reldist)
                
            line, = axs.plot(T,RD,'-x')
            lv.append(line)
        else:
            
            ntime = len(traj1)
            T = []
            RD = []
            
            for k in range(ntime):
                val1 = [a for a in traj1[k]]
                idx = -1
                for j in range(len(traj2)):
                    if abs(traj2[j][0]-val1[0]) <1e-3:
                        idx = j
                        break;
                
                
                if idx >=0:
                    val2 = [a for a in traj2[idx]]
                    T.append(val2[0]);
                    reldist = compute_distance_gc(val1[1], val1[2], val2[1], val2[2], (val1[3]+val2[3])/2.)
                    RD.append(reldist)
                
            line, = axs.plot(T,RD,'-x')
            lv.append(line)
            
    
                    
    axs.set_xlabel('Time(s)');
    axs.set_ylabel('Relative distance between two aircraft (ft)')    
    axs.grid(True)
    #lh = axs.axhline(5*6076,ls = '--')
    fig.legend( (lv[0],lv[1]), ('w CDNR', 'w/o CDNR'),
                'upper center', ncol = 2)
    
    plt.show()    
        
     
        
        

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

# Aircraft clearance definition
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

NauticalMilestoFeet = 6076.12

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
    print "Can't get SimulationInterface from server"

else:
    
    CDNR_FLAG = [False,True]
     
    for flag in CDNR_FLAG:
        simulationInterface.clear_trajectory()
        environmentInterface.load_rap("share/tg/rap")
    
        aircraftInterface.load_aircraft("share/tg/trx/TRX_DEMO_CDNR.trx", "share/tg/trx/TRX_DEMO_CDNR_mfl.trx")

        simulationInterface.setupSimulation(36000, 30)

    # Set distance parameters of CDNR
    # These functions are optional.  The following values are default in NATS.
    # If users don't call these functions, NATS engine uses default values.
    #simulationInterface.setCDNR_distance_of_regard_ft_surface(600);
    #simulationInterface.setCDNR_distance_of_regard_ft_terminal(10 * NauticalMilestoFeet);
    #simulationInterface.setCDNR_distance_of_regard_ft_enroute(10 * NauticalMilestoFeet);
    #simulationInterface.setCDNR_distance_of_resolve_ft_surface(300);
    #simulationInterface.setCDNR_distance_of_resolve_ft_terminal(3 * NauticalMilestoFeet);
    #simulationInterface.setCDNR_distance_of_resolve_ft_enroute(5 * NauticalMilestoFeet);

    # Enable conflict detection and resolution
        simulationInterface.enableConflictDetectionAndResolution(flag);
    
        simulationInterface.start()

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
        simulationInterface.write_trajectories(os.path.splitext(os.path.basename(__file__))[0] + "_" + str(millis) + ".csv")

        aircraftInterface.release_aircraft()
        environmentInterface.release_rap()
    
    post_process_CDNR();

# Close connection from NATS Server
natsClient.disConnect()

shutdownJVM()