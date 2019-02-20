'''
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Parikshit Dutta
Date: 2019-01-03
'''
from jpype import JClass,shutdownJVM
from NATS_header import NATS_SIMULATION_STATUS_ENDED
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
import numpy as np
import sys

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

'''This class provides an interface to the NATS simulation. 
Its starts the NATS client and establishes connection with the NATS server.
PLEASE MODIFY PATHS BEFORE DOING ANYTHING'''
class NATSInterface:
    def __init__(self, duration = 86400,
                 interval = 30, 
                 client_dir = './', 
                 wind_dir = 'share/tg/rap', 
                 track_file = "share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx", 
                 max_flt_lev_file = "share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx"):
        self.endTime = duration;
        self.interval = interval;
        self.initializeJVM(client_dir);
        self.wind_dir = wind_dir;
        self.trx_file = track_file;
        self.mfl_file = max_flt_lev_file;

    

    def initializeJVM(self, client_dir = './'):

        self.NATS_SIMULATION_STATUS_ENDED = NATS_SIMULATION_STATUS_ENDED;
        NATSClientFactory = JClass('NATSClientFactory')
        self.natsClient = NATSClientFactory.getNATSClient()
        
        self.equipmentInterface = self.natsClient.getEquipmentInterface();


        # Get EnvironmentInterface
        self.environmentInterface = self.natsClient.getEnvironmentInterface();
        # Get AirportInterface
        self.airportInterface = self.environmentInterface.getAirportInterface()
        # Get TerminalAreaInterface
        self.terminalAreaInterface = self.environmentInterface.getTerminalAreaInterface()
        
        self.sim = self.natsClient.getSimulationInterface()
                
        self.aircraftInterface = self.equipmentInterface.getAircraftInterface(); 
        
        
    def shutdownJVM(self):
        shutdownJVM()
    
    def getNATSClient(self):
        return self.natsClient;
    
    def getNATSEquipmentInterface(self):
        return self.equipmentInterface;
    
    def getNATSEnvironmentInterface(self):
        return self.environmentInterface;
    
    def getNATSAirportInterface(self):
        return self.airportInterface;
    
    def getNATSTerminalAreaInterface(self):
        return self.terminalAreaInterface;
    
    def getNATSSimulationInterface(self):
        return self.sim
    
    def getAircraftInterface(self):
        if self.aircraftInterface == None:
            self.aircraftInterface = self.equipmentInterface.getAircraftInterface(); 
        self.aircraftInterface.load_aircraft(self.trx_file,self.mfl_file)
        return self.aircraftInterface
    
    
    
'''This class in an interactive interface for procedure display and selection.'''   
class ProcedureDisplay(NATSInterface):
    def __init__(self):
        NATSInterface.__init__(self);    
        self.connecting_pt = ''
    
    '''This is the function being called for plotting all the procedures.
    :dep_surf_layout: departure airport surface layout
    :arv_surf_layout: arrival airport surface layout
    :center_handle: plot handle for CONUS centers.
    :airport: airport for procedure display
    :proctype: procedure type SID/STAR/APPROACH
    
    :return: chosen proctype by the user. 
    '''
    def plot_all_procs(self,dep_surf_layout, arv_surf_layout, \
                       center_handle,airport="KSFO",proctype="SID", \
                       connecting_pt = ''):
        self.airport = airport;
        self.proctype = proctype;
        if connecting_pt != '':
            self.connecting_pt = connecting_pt;
        if self.proctype == "SID":
            sids =  self.terminalAreaInterface.getAllSids(self.airport)
            
            if sids == None:
                print 'No ', self.proctype,'present for',self.airport;
                return "",[],[],[],[],[],"";                                         
 
            
            latvvv = [];lonvvv = []; wpvvv = [];sidnames = [];alt1vvv = [];alt2vvv=[];altdescvvv = [];
            for sid in sids:                             
                latvv,lonvv,wpvv,alt1vv,alt2vv,altdescvv = self.get_waypoint_lat_lon_vector(sid)
                latvvv.append(latvv); lonvvv.append(lonvv);wpvvv.append(wpvv);sidnames.append(sid);alt1vvv.append(alt1vv);alt2vvv.append(alt2vv);altdescvvv.append(altdescvv);                
            chosen_sid = self.plotProcs(latvvv,lonvvv,wpvvv,sidnames,center_handle,dep_surf_layout)
            chosen_sid = chosen_sid.upper()
            for sid in sids:            
                if (sid in chosen_sid) or (chosen_sid in sid):
                    chosen_sid = sid;
                    break;     
                
            leglat,leglon,legwp,legalt1,legalt2,legaltdesc = self.getProcLeg(chosen_sid,latvvv,lonvvv,wpvvv,alt1vvv,alt2vvv,altdescvvv,sidnames);
            return chosen_sid,leglat,leglon,legwp,legalt1,legalt2,legaltdesc;                                         
            
        elif self.proctype == "STAR":
            stars =  self.terminalAreaInterface.getAllStars(self.airport)
            if stars == None:
                print 'No ', self.proctype,'present for',self.airport;
                return "",[],[],[],[],[],"";
            
            latvvv = [];lonvvv = []; wpvvv = [];starnames = [];alt1vvv = [];alt2vvv=[];altdescvvv=[];
            for star in stars:                             
                latvv,lonvv,wpvv,alt1vv,alt2vv,altdescvv = self.get_waypoint_lat_lon_vector(star)
                latvvv.append(latvv); lonvvv.append(lonvv);wpvvv.append(wpvv);starnames.append(star);alt1vvv.append(alt1vv);alt2vvv.append(alt2vv);altdescvvv.append(altdescvv)                
            chosen_star = self.plotProcs(latvvv,lonvvv,wpvvv,starnames,center_handle,arv_surf_layout)
            chosen_star = chosen_star.upper()            
            for star in stars:            
                if (star in chosen_star) or (chosen_star in star):
                    chosen_star = star;
                    break;     
            leglat,leglon,legwp,legalt1,legalt2,legaltdesc = self.getProcLeg(chosen_star,latvvv,lonvvv,wpvvv,alt1vvv,alt2vvv,altdescvvv,starnames);
            return chosen_star,leglat,leglon,legwp,legalt1,legalt2,legaltdesc;
            
        elif self.proctype == "APPROACH":
            approaches =  self.terminalAreaInterface.getAllApproaches(self.airport)
            
            if approaches == None:
                print 'No ', self.proctype,'present for',self.airport;
                return "",[],[],[],[],[],"";
            latvvv = [];lonvvv = []; wpvvv = [];approachnames = [];alt1vvv = [];alt2vvv=[];altdescvvv = [];
            for approach in approaches:                             
                latvv,lonvv,wpvv,alt1vv,alt2vv,altdescvv = self.get_waypoint_lat_lon_vector(approach)
                latvvv.append(latvv); lonvvv.append(lonvv);wpvvv.append(wpvv);approachnames.append(approach);alt1vvv.append(alt1vv);alt2vvv.append(alt2vv),altdescvvv.append(altdescvv);                
            chosen_approach = self.plotProcs(latvvv,lonvvv,wpvvv,approachnames,center_handle,arv_surf_layout)
            chosen_approach = chosen_approach.upper()            
            for approach in approaches:            
                if (approach in chosen_approach) or (chosen_approach in approach):
                    chosen_approach = approach;
                    break;    
            leglat,leglon,legwp,legalt1,legalt2,legaltdesc = self.getProcLeg(chosen_approach,latvvv,lonvvv,wpvvv,alt1vvv,alt2vvv,altdescvvv,approachnames); 
            return chosen_approach,leglat,leglon,legwp,legalt1,legalt2,legaltdesc;
        
        
    '''Deprecated version of plot_all_procs. Use if you do not need interactive display.'''
    def plot_all_procs_non_interactive(self,dep_surf_layout, arv_surf_layout, center_handle,airport="KSFO",proctype="SID"):
        self.airport = airport;
        self.proctype = proctype;
        if self.proctype == "SID":
            sids =  self.terminalAreaInterface.getAllSids(self.airport)
    
            for sid in sids:                             
                '''BACKGROUND'''
                fig=plt.figure()
                fig.set_size_inches(9*12/7,9)
                ax=fig.add_axes([0.05,0.05,0.9,0.9])
                ax.set_facecolor('black')
                plt.title(sid)
                center_handle.plot_regions(plt,color='w')
                dep_surf_layout.plot_airport_layout(plt)
                '''BACKGROUND ENDS'''
                
                latvv,lonvv,wpvv = self.get_waypoint_lat_lon_vector(sid)
                for j in range(len(latvv)):
                    latv = latvv[j];lonv = lonvv[j];wpv = wpvv[j];        
                    plt.plot(lonv,latv,color = 'm')
#                     plt.hold(True)
                    for k in range(len(lonv)):
                        if k < len(lonv)-1:
                            plt.annotate('', xytext=(lonv[k], latv[k]), \
                                               xy=(lonv[k+1], latv[k+1]), \
                                               arrowprops=dict(arrowstyle="->", color='m'), \
                                               size=15);
                        plt.annotate(wpv[k],xy=(lonv[k],latv[k]), \
                                     xytext =(1.000001*lonv[k],1.000001*latv[k]), \
                                     color='m')
                    
            plt.draw()
            plt.pause(1);
            chosen_sid = raw_input("Please enter the chosen SID.")
            plt.close("all")
            
            
           
                    
            
            return chosen_sid;
            
            
                 
            
        elif self.proctype == "STAR":
            stars =  self.terminalAreaInterface.getAllStars(self.airport)
            for star in stars:
                '''BACKGROUND'''
                fig=plt.figure()
                fig.set_size_inches(9*12/7,9)
                ax=fig.add_axes([0.05,0.05,0.9,0.9])
                ax.set_facecolor('black')
                plt.title(star)
                center_handle.plot_regions(plt,color='w')
                arv_surf_layout.plot_airport_layout(plt)
                '''BACKGROUND ENDS'''
                
                latvv,lonvv,wpvv = self.get_waypoint_lat_lon_vector(star)
                for j in range(len(latvv)):
                    latv = latvv[j];lonv = lonvv[j];wpv = wpvv[j];        
                    plt.plot(lonv,latv,color = 'm')
#                     plt.hold(True)
                    for k in range(len(lonv)):
                        if k < len(lonv)-1:
                            plt.annotate('', xytext=(lonv[k], latv[k]), \
                                               xy=(lonv[k+1], latv[k+1]), \
                                               arrowprops=dict(arrowstyle="->", color='m'), \
                                               size=15);
                        plt.annotate(wpv[k],xy=(lonv[k],latv[k]), \
                                     xytext =(1.000001*lonv[k],1.000001*latv[k]), \
                                     color='m')
                    
            plt.draw()
            plt.pause(1);
            chosen_star = raw_input("Please enter the chosen STAR.")
            plt.close("all")
            
            return chosen_star;
            
        elif self.proctype == "APPROACH":
            approaches =  self.terminalAreaInterface.getAllApproaches(self.airport)
            for approach in approaches:
                '''BACKGROUND'''
                fig=plt.figure()
                fig.set_size_inches(9*12/7,9)
                ax=fig.add_axes([0.05,0.05,0.9,0.9])
                ax.set_facecolor('black')
                plt.title(approach)
                center_handle.plot_regions(plt,color='w')
                arv_surf_layout.plot_airport_layout(plt)
                '''BACKGROUND ENDS'''
                
                latvv,lonvv,wpvv = self.get_waypoint_lat_lon_vector(approach)
                for j in range(len(latvv)):
                    latv = latvv[j];lonv = lonvv[j];wpv = wpvv[j];                            
                    plt.plot(lonv,latv,color = 'm')
#                     plt.hold(True)
                    for k in range(len(lonv)):
                        if k < len(lonv)-1:
                            plt.annotate('', xytext=(lonv[k], latv[k]), \
                                               xy=(lonv[k+1], latv[k+1]), \
                                               arrowprops=dict(arrowstyle="->", color='m'), \
                                               size=15);
                        plt.annotate(wpv[k],xy=(lonv[k],latv[k]), \
                                     xytext =(1.000001*lonv[k],1.000001*latv[k]), \
                                     color='m')                    
                    
            plt.draw()
            plt.pause(1);
            chosen_approach = raw_input("Please enter the chosen Approach.")
            plt.close("all")
            
            return chosen_approach;
    
    '''This function takes in the procedure name and creates
    list of waypoints and legs corresponding to the procedure
    :procname: procedure name
    
    :return: vector of procedure legs containing waypoint information.'''
    
    
    def get_waypoint_lat_lon_vector(self,procname):
        
        latvv = [];lonvv=[];wpvv = [];alt1vv= [];alt2vv = [];altdescvv = [];
        leg_names = self.terminalAreaInterface.getProcedure_leg_names(self.proctype,procname,self.airport)
#         print 'Procname = ',procname
        for leg in leg_names:
#             print 'lEG NAME = ',leg
            legwp = self.terminalAreaInterface.getWaypoints_in_procedure_leg(self.proctype,procname,self.airport,leg)
            latv = [];lonv = [];    wpv = []; alt1v = []; alt2v=[];altdescv = [];
            for wp in legwp:
#                 print 'WPNAME = ',wp
                latlon = self.terminalAreaInterface.getWaypoint_Latitude_Longitude_deg(wp)
                alt1 = self.terminalAreaInterface.getProcedure_alt_1(self.proctype,procname,self.airport,leg,wp);
                alt2 = self.terminalAreaInterface.getProcedure_alt_2(self.proctype,procname,self.airport,leg,wp);
                altdesc = self.terminalAreaInterface.getProcedure_alt_desc(self.proctype,procname,self.airport,leg,wp);
                if latlon != None:
                    if latlon[0]!=0 and latlon[1]!=0:
#                         print 'LAT LON = ',latlon
                        latv.append(latlon[0]);lonv.append(latlon[1]);wpv.append(wp);alt1v.append(alt1);alt2v.append(alt2);altdescv.append(altdesc);
                    else:
                        latlon  = self.airportInterface.getLocation(wp);
                        if latlon != None:
                            if latlon[0]!=0 and latlon[1]!=0:
#                                 print 'LAT LON = ',latlon
                                latv.append(latlon[0]);lonv.append(latlon[1]);wpv.append(wp);alt1v.append(alt1);alt2v.append(alt2);altdescv.append(altdesc);
                            else:
                                wp = wp.replace('-NO_WP_NAME','')
#                                 print 'NEW WP = ',wp
                                latlon  = self.terminalAreaInterface.getWaypoint_Latitude_Longitude_deg(wp);
                                alt1 = self.terminalAreaInterface.getProcedure_alt_1(self.proctype,procname,self.airport,leg,wp);
                                alt2 = self.terminalAreaInterface.getProcedure_alt_2(self.proctype,procname,self.airport,leg,wp);
                                altdesc = self.terminalAreaInterface.getProcedure_alt_desc(self.proctype,procname,self.airport,leg,wp);
                                if latlon != None:
                                    if latlon[0]!=0 and latlon[1]!=0:
#                                         print 'LAT LON = ',latlon
                                        latv.append(latlon[0]);lonv.append(latlon[1]);wpv.append(wp);alt1v.append(alt1);alt2v.append(alt2);altdescv.append(altdesc);
                                
                else:
#                     print 'NONE TYPE = ',wp
                    wp = wp.replace('-NO_WP_NAME','')
#                     print 'NEW WP = ',wp
                    latlon  = self.terminalAreaInterface.getWaypoint_Latitude_Longitude_deg(wp);
                    alt1 = self.terminalAreaInterface.getProcedure_alt_1(self.proctype,procname,self.airport,leg,wp);
                    alt2 = self.terminalAreaInterface.getProcedure_alt_2(self.proctype,procname,self.airport,leg,wp);
                    altdesc = self.terminalAreaInterface.getProcedure_alt_desc(self.proctype,procname,self.airport,leg,wp);

                    if latlon != None:
                        if latlon[0]!=0 and latlon[1]!=0:
#                             print 'LAT LON = ',latlon
                            latv.append(latlon[0]);lonv.append(latlon[1]);wpv.append(wp);alt1v.append(alt1);alt2v.append(alt2);altdescv.append(altdesc);

            latvv.append(latv);lonvv.append(lonv);wpvv.append(wpv);alt1vv.append(alt1v);alt2vv.append(alt2v);altdescvv.append(altdescv);

        return latvv,lonvv,wpvv,alt1vv,alt2vv,altdescvv;
            
    '''This function plots the procedures as chosen by the user'''
    def plotProcs(self,latvvv,lonvvv,wpvvv,procnames,center_handle,ap_surf_layout):
        '''First write a code to pick annotations on double click'''
        
            
        '''BACKGROUND'''
        fig=plt.figure()
        ax=fig.add_axes([0.1,0.05,0.9,0.9])
        ax.set_facecolor('black')                
#         plt.title(proc)
        center_handle.plot_regions(plt,color='w')
        ap_surf_layout.plot_airport_layout(plt)
        '''BACKGROUND ENDS'''
        
        proclines = dict();procannos = dict();procarrows = dict();
        for i in range(len(latvvv)):            
            latvv = latvvv[i];lonvv = lonvvv[i];wpvv = wpvvv[i]; proc = procnames[i];
            procl = []; procann = [];procarr = [];

        
            for j in range(len(latvv)):
                latv = latvv[j];lonv = lonvv[j];wpv = wpvv[j];            
                lines, = plt.plot(lonv,latv,color = 'm',visible  = False)
                procl.append(lines)
                    
                
                for k in range(len(lonv)):
                    if k < len(lonv)-1:
                        arr = plt.annotate('', visible=False,xytext=(lonv[k], latv[k]), \
                                    xy=(lonv[k+1], latv[k+1]), \
                                    arrowprops=dict(arrowstyle="->", color='m'), \
                                    size=15);
                        procarr.append(arr);    
                    annos = plt.annotate(wpv[k],visible=False,xy=(lonv[k],latv[k]), \
                                xytext =(1.000001*lonv[k],1.000001*latv[k]), \
                                color='m')
                    
                    procann.append(annos);
            
            proclines[proc] = procl; procannos[proc] = procann;procarrows[proc] = procarr
        
        rax = plt.axes([0.01, 0.05, 0.07, 0.9])
        visibility = [False for proc in procnames]
        check = CheckButtons(rax, procnames,visibility)
        AllSelectedLabels = [];
        def func(label):
            procl = proclines[label];
            procann = procannos[label];
            procarr = procarrows[label];
            for arr in procarr:
                arr.set_visible(not arr.get_visible())
            for anno in procann:
                anno.set_visible(not anno.get_visible())
            for line in procl:
                line.set_visible(not line.get_visible())
            
            if label not in AllSelectedLabels:
                print(self.proctype + ' '+label+' is displayed in the figure.')
                AllSelectedLabels.append(label);
            else:
                print(self.proctype + ' '+label+ ' is removed from the figure.')
                AllSelectedLabels.remove(label)
            titlestring = 'Displayed '+ self.proctype + ' '
            for lab in AllSelectedLabels:
                titlestring = titlestring + lab+' ';
            if AllSelectedLabels == []:
                titlestring = 'None selected'
            ax.set_title(titlestring)
            plt.draw()
        

        
        check.on_clicked(func)                          
        
        plt.draw()
        plt.pause(1);
        chosen_proc = raw_input("Please enter the chosen "+ self.proctype+'.')   
        plt.close("all")
        return chosen_proc;
    
    
    '''Once the procedure is chosen, this function creates a possible set of 
    waypoints from start till the end of the procedure'''
    def getProcLeg(self,proc,latvvv,lonvvv,wpvvv,alt1vvv,alt2vvv,altdescvvv,sidnames):
        
        idx = sidnames.index(proc);
        
        if self.connecting_pt == '':
            return [],[],[],[],[],[];
        
        latlon = self.terminalAreaInterface.getWaypoint_Latitude_Longitude_deg(self.connecting_pt);
        if latlon != None:
            if latlon[0]!=0 and latlon[1]!=0:
                latc = latlon[0];lonc = latlon[1];
            else:
                print 'Lat lon of connection was not found'
                return [],[],[],[],[],[];
        else:
            print 'Lat lon of connection was not found'
            return [],[],[],[],[],[];
        
        
        if idx < 0:
            print 'No such SID:', proc
            quit();
        
        
        latvv = latvvv[idx];lonvv = lonvvv[idx]; wpvv = wpvvv[idx];alt1vv = alt1vvv[idx];alt2vv = alt2vvv[idx];altdescvv = altdescvvv[idx];
        lat_seq = [];lon_seq= [];wp_seq = [];alt1_seq=[];alt2_seq = [];altdesc_seq = [];
        '''Loop until you have reached the end of the procedure or the 
        last waypoint in the procedure has no other branch.'''
        while True:
            act_lat,act_lon,act_wp,act_alt1,act_alt2,act_altdesc = self.findLeg(latvv,lonvv,wpvv, \
                                                                    alt1vv,alt2vv,altdescvv,latc,lonc);
            if act_lat == None or act_lon == None or act_wp == None:
                break;
            if self.proctype == "SID":
                lat_seq.extend(reversed(act_lat));lon_seq.extend(reversed(act_lon));wp_seq.extend(reversed(act_wp));
                alt1_seq.extend(reversed(act_alt1));alt2_seq.extend(reversed(act_alt2));altdesc_seq.extend(reversed(act_altdesc));
            else:
                lat_seq.extend(act_lat);lon_seq.extend(act_lon);wp_seq.extend(act_wp);
                alt1_seq.extend(act_alt1);alt2_seq.extend(act_alt2);altdesc_seq.extend(act_altdesc);
                
                
            if self.proctype == "SID":
                latc = act_lat[0];lonc = act_lon[0];wp_now = act_wp[0];
            else:
                latc = act_lat[-1];lonc = act_lon[-1];wp_now = act_wp[-1];
            
                
            
            for latv,lonv,wpv,alt1v,alt2v,altdescv in zip(latvv,lonvv,wpvv,alt1vv,alt2vv,altdescvv):
                if self.proctype == "SID":
                    if wpv[0] == wp_now:
                        latvv.remove(latv); lonvv.remove(lonv);wpvv.remove(wpv);
                        alt1vv.remove(alt1v);alt2vv.remove(alt2v);altdescvv.remove(altdescv);                        
                else:
                    if wpv[-1] == wp_now:
                        latvv.remove(latv); lonvv.remove(lonv);wpvv.remove(wpv);
                        alt1vv.remove(alt1v);alt2vv.remove(alt2v);altdescvv.remove(altdescv);
                    
            
            found = False;
            for wpv in wpvv:
                for wp in wpv:
                    if wp == wp_now:
                        found = True
                        break;
            if not found:
                break;
            
            
 
        # order preserving
        u_lat=[];u_lon=[];u_wp = [];u_alt1 = [];u_alt2 = [];u_altdesc = [];
        for lat,lon,wp,alt1,alt2,altdesc in zip(lat_seq,lon_seq,wp_seq,alt1_seq,alt2_seq,altdesc_seq):
            if wp not in u_wp:
                u_lat.append(lat);u_lon.append(lon);u_wp.append(wp);u_alt1.append(alt1);u_alt2.append(alt2);u_altdesc.append(altdesc)
           
        return u_lat,u_lon,u_wp,u_alt1,u_alt2,u_altdesc;
        
    '''Find the leg that is nearest to the last waypoint in the previous 
    procedure''' 
    def findLeg(self,latvv,lonvv,wpvv,alt1vv,alt2vv,altdescvv,latc,lonc):
        act_lat = [];act_lon = []; act_wp = [];act_alt1 = []; act_alt2= [];act_altdesc = [];
        min_dist = sys.float_info.max;
        for latv,lonv,wpv,alt1v,alt2v,altdescv in zip(latvv,lonvv,wpvv,alt1vv,alt2vv,altdescvv):
            for lat,lon in zip(latv,lonv):
                distv = compute_distance_gc(lat, lon, latc, lonc, 0.0)
                if distv < min_dist:
                    min_dist = distv
                    act_lat = latv;
                    act_lon = lonv;
                    act_wp = wpv;
                    act_alt1 = alt1v;
                    act_alt2 = alt2v;
                    act_altdesc = altdescv;
        return act_lat,act_lon,act_wp,act_alt1,act_alt2,act_altdesc;
                
        
        
        
            
            
        
    
    
    