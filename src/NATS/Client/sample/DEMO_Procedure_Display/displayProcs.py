'''
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Parikshit Dutta
Date: 2018-04-02

THIS EXAMPLE SHOWS HOW TO CREATE FLIGHT PLANS FOR IMPLEMENTING IN NATS. 
AS AN EXAMPLE, WE HAVE SHOWN FLIGHT PLAN CREATION FROM KSFO-KPHX. 
'''

print('This file displays arrival and departure procedures. \nOrder of display: SID, STAR and Approach ')
print('Usage: python sample/DEMO_Procedure_Display/displayProcs.py KSFO')
print('Usage: python sample/DEMO_Procedure_Display/displayProcs.py KSFO KMSP')
import PlotHelpers as ph
import ProcedureDisplay as pd
import sys
import os


airport_list = []
if len(sys.argv) < 2:
    print 'Please input airport list'
    quit();
else:
    num_apts = len(sys.argv)
    
    for apt in sys.argv:
        if '.py' in apt:
            continue;
        else:
            airport_list.append(str(apt))

#a.include center
for dirpath, dirnames, filenames in os.walk("."):
    for f in filenames:
        if 'Centers_CONUS' in f:
            centerfile = os.path.join(dirpath, f)
            break;
   
'''DISPLAY PROCEDURE CLASS VARIABLE. PLEASE UPDATE PATHS HERE. ACCORDINGLY'''
for airport in airport_list:     
    proc_layout = pd.ProcedureDisplay()
    print 'airport = ', airport
 
    
    
    #in Default, include center boundaries
    center_handle = ph.RegionHandler()
    center_handle.read_region_file(centerfile,'CENTER')
      
  
    '''Departure airport surface layout details and handles'''
    __arpt_nodemap = proc_layout.airportInterface.getLayout_node_map(airport)
    __arpt_nodedata = proc_layout.airportInterface.getLayout_node_data(airport)
    __arpt_linkdata = proc_layout.airportInterface.getLayout_links(airport)
    __rwy_data=proc_layout.airportInterface.getAllRunways(airport)
    __surf_layout=ph.AirportLayout(airport)
    __surf_layout.initialize_from_NATS_airport_layout(__arpt_nodemap,__arpt_nodedata,__arpt_linkdata,__rwy_data)

    proc_layout.plot_all_procs(__surf_layout, __surf_layout, center_handle,airport,"SID")
    
    proc_layout.plot_all_procs(__surf_layout, __surf_layout, center_handle,airport,"STAR")
    
    proc_layout.plot_all_procs(__surf_layout, __surf_layout, center_handle,airport,"APPROACH")