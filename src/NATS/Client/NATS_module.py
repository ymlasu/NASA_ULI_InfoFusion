'''
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Parikshit Dutta
Date: 2018-04-02
'''
import sys
sys.path.append('/home/dyn.datasys.swri.edu/mhartnett/NASA_ULI/NASA_ULI_InfoFusion/src/NATS/Client/')

from NATS_header import NATS_Config, NATS_SIMULATION_STATUS_ENDED, NATS_SIMULATION_STATUS_PAUSE
from NATS_MonteCarlo_Interface import NATS_MonteCarlo_Interface
from sys import argv
import time
import numpy as np
import PostProcessor as pp
import centaur
import time
centaur.CentaurUtils.initialize_centaur()

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

    
def main(arg):
    mfl = '_'.join(arg[1].split('_')[:-1]) + '_mfl.trx'
    config = NATS_Config(track_file = "share/tg/trx/"+arg[1],
                         max_flt_lev_file = "share/tg/trx/"+mfl)
    MC_interface = NATS_MonteCarlo_Interface(config);
    
    curr_ac = "AC0001";
    
    '''Flight Plan Latitude'''
    fpwpidx = 1;
    uncertain_value = arg[2][0]
    print(uncertain_value)
    
    '''args = [ac_name, var_name, var_vals, fpindex (optional)]'''
        
    args = [[curr_ac],args_dict[6],uncertain_value,fpwpidx]
    filename = MC_interface.runMCSim(args)
    return filename

if __name__ == '__main__':
    main(argv)
