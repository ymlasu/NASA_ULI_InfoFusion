'''
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Parikshit Dutta
Date: 2018-04-02
'''

from jpype import startJVM,getDefaultJVMPath,JPackage,JClass,shutdownJVM
from NATS_header import NATS_SIMULATION_STATUS_ENDED   
import time
import numpy as np

import PostProcessor as pp

'''This is the same arg_dict variable that is used in Example_MC_code.'''
args_dict = {1:'initial_latitude', \
             2:'initial_longitude', \
             3:'initial_altitude', \
             4:'cruise_tas', \
             5:'cruise_altitude', \
             6:'flight_plan_lat_deg', \
             7:'flight_plan_lon_deg', \
             8:'flight_plan_lat_lon_deg', \
             9:'departure_delay', \
             10:'rate_of_climb_and_descent'}


'''This class initializes the NATS client, accepts MC samples as inputs,
runs the NATS simulation and produces .csv output.'''
class NATS_MonteCarlo_Interface:
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

    '''Initialize the NATS client'''    
    def initializeJVM(self, client_dir):

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
    
    
    
    '''This function sets the value the chosen random variable to 
    the prescribed value, before running simulation.'''
    def setValue(self, val, var_name,fpindex):        
        
        if var_name == 'initial_latitude':
        
            self.ac.setLatitude_deg(val)                
    
            print 'Starting simulation with initial latitude ', val, ' for ac ', self.ac.getAcid();
        
        elif var_name == 'initial_longitude':
            
            self.ac.setLongitude_deg(val)                
    
            print 'Starting simulation with initial longitude ', val, ' for ac ', self.ac.getAcid();
            
        elif var_name == 'initial_altitude':
            
            self.ac.setAltitude_ft(val);
            
            print 'Starting simulation with initial altitude ', val, ' for ac ', self.ac.getAcid();
        
        elif var_name == 'cruise_tas':
            
            self.ac.setCruise_tas_knots(val)
            
            print 'Starting simulation with cruise tas ', val, ' for ac ', self.ac.getAcid();
            
        elif var_name == 'cruise_altitude':
            
            self.ac.setCruise_alt_ft(val)
            
            print 'Starting simulation with cruise altitude ', val, ' for ac ', self.ac.getAcid();
            
        elif var_name == 'flight_plan_lat_deg':
            
            if fpindex >= 0:
                
                self.ac.setFlight_plan_latitude_deg(fpindex,val);
                
                print 'Starting simulation with flight plan latitude  ', val, ' for index ', fpindex, ' for ac ', self.ac.getAcid();
        
        elif var_name == 'flight_plan_lon_deg':
            
            if fpindex >= 0:
                
                self.ac.setFlight_plan_longitude_deg(fpindex,val);
                
                print 'Starting simulation with flight plan longitude  ', val, ' for index ', fpindex, ' for ac ', self.ac.getAcid();
        
        elif var_name == 'flight_plan_lat_lon_deg':
            
            if fpindex >= 0 and len(val) == 2:
                
                
                self.ac.setFlight_plan_latitude_deg(fpindex,val[0]);
                
               
                
                self.ac.setFlight_plan_longitude_deg(fpindex,val[1]);
                
                print 'Starting simulation with flight plan latitude,longitude  ', val, ' for index ', fpindex, ' for ac ', self.ac.getAcid();
                
        elif var_name == 'departure_delay':
            
            self.ac.delay_departure(val);
            
            print 'Starting simulation with departude delay ', val;
        
        elif var_name == 'rate_of_climb_and_descent':
            
            self.ac.setRocd_fps(val);
            
            print 'Starting simulation with rate of climb and descent (rocd) in fps ', val;
        
            
    '''This is the main file being called. args are 
    
    :ac_name: The callsign of the aircraft being experimented, 
    :var_name: random variable perturbed. Please refer to args_dict for proper naming convention, 
    :var_vals: The array/matrix of the perturbed values, 
    :index (optional): This is an optional argument used for perturbing the flight plan. 
                      refers to the flight plan index being perturbed
                      
                      
    :outputs: None
    
    '''
    def runMCSims(self,args):
        '''args = [ac_name, var_name, var_vals, index (optional)]'''
        if len(args) < 3 or len(args) > 4:
            print ' Incorrect args size. Please check';
            return 0;        
        ac_list = args[0];
        var_name = args[1];
        var_vec = args[2];
        
        if len(args) == 4:
            fpwpidx = args[3];
        else:
            fpwpidx = [1]*len(ac_list) ;
        
        k = 1;
        for var in var_vec:
            print 'Running ',k,'th simulation'
            k = k+1;
            self.sim.clear_trajectory()

        
            print 'Loading wind and aircraft'
            self.environmentInterface.load_rap(self.wind_dir) # Here the parameters specify the file and path on server.  Please don't change it.
    
    
            # Get AircraftInterface
            self.aircraftInterface = self.equipmentInterface.getAircraftInterface();    
            self.aircraftInterface.load_aircraft(self.trx_file,self.mfl_file)
            if self.aircraftInterface is None:
                print 'Aircraft interface not found. Quitting...';
                quit();
            if len(ac_list) == 1:
                curr_ac = ac_list[0]
                try:
                    self.ac = self.aircraftInterface.select_aircraft(curr_ac);
                except ValueError:
                    print 'Cannot assign aircraft\n'
    
   
                if len(var_name) == 1:
                    self.setValue(var,var_name,fpwpidx)
                else:
                    assert len(var) == len(var_name) == len(fpwpidx)                    
                    for vval,vname,fpidx in zip(var,var_name,fpwpidx):
                        self.setValue(vval,vname,fpidx)
                    
                
                
            else:
                
    
                for j in range(len(ac_list)):
                    curr_ac = ac_list[j]
                    try:
                        self.ac = self.aircraftInterface.select_aircraft(curr_ac);
                    except ValueError:
                        print 'Cannot assign aircraft\n'
       
                    self.setValue(var[j],var_name[j],fpwpidx[j])
            

            self.sim.setupSimulation(self.endTime, self.interval);
            time.sleep(2);
            self.sim.start();
    
            '''This loop checks if the server is running.Leave it as it is.'''
            #---------PUT THE FOLLOWING IN EACH PROGRAM------------
            while True:
                server_runtime_sim_status = self.sim.get_runtime_sim_status()
                if (server_runtime_sim_status == self.NATS_SIMULATION_STATUS_ENDED) :
                    break
                else:
                    time.sleep(1)
            #---------PUT THE ABOVE IN EACH PROGRAM------------    
            print "Outputting trajectory data.  Please wait...."
            # The trajectory output file will be saved on NATS_Server side
#             self.sim.write_trajectories("output_trajectory_" + str(var) + "_" + curr_ac + ".csv")
            self.sim.write_trajectories("output_trajectory_" + str(k) + "_" + curr_ac + ".csv")
    
            time.sleep(2);
    
            print 'Releasing previous data and clearing trajectories'
            self.aircraftInterface.release_aircraft()
            self.environmentInterface.release_rap()
    
    

    




if __name__ == '__main__':
    
    MC_interface = NATS_MonteCarlo_Interface();
    
    curr_ac = "SWA1897";
    
    '''Flight Plan Latitude'''
    fpwpidx = 6;
    mean_lat = 40.995819091796875;
    std_dev_lat = 0.01*mean_lat;
    sample_sz_lat = 5;
    k=0;
    lat_vec = np.random.normal(mean_lat,std_dev_lat,sample_sz_lat)
    
    '''args = [ac_name, var_name, var_vals, fpindex (optional)]'''
        
    args = [[curr_ac],args_dict[6],lat_vec,fpwpidx]
    MC_interface.runMCSims(args)
    
    post_process = pp.PostProcessor(file_path = "../NATS_Server_20180903_2037", \
                 ac_name = curr_ac);
    
    post_process.plotRoutine();
    
    
