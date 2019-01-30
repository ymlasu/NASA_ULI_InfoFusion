'''
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Parikshit Dutta
Date: 2018-04-02

THIS EXAMPLE SHOWS HOW TO CREATE FLIGHT PLANS FOR IMPLEMENTING IN NATS. 
AS AN EXAMPLE, WE HAVE SHOWN FLIGHT PLAN CREATION FROM KSFO-KPHX. 
@goto: LINE NUMBER 151 TO KNOW WHAT EACH FIELD IN A TRX ENTRY REPRESENT. 
       WITH THIS YOU CAN CREATE YOUR OWN TRX FILE. 
'''

print('This file helps create a flight plan that can be used as TRX file and MFL file.')
import PlotHelpers as ph
import ProcedureDisplay as pd
import numpy as np
import os

'''FIRST THE CONTINENTAL US CENTERS AND THE AIRPORT LAYOUTS ARE 
INPUTTED TO THE PLOT HANDLER. 
@DATAFILES: centerfile
MAKE SURE THAT THE PATHS TO DATAFILES ARE CORRECT!!!! IT WILL PRODUCE ERRORS OTHERWISE'''
 
 
'''DISPLAY PROCEDURE CLASS VARIABLE. PLEASE UPDATE PATHS HERE. ACCORDINGLY'''
proc_layout = pd.ProcedureDisplay()
proc_layout.trx_file = "share/tg/trx/TRX_DEMO_SFO_PHX.trx"
proc_layout.mfl_file = "share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx"

'''ORIGIN DESTINATION PAIR'''
origin = "KSFO"
dest = "KPHX"

#a.include center
#a.include center
for dirpath, dirnames, filenames in os.walk("."):
    for f in filenames:
        if 'Centers_CONUS' in f:
            centerfile = os.path.join(dirpath, f)
            break;
    #in Default, include center boundaries
center_handle = ph.RegionHandler()
center_handle.read_region_file(centerfile,'CENTER')
     
 
'''Departure airport surface layout details and handles'''
dep_arpt_nodemap = proc_layout.airportInterface.getLayout_node_map(origin)
dep_arpt_nodedata = proc_layout.airportInterface.getLayout_node_data(origin)
dep_arpt_linkdata = proc_layout.airportInterface.getLayout_links(origin)
dep_rwy_data=proc_layout.airportInterface.getAllRunways(origin)
dep_surf_layout=ph.AirportLayout(origin)
dep_surf_layout.initialize_from_NATS_airport_layout(dep_arpt_nodemap,dep_arpt_nodedata,dep_arpt_linkdata,dep_rwy_data)

'''Arrival airport surface layout details and handles'''
arv_arpt_nodemap=proc_layout.airportInterface.getLayout_node_map(dest)
arv_arpt_nodedata=proc_layout.airportInterface.getLayout_node_data(dest)
arv_arpt_linkdata=proc_layout.airportInterface.getLayout_links(dest)
arv_rwy_data=proc_layout.airportInterface.getAllRunways(dest)
arv_surf_layout=ph.AirportLayout(dest)
arv_surf_layout.initialize_from_NATS_airport_layout(arv_arpt_nodemap,arv_arpt_nodedata,arv_arpt_linkdata,arv_rwy_data)

'''WE WILL NOW CREATE SIDS AND STARS AND INPUT IT TO THE FLIGHT PLAN.'''

'''INITIAL SKELETON FLIGHT PLAN'''
initial_fp = 'SFO..LOSHN..BOILE..BLH..PHX'
# initial_fp = 'PHX..BLH..BOILE..LOSHN..SFO'
split_fp = initial_fp.split('..');
first_pt = split_fp[1];last_pt = split_fp[-2];
print 'Current flight plan is ', initial_fp

'''DISPLAY AND CHOOSE SID'''
raw_input('\nPress any key to display SIDS for '+origin);    
sid,sidlats,sidlons,sidwps,sidalt1s,sidalt2s,sidaltdescs = proc_layout.plot_all_procs(dep_surf_layout, arv_surf_layout, center_handle,origin,"SID",first_pt)
print 'Possible Waypoint Latitude and Longitude Sequence for SID ',sid,':'
print 'Waypoint|      Latitude|       Longitude|       Altitude1|       Altitude2|       Altitude Constraint Description|'
print '------------------------------------------------------------------------------------------------------------------'
for lat,lon,wp,alt1,alt2,altdesc in zip(sidlats,sidlons,sidwps,sidalt1s,sidalt2s,sidaltdescs):
    alt1str = alt1;
    if alt1 < 0:
        alt1str = 'NONE'
    alt2str = alt2;
    if alt2 < 0:
        alt2str = 'NONE'
    print wp,'     ',lat,'     ',lon,'     ',alt1str,'     ',alt2str,'            ',altdesc
    
    
'''INSERT SID'''
sid_string = '.'+sid+'.';
idx = initial_fp.find(origin)

if idx <0:
    idx = initial_fp.find(origin[1:])
    if idx < 0:
        print 'Origin not found'
        quit();
    else:
        idx = idx+3
    
else:
    idx = idx +4;
initial_fp = initial_fp[:idx]+sid_string+initial_fp[idx+2:]
print '\n\nCurrent flight plan is ', initial_fp


'''DISPLAY AND CHOOSE STAR'''
raw_input('\n\nPress any key to display STARs for '+dest);           
star,starlats,starlons,starwps,staralt1s,staralt2s,staraltdescs = proc_layout.plot_all_procs(dep_surf_layout, arv_surf_layout, center_handle,dest,"STAR",last_pt)
print 'Possible Waypoint Latitude and Longitude Sequence for STAR ',star,':'
print 'Waypoint|      Latitude|       Longitude|       Altitude1|       Altitude2|       Altitude Constraint Description|'
print '------------------------------------------------------------------------------------------------------------------'
for lat,lon,wp,alt1,alt2,altdesc in zip(starlats,starlons,starwps,staralt1s,staralt2s,staraltdescs):
    alt1str = alt1;
    if alt1 < 0:
        alt1str = 'NONE'
    alt2str = alt2;
    if alt2 < 0:
        alt2str = 'NONE'
    print wp,'     ',lat,'     ',lon,'     ',alt1str,'     ',alt2str,'            ',altdesc
    
    

'''LAST POINT OF STAR IS THE FIRST POINT OF APPROACH'''
first_approach_pt = starwps[-1];
'''DISPLAY AND CHOOSE APPROACH'''
raw_input('\n\nPress any key to display Approach Procedures for '+dest);
approach,approachlats,approachlons,approachwps,approachalt1s,approachalt2s,approachaltdescs = proc_layout.plot_all_procs(dep_surf_layout, arv_surf_layout, center_handle,dest,"APPROACH",first_approach_pt)
print 'Possible Waypoint Latitude and Longitude Sequence for APPROACH ',approach,':'
print 'Waypoint|      Latitude|       Longitude|       Altitude1|       Altitude2|       Altitude Constraint Description|'
print '------------------------------------------------------------------------------------------------------------------'
for lat,lon,wp,alt1,alt2,altdesc in zip(approachlats,approachlons,approachwps,approachalt1s,approachalt2s,approachaltdescs):
    alt1str = alt1;
    if alt1 < 0:
        alt1str = 'NONE'
    alt2str = alt2;
    if alt2 < 0:
        alt2str = 'NONE'
    print wp,'     ',lat,'     ',lon,'     ',alt1str,'     ',alt2str,'            ',altdesc
    
print '\n\n'

'''INSERT STAR AND APPROACH'''
arrival_str = '.'+star+'.'+approach+'.'
idx = initial_fp.find(dest)
if idx <0:
    idx = initial_fp.find(dest[1:])
    if idx < 0:
        print 'Destination not found'
        quit();

initial_fp = initial_fp[:idx-2]+arrival_str+initial_fp[idx:]

'''PRINT FINAL FP'''
print 'The final flight plan is ', initial_fp

raw_input('')

print '\n\n\n'

'''CREATE TRX FROM FP'''
print 'Now creating the TRX file'

'''FIRST LINE
@usage: This line gives you the UTC time at which the flight simulation in NATS starts.
        Not much to do here just input the current UTC time'''
import time
tracktime = np.floor(time.time())
first_line = 'TRACK_TIME '+ str(tracktime);
print 'The first line is:', first_line;

raw_input('Press key for creating second line\n\n');

'''SECOND LINE
@usage: This gives you details about aircraft and initial conditions for simulations.
        I will describe this field by field.
        
@field1: callsign of the aircraft
@field2: aircraft type
@field3: initial latitude in deg min sec (unsigned: assumes Northern Hemisphere) 
@field4: initial longitude in deg min sec (unsigned: assumed West of Prime Meridian
@field5: initial speed in knots
@field6: initial altitude in ft divided by 100.
@field7: initial heading in degrees
@field8: initial center ( can be obtained from FAA database). 
         But not to worry. Even if wrong center entered. NATS automatically corrects it
         based on initial position.
@field9: initial sector ( can be obtained from FAA database). 
         But not to worry. Even if wrong sector entered. NATS automatically corrects it
         based on initial position.'''
         
print 'creating second line:'
fltnum = 'SWA1897' 
print 'Flight Number: ', fltnum;
actype = 'B733'  
print 'AC type: ',actype;
# inilatlon =  '373638 1222286'#KSFO
inilatlon = '332603  1120041'#KPHX
print 'Initial lat lon in deg min,sec: ', inilatlon;
ini_speed = '130'
print 'Initial speed in knots: ',ini_speed;
# ini_alt = ' 0.114'#KSFO
ini_alt = ' 11.346'#KPHX
print 'Initial altitude in ft /100: ',ini_alt
ini_hdg = ' 280'
print 'Initial heading in deg: ', ini_hdg;
ini_center_sector =  'ZOA ZOA46'
print 'Initial center and sector: ',ini_center_sector;

second_line = 'TRACK '+ fltnum+ ' ' + actype + ' ' + inilatlon + ' ' + ini_speed + ' '+ini_alt \
              + ' ' + ini_hdg + ' ' + ini_center_sector

'''THIRD LINE
@usage: prints the entire flight plan string.'''            
third_line = '   FP_ROUTE '+ initial_fp;


raw_input('\n\nThe final TRX file')
print first_line
print second_line
print third_line 

TRXfile = 'PHX_SFO_DEMO.trx'
print 'Writing to TRX file ', TRXfile
fid = open(TRXfile,'w');
fid.write(first_line+'\n');
fid.write(second_line+'\n');
fid.write(third_line+'\n');
fid.close();

raw_input()

print '\n\nNow creating mfl file'

'''FIRST LINE
@usage: Explained below by fields: 
@field1: callsign 
@field2: maximum flight level that the flight achieves.
'''

max_flt_lev = '380'
print 'Max flight level of ',fltnum, ' is ', max_flt_lev;
mflline = fltnum+ ' '+ max_flt_lev
raw_input('the MFL file entry');
print mflline;

MFLfile = 'PHX_SFO_DEMO-mfl.trx'
print 'Writing to MFL file ', MFLfile
fid = open(MFLfile,'w');
fid.write(mflline);
fid.close();








 





