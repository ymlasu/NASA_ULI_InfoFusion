'''
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Parikshit Dutta
Date: 2018-04-02
'''
import sys
sys.path.append('/home/dyn.datasys.swri.edu/mhartnett/NASA_ULI/NASA_ULI_InfoFusion/src/NATS/Client/')
import os

from jpype import JClass,shutdownJVM
import NATS_header
import time
import numpy as np
import PostProcessor as pp

'''This is the same arg_dict variable that is used in Example_MC_code.'''
args_dict = {1:'latitude', \
             2:'longitude', \
             3:'altitude', \
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
    def __init__(self,config):
        self.__dict__ = config.__dict__.copy()
        print(self.__dict__)
    
    '''This function sets the value the chosen random variable to 
    the prescribed value, before running simulation.'''
    def setValue(self, val, var_name,fpindex):        
        
        if var_name == 'latitude':
        
            self.ac.setLatitude_deg(val)                
    
            print('Starting simulation with latitude ', val, ' for ac ', self.ac.getAcid())
        
        elif var_name == 'longitude':
            
            self.ac.setLongitude_deg(val)                
    
            print('Starting simulation with longitude ', val, ' for ac ', self.ac.getAcid())
            
        elif var_name == 'altitude':
            
            self.ac.setAltitude_ft(val);
            
            print('Starting simulation with altitude ', val, ' for ac ', self.ac.getAcid())
        
        elif var_name == 'cruise_tas':
            
            self.ac.setCruise_tas_knots(val)
            
            print('Starting simulation with cruise tas ', val, ' for ac ', self.ac.getAcid())
            
        elif var_name == 'cruise_altitude':
            
            self.ac.setCruise_alt_ft(val)
            
            print('Starting simulation with cruise altitude ', val, ' for ac ', self.ac.getAcid())
            
        elif var_name == 'flight_plan_lat_deg':
            
            if fpindex >= 0:
                
                self.ac.setFlight_plan_latitude_deg(fpindex,val);
                
                print('Starting simulation with flight plan latitude  ', val, ' for index ', fpindex, ' for ac ', self.ac.getAcid())
        
        elif var_name == 'flight_plan_lon_deg':
            
            if fpindex >= 0:
                
                self.ac.setFlight_plan_longitude_deg(fpindex,val);
                
                print('Starting simulation with flight plan longitude  ', val, ' for index ', fpindex, ' for ac ', self.ac.getAcid())
        
        elif var_name == 'flight_plan_lat_lon_deg':
            
            if fpindex >= 0 and len(val) == 2:
                                
                self.ac.setFlight_plan_latitude_deg(fpindex,val[0]);

                self.ac.setFlight_plan_longitude_deg(fpindex,val[1]);
                
                print('Starting simulation with flight plan latitude,longitude  ', val, ' for index ', fpindex, ' for ac ', self.ac.getAcid())
                
        elif var_name == 'departure_delay':
            
            self.ac.delay_departure(val);
            
            print('Starting simulation with departude delay ', val)
        
        elif var_name == 'rate_of_climb_and_descent':
            
            self.ac.setRocd_fps(val);
            
            print('Starting simulation with rate of climb and descent (rocd) in fps ', val)


    '''This function gets the value the chosen random variable to 
    the prescribed value, before running simulation.'''
    def getValue(self, std_dev, sample_sz, var_name,fpindex):        
        
        if var_name == 'latitude':
        
            meanv = self.ac.getLatitude_deg()                
    
            var_samp = np.random.normal(meanv,std_dev,size = sample_sz)
            
            return var_samp
        
        elif var_name == 'longitude':
            
            meanv = self.ac.getLongitude_deg()                
    
            var_samp = np.random.normal(meanv,std_dev,size = sample_sz)
            
            return var_samp
            
        elif var_name == 'altitude':
            
            meanv = self.ac.getAltitude_ft();
            
            var_samp = np.random.normal(meanv,std_dev,size = sample_sz)
            
            return var_samp
        
        elif var_name == 'cruise_tas':
            
            meanv = self.ac.getCruise_tas_knots();
            
            var_samp = np.random.normal(meanv,std_dev,size = sample_sz)
            
            return var_samp
            
        elif var_name == 'cruise_altitude':
            
            meanv = self.ac.getCruise_alt_ft()
            
            var_samp = np.random.normal(meanv,std_dev,size = sample_sz)
            
            return var_samp
            
        elif var_name == 'flight_plan_lat_deg':
            
            if fpindex >= 0:
                
                meanv = self.ac.getFlight_plan_latitude_array()[fpindex];
                
                var_samp = np.random.normal(meanv,std_dev,size = sample_sz)
                
                return var_samp
        
        elif var_name == 'flight_plan_lon_deg':
            
            if fpindex >= 0:
                
                meanv = self.ac.getFlight_plan_longitude_array()[fpindex];
                
                var_samp = np.random.normal(meanv,std_dev,size = sample_sz)
                
                return var_samp
                    
     
        
        elif var_name == 'rate_of_climb_and_descent':
            
            meanv = self.ac.getRocd_fps();
            
            var_samp = np.random.normal(meanv,std_dev,size = sample_sz)
                
            return var_samp
        
        else:            
            
            raise ValueError('%s currently not implemented. Just generate samples on your own.\n',str(var_name))    
            
    
    def runMCSim(self,args):
        '''args = [ac_name, var_name, var_vals, index (optional)]'''
        if len(args) < 3 or len(args) > 4:
            print(' Incorrect args size. Please check')
            return 0;        
        ac_list = args[0];
        var_name = args[1];
        var = args[2];
        
        if len(args) == 4:
            fpwpidx = args[3];
        else:
            fpwpidx = [-1]*len(ac_list) ;
        
        print('Running simulation')
        self.sim.clear_trajectory()

    
        print('Loading wind and aircraft')
        #self.environmentInterface.load_rap(self.wind_dir) # Here the parameters specify the file and path on server.  Please don't change it.


        # Get AircraftInterface
        self.aircraftInterface = self.equipmentInterface.getAircraftInterface();    
        self.aircraftInterface.load_aircraft(self.trx_file,self.mfl_file)
        if self.aircraftInterface is None:
            print('Aircraft interface not found. Quitting...')
            quit();
                    
        if len(ac_list) == 1:
            curr_ac = ac_list[0]
            try:
                self.ac = self.aircraftInterface.select_aircraft(curr_ac);
            except ValueError:
                print('Cannot assign aircraft\n')

            if type(var_name) != list:
                self.setValue(var,var_name,fpwpidx)
            elif len(var_name) == 1:
                self.setValue(var,var_name[0],fpwpidx)
            else:
                assert len(var) == len(var_name) == len(fpwpidx)                    
                for vval,vname,fpidx in zip(var,var_name,fpwpidx):
                    print('at t=0s.')
                    self.setValue(vval,vname,fpidx)
            
        else:                
            for j in range(len(ac_list)):
                curr_ac = ac_list[j]
                try:
                    self.ac = self.aircraftInterface.select_aircraft(curr_ac);
                except ValueError:
                    print('Cannot assign aircraft\n')
   
                self.setValue(var[j],var_name[j],fpwpidx[j])
        

        self.sim.setupSimulation(self.endTime, self.interval);
        time.sleep(2);
        self.sim.start();

        '''This loop checks if the server is running.Leave it as it is.'''
        #---------PUT THE FOLLOWING IN EACH PROGRAM------------
        while True:
            server_runtime_sim_status = self.sim.get_runtime_sim_status()
            if (server_runtime_sim_status == self.NATS_header.NATS_SIMULATION_STATUS_ENDED) :
                break
            else:
                time.sleep(1)
        #---------PUT THE ABOVE IN EACH PROGRAM------------    
        print("Outputting trajectory data.  Please wait....")
        # The trajectory output file will be saved on NATS_Server side
#         self.sim.write_trajectories("output_trajectory_" + str(var) + "_" + curr_ac + ".csv")
        write_path = 'output_trajectory_'+str(time.time())+'_'+curr_ac+'.csv'
        self.sim.write_trajectories(write_path)

        time.sleep(2);

        print('Releasing previous data and clearing trajectories')
        self.aircraftInterface.release_aircraft()
        self.environmentInterface.release_rap()

        return write_path

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
            print(' Incorrect args size. Please check')
            return 0;        
        ac_list = args[0];
        var_name = args[1];
        var_vec = args[2];
        
        if len(args) == 4:
            fpwpidx = args[3];
        else:
            fpwpidx = [-1]*len(ac_list) ;
        
        k = 1;
        for var in var_vec:
            print('Running ',k,'th simulation')
            k = k+1;
            self.sim.clear_trajectory()

        
            print('Loading wind and aircraft')
            #self.environmentInterface.load_rap(self.wind_dir) # Here the parameters specify the file and path on server.  Please don't change it.
    
    
            # Get AircraftInterface
            self.aircraftInterface = self.equipmentInterface.getAircraftInterface();    
            self.aircraftInterface.load_aircraft(self.trx_file,self.mfl_file)
            if self.aircraftInterface is None:
                print('Aircraft interface not found. Quitting...')
                quit();
                        
            if len(ac_list) == 1:
                curr_ac = ac_list[0]
                try:
                    self.ac = self.aircraftInterface.select_aircraft(curr_ac);
                except ValueError:
                    print('Cannot assign aircraft\n')
    
                if type(var_name) != list:
                    self.setValue(var,var_name,fpwpidx)
                elif len(var_name) == 1:
                    self.setValue(var,var_name[0],fpwpidx)
                else:
                    assert len(var) == len(var_name) == len(fpwpidx)                    
                    for vval,vname,fpidx in zip(var,var_name,fpwpidx):
                        print('at t=0s.')
                        self.setValue(vval,vname,fpidx)
                
            else:                
                for j in range(len(ac_list)):
                    curr_ac = ac_list[j]
                    try:
                        self.ac = self.aircraftInterface.select_aircraft(curr_ac);
                    except ValueError:
                        print('Cannot assign aircraft\n')
       
                    self.setValue(var[j],var_name[j],fpwpidx[j])
            

            self.sim.setupSimulation(self.endTime, self.interval);
            time.sleep(2);
            self.sim.start();
    
            '''This loop checks if the server is running.Leave it as it is.'''
            #---------PUT THE FOLLOWING IN EACH PROGRAM------------
            while True:
                server_runtime_sim_status = self.sim.get_runtime_sim_status()
                if (server_runtime_sim_status == self.NATS_header.NATS_SIMULATION_STATUS_ENDED) :
                    break
                else:
                    time.sleep(1)
            #---------PUT THE ABOVE IN EACH PROGRAM------------    
            print("Outputting trajectory data.  Please wait....")
            # The trajectory output file will be saved on NATS_Server side
#             self.sim.write_trajectories("output_trajectory_" + str(var) + "_" + curr_ac + ".csv")
            self.sim.write_trajectories("output_trajectory_" + str(k) + "_" + curr_ac + ".csv")
    
            time.sleep(2);
    
            print('Releasing previous data and clearing trajectories')
            self.aircraftInterface.release_aircraft()
            self.environmentInterface.release_rap()
    
    
    def runMCSimWithPause(self,args):
        self.sim.clear_trajectory()

        #self.environmentInterface.load_rap("share/tg/rap")
    
        self.aircraftInterface.load_aircraft(self.trx_file,self.mfl_file)
    
        # Controller to set human error: delay time
        # Users can try the following setting and see the difference in trajectory
        delays = [NATS_header.AIRCRAFT_CLEARANCE_PUSHBACK, NATS_header.AIRCRAFT_CLEARANCE_TAXI_DEPARTING, 
          NATS_header.AIRCRAFT_CLEARANCE_TAKEOFF, NATS_header.AIRCRAFT_CLEARANCE_ENTER_ARTC, 
          NATS_header.AIRCRAFT_CLEARANCE_DESCENT_FROM_CRUISE, NATS_header.AIRCRAFT_CLEARANCE_ENTER_TRACON,
          NATS_header.AIRCRAFT_CLEARANCE_APPROACH, NATS_header.AIRCRAFT_CLEARANCE_TOUCHDOWN, 
          NATS_header.AIRCRAFT_CLEARANCE_TAXI_LANDING, NATS_header.AIRCRAFT_CLEARANCE_RAMP_LANDING]
        for ac in self.aircraftInterface.getAllAircraftId():
            print('Changing controllerInterface parameters for {}'.format(ac))
            for i,d in enumerate(delays):
                print('Setting {} to {}'.format(d,args[0][i]))
                self.controllerInterface.setDelayPeriod(ac, d, int(np.round(args[0][i])))
    
        self.sim.setupSimulation(self.endTime,self.interval) # SFO - PHX
        time.sleep(5)
        self.sim.start()
    
        # Use a while loop to constantly check simulation status.  When the simulation finishes, continue to output the trajectory data
        '''
        while self.sim.get_runtime_sim_status() != NATS_header.NATS_SIMULATION_STATUS_PAUSE:
            time.sleep(1)
            print('1st status: ',self.sim.get_runtime_sim_status())
    
        # Pilot to set error scenarios
        # Users can try the following setting and see the difference in trajectory
        for ac in self.aircraftInterface.getAllAircraftId():
            print('Changing pilotInterface parameters for {}'.format(ac))
            self.pilotInterface.setActionLag(ac, 'COURSE', 10, 0.0, 60)
            self.pilotInterface.setActionLag(ac, 'ALTITUDE', 10, 0.0, 60)
            self.pilotInterface.setActionLag(ac, 'VERTICAL_SPEED', 10, 0.0, 60)
        '''
        #self.sim.resume()
        
        while True:
            x = self.sim.get_runtime_sim_status()
            print('status: ', x,'time: ', self.sim.get_curr_sim_time())
            if x == NATS_header.NATS_SIMULATION_STATUS_ENDED:
                break
            else:
                time.sleep(1)
        
        millis = int(round(time.time() * 1000)) 
        print("Outputting trajectory data.  Please wait....")
    
        planned_dirname = os.path.splitext(os.path.basename(__file__))[0] + "_" + str(millis)
        output_filename = planned_dirname + ".csv"
    
        # Output the trajectory result file
        self.sim.write_trajectories(output_filename)
    
        self.aircraftInterface.release_aircraft()
        self.environmentInterface.release_rap()

        # =========================================================
        
        # The following statements read the result trajectory files and display plotting.
        
        # Create temp directory and copy the result trajectory file into it
        planned_dirname = "tmp_" + planned_dirname
        os.makedirs(planned_dirname)
        
        return output_filename

        local_trajectory_filename = output_filename
        
        copyfile(local_trajectory_filename, planned_dirname + "/" + local_trajectory_filename)
        
        post_process = pp.PostProcessor(file_path = planned_dirname,
                                        ac_name = 'SWA1897');
        
        post_process.plotSingleAircraftTrajectory();
        
        # Delete temp directory
        print("Deleting directory:", planned_dirname)
        rmtree(planned_dirname)
    
    '''This is the main file being called. args are 
    
    :ac_name: The callsign of the aircraft being experimented,
    :time_pause: time at which simulation paused, 
    :var_name: random variable perturbed. Please refer to args_dict for proper naming convention, 
    :var_vals: The array/matrix of the perturbed values, 
    :index (optional): This is an optional argument used for perturbing the flight plan. 
                      refers to the flight plan index being perturbed
    :std_dev (optional): This is an optional argument used when you do not have the var_vals. 
                         This is an array of std deviations. 
    :sample_size (optional): Number of samples to be generated.                 
                      
    :outputs: None
    
    '''
    
    def runMCSimsWithPause(self,args):
        '''args = [ac_name, 
                    time_pause,
                    var_name, 
                    var_vals, 
                    index (optional),
                    std_dev (optional), 
                    sample_size (optional)]'''
        if len(args) < 3 or len(args) > 7:
            print(' Incorrect args size. Please check')
            return 0;        
        
        ac_list = args[0];
        time_pause = args[1];
        var_name = args[2];
        try:
            assert len(ac_list) == len(time_pause) == len(var_name)
        except AssertionError:
            ac_list = ac_list*len(time_pause)
        
        if len(args) >= 4:
            var_vec = args[3];
        else:
            var_vec = [[]] ;
        
        if len(args) >= 5:
            fpwpidx = args[4];
            if fpwpidx == []:
                fpwpidx = [-1]*len(ac_list) ;
        else:
            fpwpidx = [-1]*len(ac_list) ;
            
        
        if len(args) >= 6:
            try:
                assert len(args) == 7;
            except AssertionError:
                print('Have to give me sample size.')
                raise                        
            stddev = args[5];
            try: 
                assert len(stddev) == len(ac_list)
            except AssertionError:
                stddev = [0.1]*len(ac_list)
            
            sample_sz = args[6];                    
        else:
            stddev = [0.1]*len(ac_list)
            sample_sz = 10;
        
        idx_pause = (np.argsort(time_pause)).tolist()
        
        '''First simulate and populate the var_vec if its empty'''
        
        if var_vec == [[]]:            
            print('Generate samples by first running the simulation and getting value.')
            
            self.sim.clear_trajectory()
            
            print('Loading wind and aircraft')
            #self.environmentInterface.load_rap(self.wind_dir)
            
            self.aircraftInterface = self.equipmentInterface.getAircraftInterface();    
            self.aircraftInterface.load_aircraft(self.trx_file,self.mfl_file)
            if self.aircraftInterface is None:
                print('Aircraft interface not found. Quitting...')
                quit();
            
            all_var_vals = [[]]*len(ac_list)
            
            self.sim.setupSimulation(self.endTime, self.interval);
            time.sleep(2);
            self.sim.start(time_pause[idx_pause[0]]);
                
            #---------WAIT FOR PAUSE------------
            while True:
                server_runtime_sim_status = self.sim.get_runtime_sim_status()
                if (server_runtime_sim_status == NATS_header.NATS_SIMULATION_STATUS_PAUSE) :
                    break
                else:
                    time.sleep(1)
                
            self.ac = self.aircraftInterface.select_aircraft(ac_list[idx_pause[0]]);
            
            var_vals = self.getValue(stddev[idx_pause[0]],sample_sz, \
                                     var_name[idx_pause[0]],fpwpidx[idx_pause[0]]);
            all_var_vals[idx_pause[0]] = var_vals
            if len(idx_pause) > 1:                    
                for j in range(1,len(idx_pause)):

                    time_to_run = time_pause[idx_pause[j]]-time_pause[idx_pause[j-1]];
                    self.sim.resume(time_to_run);
                        
                    while True:
                        server_runtime_sim_status = self.sim.get_runtime_sim_status()
                        if (server_runtime_sim_status == NATS_header.NATS_SIMULATION_STATUS_PAUSE) :
                            break
                        else:
                            time.sleep(1) 
                    time.sleep(2);                                 
                    self.ac = self.aircraftInterface.select_aircraft(ac_list[idx_pause[0]]);
            
                    var_vals = self.getValue(stddev[idx_pause[j]],sample_sz, \
                                     var_name[idx_pause[j]],fpwpidx[idx_pause[j]]);
                    all_var_vals[idx_pause[j]] = var_vals
                    
                    time.sleep(2);
                    if j == len(idx_pause)-1:
                        break;
            self.sim.resume()
                    
            #---------PUT THE FOLLOWING IN EACH PROGRAM------------
            while True:
                server_runtime_sim_status = self.sim.get_runtime_sim_status()
                if (server_runtime_sim_status == self.NATS_header.NATS_SIMULATION_STATUS_ENDED) :
                    break
                else:
                    time.sleep(1)                                    
                
            #---------PUT THE ABOVE IN EACH PROGRAM------------    
            #NO TRAJECTORY OUTPUTTING
                
            time.sleep(2);
    
            print('Releasing previous data and clearing trajectories')
            self.aircraftInterface.release_aircraft()
            self.environmentInterface.release_rap()            
            
            '''Populate var_vec'''                        
            var_vec = [];
            for j in range(sample_sz):
                var_samp = [];
                for i in range(len(ac_list)):
                    var_samp.append(all_var_vals[i][j])
                var_vec.append(var_samp);
                
        k = 1;
           
        for var in var_vec:
            print('Running ',k,'th simulation'            )
            self.sim.clear_trajectory()
            
            print('Loading wind and aircraft')
            #self.environmentInterface.load_rap(self.wind_dir) # Here the parameters specify the file and path on server.  Please don't change it.
    
            # Get AircraftInterface
            self.aircraftInterface = self.equipmentInterface.getAircraftInterface();    
            self.aircraftInterface.load_aircraft(self.trx_file,self.mfl_file)
            if self.aircraftInterface is None:
                print('Aircraft interface not found. Quitting...')
                quit();                                            
                
                
            self.sim.setupSimulation(self.endTime, self.interval);
            time.sleep(2);
            self.sim.start(time_pause[idx_pause[0]]);
                
            #---------WAIT FOR PAUSE------------
            while True:
                server_runtime_sim_status = self.sim.get_runtime_sim_status()
                if (server_runtime_sim_status == NATS_header.NATS_SIMULATION_STATUS_PAUSE) :
                    break
                else:
                    time.sleep(1)
            time.sleep(2)
            self.ac = self.aircraftInterface.select_aircraft(ac_list[idx_pause[0]]);            
            self.setValue(var[idx_pause[0]],var_name[idx_pause[0]],fpwpidx[idx_pause[0]]);
            time.sleep(2);
                
            if len(idx_pause) > 1:                    
                for j in range(1,len(idx_pause)):

                    time_to_run = time_pause[idx_pause[j]]-time_pause[idx_pause[j-1]];
                    self.sim.resume(time_to_run);
                        
                    while True:
                        server_runtime_sim_status = self.sim.get_runtime_sim_status()
                        if (server_runtime_sim_status == NATS_header.NATS_SIMULATION_STATUS_PAUSE) :
                            break
                        else:
                            time.sleep(1)
                    time.sleep(2);        
                    v_name = var_name[idx_pause[j]];
                    v_val = var[idx_pause[j]];
                    fpid = fpwpidx[idx_pause[j]];
                    self.ac = self.aircraftInterface.select_aircraft(ac_list[idx_pause[j]]);
                    self.setValue(v_val,v_name,fpid);
                    time.sleep(2);
                    if j == len(idx_pause)-1:
                        break;
                    
            self.sim.resume()
                    
            #---------PUT THE FOLLOWING IN EACH PROGRAM------------
            while True:
                server_runtime_sim_status = self.sim.get_runtime_sim_status()
                if (server_runtime_sim_status == self.NATS_header.NATS_SIMULATION_STATUS_ENDED) :
                    break
                else:
                    time.sleep(1)
                
                    
                
            #---------PUT THE ABOVE IN EACH PROGRAM------------    
            print("Outputting trajectory data.  Please wait....")
            # The trajectory output file will be saved on NATS_Server side
            #             self.sim.write_trajectories("output_trajectory_" + str(var) + "_" + curr_ac + ".csv")
            self.sim.write_trajectories("output_trajectory_" + str(k) + ".csv")
                
            time.sleep(2);
    
            print('Releasing previous data and clearing trajectories')
            self.aircraftInterface.release_aircraft()
            self.environmentInterface.release_rap()

            k = k+1;  
                
    
    '''This is the main MC manager. 
    
    @1: If the arguments are         
        args = [ac_name, var_name, var_vals, index (optional)] 
        the you are perturbing the variables initially. 
        It will default to runMCSims(self.args).
    @2: If the arguments are:
        args = [ac_name,time_pause,var_name,var_vals (optional), index (optional)].
        It will then run runMCSimsWithPause(self,args)
        
    :Important: Notice the subtle change here second argument is not a 
                string. 
    
    '''
    def MCManager(self,args):
                        
        if len(args) == 7 or len(args) == 5:
            self.runMCSimsWithPause(args);
        elif len(args) == 3 or len(args) == 4:
            checker_arg = args[1];
            if type(checker_arg) != list:
                if isinstance(checker_arg, basestring):
                    self.runMCSims(args);
                else:
                    self.runMCSimsWithPause(args);
            else:
                if isinstance(checker_arg[0], basestring):
                    self.runMCSims(args);
                else:
                    self.runMCSimsWithPause(args);
        else:
            print('Wrong number of arguments please refer to the usage.')
    




if __name__ == '__main__':
    
    MC_interface = NATS_MonteCarlo_Interface();
    
    curr_ac = "AC0001";
    
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
    
    post_process = pp.PostProcessor(file_path = "../Server/", \
                 ac_name = curr_ac);
    
    post_process.plotRoutine();
    
    
