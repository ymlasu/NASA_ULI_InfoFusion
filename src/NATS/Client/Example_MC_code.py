'''
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Parikshit Dutta
Date: 2018-04-02
'''


import NATS_MonteCarlo_Interface as NATSMC
import PostProcessor as pp
import numpy as np

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

MC_interface = NATSMC.NATS_MonteCarlo_Interface(track_file = "share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx", \
                                                max_flt_lev_file= "share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx", \
                                                interval = 1);

'''The Flight plan for ULI13-2553603 from the TRX file 
share/tg/trx/TRX_07132005_noduplicates_cut_crypted_10Flights.trx
is used in this Monte Carlo simulation.'''
ac_list = ["SWA1897"];
    
'''Latitude location of the Aircraft at the start of the simulation to be perturbed.'''
# mean_lat = 38.0032615662;
# std_dev_lat = 0.01*np.abs(mean_lat)
# sample_sz_lat = 10;
# lat_vec = np.random.normal(mean_lat,std_dev_lat,sample_sz_lat)
# '''args = [ac_name, var_name, var_vals, fpindex (optional)]'''        
# args = [ac_list,args_dict[1],lat_vec]

'''Longitude location of the Aircraft at the start of the simulation to be perturbed.'''
# mean_lon = -117.770446777;
# std_dev_lon = 0.0001*np.abs(mean_lon);
# sample_sz_lon = 10;
# lon_vec = np.random.normal(mean_lon,std_dev_lon,sample_sz_lon)
# '''args = [ac_name, var_name, var_vals, fpindex (optional)]'''        
# args = [ac_list,args_dict[2],lon_vec]

'''Initial Altitude of the aircraft is not perturbed. But can be done similarly.'''  

'''Cruise Altitude to be perturbed.'''
# mean_alt = 33000;
# std_dev_alt = 0.05*mean_alt
# sample_sz_alt = 10;
# alt_vec = np.random.normal(mean_alt,std_dev_alt,sample_sz_alt)
# '''args = [ac_name, var_name, var_vals, fpindex (optional)]'''        
# args = [ac_list,args_dict[5],alt_vec]

'''Flight Plan Latitude to be perturbed.'''
# fpwpidx = 4;
# mean_lat = 37.14604949951172;
# std_dev_lat = 0.01*mean_lat;
# sample_sz_lat = 10;
# lat_vec = np.random.normal(mean_lat,std_dev_lat,sample_sz_lat)    
# '''args = [ac_name, var_name, var_vals, fpindex (optional)]'''        
# args = [ac_list,args_dict[6],lat_vec,fpwpidx]

'''Flight Plan Latitude and Longitude to be perturbed. 
Example illustrating perturbation of joint distribution variables.'''
# fpwpidx = 20;
# mean_lat = 40.2937660217;
# mean_lon = -87.557258606;
# std_dev_lat = 0.01*np.abs(mean_lat);
# std_dev_lon = 0.01*np.abs(mean_lon);
# mean = [mean_lat,mean_lon]
# cov = [[std_dev_lat**2, 0],[0,std_dev_lon**2]]
# sample_sz = 5;
# lat_vec,lon_vec = np.random.multivariate_normal(mean, cov, sample_sz).T
# fp_vec = []
# for i in range(sample_sz):
#     fp_vec.append([lat_vec[i],lon_vec[i]])
# '''args = [ac_name, var_name, var_vals, fpindex (optional)]'''        
# args = [ac_list,args_dict[8],fp_vec,fpindex]


'''Departure delay to be perturbed.'''
# mean_time = 60;
# std_dev_time = 0.5*mean_time
# sample_sz_time = 10;
# time_vec = np.random.randint(mean_time-std_dev_time,mean_time+std_dev_time,sample_sz_time)
# #Put Poisson if you know the arrival or departure rate at airport.  
# time_vec = np.random.poisson(mean_time,sample_sz_time)
# '''args = [ac_name, var_name, var_vals, fpindex (optional)]'''        
# args = [ac_list,args_dict[9],time_vec]

'''Rate of climb and descent to be perturbed'''
# mean_rocd = 13.6666669846
# std_dev_rocd = 0.1*np.abs(mean_rocd);
# sample_sz_rocd = 10;
# rocd_vec = np.random.normal(mean_rocd,std_dev_rocd,sample_sz_rocd)
# '''args = [ac_name, var_name, var_vals, fpindex (optional)]'''        
# args = [ac_list,args_dict[10],rocd_vec]


'''perturbing multiple aircrafts at a time.'''
# ac_list = ['ULI13-2553603','ULI3-33855','ULI18-9603'];
# var_name = [args_dict[2],args_dict[1],args_dict[3]];
# mean_1 = -117.770446777;
# std_dev_1 = 0.01*np.abs(mean_1);
# mean_2 = 35.0555992126;
# std_dev_2 = 0.01*np.abs(mean_2);
# mean_3 = 2200.0;
# std_dev_3 = 0.1*np.abs(mean_3);
# mean = [mean_1,mean_2,mean_3];
# cov = [[std_dev_1**2,0,0],[0,std_dev_2**2,0],[0,0,std_dev_3**2]];
# sample_sz = 50;
# vec_1,vec_2,vec_3 = np.random.multivariate_normal(mean, cov, sample_sz).T
# var_vec = []
# for i in range(sample_sz):
#     var_vec.append([vec_1[i],vec_2[i],vec_3[i]])    
# args = [ac_list,var_name,var_vec];


'''perturbing multiple variables of the same aircraft at a time.'''
ac_list = ['SWA1897'];
var_name = [args_dict[6],args_dict[7],args_dict[5]];
fpwidx = [4,4,-1];#Flight plan latitude, Flight plan longitude, cruise altitude
mean_1 = 37.14604949951172;
std_dev_1 = 0.01*np.abs(mean_1);
mean_2 = -121.94306182861328;
std_dev_2 = 0.01*np.abs(mean_2);
mean_3 = 33000;
std_dev_3 = 0.01*np.abs(mean_3);
mean = [mean_1,mean_2,mean_3];
cov = [[std_dev_1**2,0,0],[0,std_dev_2**2,0],[0,0,std_dev_3**2]];
sample_sz = 10;
vec_1,vec_2,vec_3 = np.random.multivariate_normal(mean, cov, sample_sz).T
var_vec = []
for i in range(sample_sz):
    var_vec.append([vec_1[i],vec_2[i],vec_3[i]])    
args = [ac_list,var_name,var_vec,fpwidx];

# ''' RUN MONTE CARLO'''
# MC_interface.runMCSims(args)
'''Post Processing and plotting the MC examples.'''
for ac in ac_list:
    post_process = pp.PostProcessor(file_path = "../NATS_Server_20180909_1532", \
                                    ac_name = ac);
#     post_process.plotRoutine();
    post_process.plotSingleAircraftTrajectory();
    
#     post_process.plotVariable('departure_delay')
