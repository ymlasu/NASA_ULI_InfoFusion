# NATS sample
#
# Optimal Synthesis Inc.
#
# Oliver Chen
# 03.25.2019
#
# Demo of Conflict Detection and Resolution during trajectory simulation
#
# This program run simulation twice to generate two different trajectory results -- without-CDNR and with-CDNR.  Finally, users can compare the difference between them.

from jpype import *
from array import *

import os
import time
import PostProcessor as pp

import copy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

from shutil import copyfile
from shutil import rmtree

RADIUS_EARTH_FT = 20925524.9;

NATS_SERVER_HOME = 'PLEASE_ENTER_NATS_SERVER_LOCATION_HERE'

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

def post_process_CDNR(dirPath):
    
    ac_list = ["SWA1897","SWA6516"];
    
    AllTrajs = {}
    for ac in ac_list:
        AllTrajs[ac] = [];
        
    for ac in ac_list:
#        post_process = pp.PostProcessor(file_path = "../NATS_Server", \
 #                                   ac_name = ac);
        post_process = pp.PostProcessor(file_path = dirPath, \
                            ac_name = ac);
#     post_process.plotRoutine();
#         post_process.plotSingleAircraftTrajectory();
        AllTrajs[ac].extend(post_process.LatLonAltSamp)
    
    nfiles = len(AllTrajs[ac_list[0]])
    fig,axs = plt.subplots(nrows =2, ncols = 1)
    lv = []
    AllLon = []; AllLat = []; AllT = [];
    for file in range(nfiles):
        traj1 = copy.deepcopy(AllTrajs[ac_list[0]][file])
        traj2 = copy.deepcopy(AllTrajs[ac_list[1]][file])
        
        if len(traj1) > len(traj2):
            
            ntime = len(traj2)
            T = []
            RD = []
            Lat =[]
            Lon = []
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
                    Lat.append([val1[1],val2[1]])
                    Lon.append([val1[2],val2[2]])
                
            line, = axs[0].plot(T,RD,'-x')
            lv.append(line)
            Lat = np.array(Lat)
            Lon = np.array(Lon)
            
            axs[1].plot(Lon[:,1],Lat[:,1],'--r')
            axs[1].plot(Lon[:,0],Lat[:,0],'--b')
            
            AllLat.append(Lat); AllLon.append(Lon); AllT.append(T)
            
        else:
            
            ntime = len(traj1)
            T = []
            RD = []
            Lat =[]
            Lon = []
                        
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
                    Lat.append([val1[1],val2[1]])
                    Lon.append([val1[2],val2[2]])
                
            line, = axs.plot(T,RD,'-x')
            lv.append(line)
            
            Lat = np.array(Lat)
            Lon = np.array(Lon)
            
            axs[1].plot(Lon[:,1],Lat[:,1],'--r')
            axs[1].plot(Lon[:,0],Lat[:,0],'--b')
            
            AllLat.append(Lat); AllLon.append(Lon); AllT.append(T)
    
    axs[0].set_xlabel('Time(s)');
    axs[0].set_ylabel('Relative distance between two aircraft (ft)')    
    axs[0].grid(True)
    
    axs[0].set_xlabel('Longitude (deg)');
    axs[0].set_ylabel('Latitude (deg)')    
    axs[0].grid(True)
    lh = axs[0].axhline(5*6076,ls = '--')
#     fig.legend( (lv[0],lv[1],lh), ('w CDNR', 'w/o CDNR','resolution threshold'),
#                 'upper center', ncol = 3)
    
#     plt.show()    

    try:
        assert len(AllLat) == len(AllLon) == len(AllT) == 2
    except AssertionError:
        print('Please remove the *.csv files in the server folder')
        raise
    
    
    frame_num = len(AllT[0])
    minlon = min( np.min(AllLon[0]),np.min(AllLon[1]))
    maxlon = max( np.max(AllLon[0]),np.max(AllLon[1]))
    
    minlat = min( np.min(AllLat[0]),np.min(AllLat[1]))
    maxlat = max( np.max(AllLat[0]),np.max(AllLat[1]))
    
    fig = plt.figure()
    ax = plt.axes(xlim=(minlon,maxlon), 
                  ylim=(minlat,maxlat)
                  )
    line11, = ax.plot([], [], linestyle = '--', color = 'r', marker = 'x', linewidth = 2)
    line12, = ax.plot([], [], linestyle = '--', color = 'g', marker = 'o', linewidth = 2)
    line21, = ax.plot([], [], linestyle = '--', color = 'k', marker = 'd', linewidth = 2)
    line22, = ax.plot([], [], linestyle = '--', color = 'b', marker = '+', linewidth = 2)
 
    lines = [line11,line12,line21,line22]
     
    def init():
        for line in lines:
            line.set_data([],[])
        return lines
     
    def animate(i):
         
        xlist = [AllLon[0][:i,0], AllLon[0][:i,1],AllLon[1][:i,0], AllLon[1][:i,1]]
        ylist = [AllLat[0][:i,0], AllLat[0][:i,1],AllLat[1][:i,0], AllLat[1][:i,1]]
         
        for lnum,line in enumerate(lines):
            line.set_data(xlist[lnum], ylist[lnum]) # set data for each line separately. 
 
        return lines
     
     
     
    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=frame_num, interval=10, blit=True)
 
 
    plt.show()
        
        

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

natsClient.login("admin")

if simulationInterface is None:
    print "Can't get SimulationInterface from server"

else:
    output_dirname = "" # Reset
    orig_filename = "" # Reset
    
    CDNR_FLAG = [False,True]
     
    for flag in CDNR_FLAG:
        simulationInterface.clear_trajectory()
        environmentInterface.load_rap("share/tg/rap")
    
        aircraftInterface.load_aircraft("share/tg/trx/TRX_DEMO_CDNR.trx", "share/tg/trx/TRX_DEMO_CDNR_mfl.trx")

        simulationInterface.setupSimulation(36000, 30)

        # Set distance parameters of CDNR
        # These functions are optional.  The following values are default in NATS.
        # If users don't call these functions, NATS engine uses default values.
        #controllerInterface.setCDR_initiation_distance_ft_surface(600);
        #controllerInterface.setCDR_initiation_distance_ft_terminal(20 * NauticalMilestoFeet);
        #controllerInterface.setCDR_initiation_distance_ft_enroute(20 * NauticalMilestoFeet);
        #controllerInterface.setCDR_separation_distance_ft_surface(300);
        #controllerInterface.setCDR_separation_distance_ft_terminal(7 * NauticalMilestoFeet);
        #controllerInterface.setCDR_separation_distance_ft_enroute(10 * NauticalMilestoFeet);

        # Enable conflict detection and resolution
        controllerInterface.enableConflictDetectionAndResolution(flag);
    
        simulationInterface.start()

        # Use a while loop to constantly check server status.  When server simulation finishes, continue to output the trajectory data
        while True:
            server_runtime_sim_status = simulationInterface.get_runtime_sim_status()
            if (server_runtime_sim_status == NATS_SIMULATION_STATUS_ENDED) :
                break
            else:
                time.sleep(1)
     
        millis = int(round(time.time() * 1000))
        
        if output_dirname == "":
            # Notice!!!!
            # The following statements assume that NATS_Client and NATS_Server are installed on the same machine.
            # If NATS_Server is installed on another machine, the following Python codes will not work due to inability to access the server files.
            output_dirname = os.path.splitext(os.path.basename(__file__))[0] + "_" + str(millis)
            orig_filename = output_dirname
            output_dirname = "tmp_" + output_dirname
            os.makedirs(NATS_SERVER_HOME + "/" + output_dirname)
        
        if flag:
            output_filename = orig_filename + "_CDNR.csv";
        else:
            output_filename = orig_filename + "_noCDNR.csv";
            
        print "Outputting trajectory data.  Please wait...."
        # The trajectory output file will be saved on NATS_Server side
        simulationInterface.write_trajectories(output_filename)

        aircraftInterface.release_aircraft()
        environmentInterface.release_rap()
        
        # Copy trajectory file to a temp directory
        copyfile(NATS_SERVER_HOME + "/" + output_filename, NATS_SERVER_HOME + "/" + output_dirname + "/" + output_filename)


# Close connection from NATS Server
natsClient.disConnect()

# Notice!!!!
# The following statements assume that NATS_Client and NATS_Server are installed on the same machine.
# If NATS_Server is installed on another machine, the following Python codes will not work due to inability to access the server files.
post_process_CDNR(NATS_SERVER_HOME + "/" + output_dirname);

# Delete temp directory
print "Deleting directory:", output_dirname
rmtree(NATS_SERVER_HOME + "/" + output_dirname)

shutdownJVM()
