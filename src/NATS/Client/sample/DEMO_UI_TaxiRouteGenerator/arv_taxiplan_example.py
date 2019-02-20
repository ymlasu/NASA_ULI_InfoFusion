#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This example illustrates how to use NATS functions of airport interfaces.

Author: Jun Yang
Date: 03/29/2018
"""

import jpype as jp
import PlotHelpers as ph
import matplotlib.pyplot as plt
import os

#Preamble. Modify the client directory
#a directory where NATS_Client jar files are located.
#client_dir='/home/jun/optisyn/p1703-Demo/0329/NATS_Client_20180329/'
client_dir='PLEASE_ENTER_PATH_TO_NATS_CLIENT_HERE'
classpath =client_dir+"dist/nats-client.jar"+":"+client_dir+"dist/nats-shared.jar"

#b directory in which Center and Sector data are located
data_dir = './data'


#Start JVM and obtain NATS client
#----------------------------------------------------------------------------------------
jp.startJVM(jp.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % classpath)
NATSClientFactory = jp.JClass('NATSClientFactory')
natsClient = NATSClientFactory.getNATSClient()

#----------------------------------------------------------------------------------------------
# TaxiPlan for the arrival airport
#
# Step 1. From aircraftInterface load TRX file and select an aircraft.
equipmentInterface=natsClient.getEquipmentInterface()
ac_if = equipmentInterface.getAircraftInterface()  # aircraft interface
if (not (ac_if)):
    print("cannot get AircraftInterface from NATS server")
ac_if.load_aircraft("share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx", "share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx")
ac_names=ac_if.getAllAircraftId()
print("acs:{} are loaded".format(ac_names))

#select the first aircraft
ac_instance=ac_if.select_aircraft(ac_names[0])
ac_flightid=ac_instance.getAcid()

#Obtain the airport for the above aircraft
environmentInterface = natsClient.getEnvironmentInterface()
airportInterface=environmentInterface.getAirportInterface()

#step 3. For departure, load the designed route at KSFO
dep_arpt_name=airportInterface.getDepartureAirport(ac_names[0])
dep_arpt_nodemap = airportInterface.getLayout_node_map(dep_arpt_name)
dep_arpt_nodedata = airportInterface.getLayout_node_data(dep_arpt_name)
dep_arpt_linkdata = airportInterface.getLayout_links(dep_arpt_name)
dep_rwy_data=airportInterface.getAllRunways(dep_arpt_name)
dep_arpt_surf=ph.AirportLayout(dep_arpt_name)
dep_arpt_surf.initialize_from_NATS_airport_layout(dep_arpt_nodemap,dep_arpt_nodedata,dep_arpt_linkdata,dep_rwy_data)

dep_taxi_plan=ph.TaxiPlan(dep_arpt_surf)
dep_taxi_plan_file='KSFO_dep_designed_taxi_route.csv'
dep_taxi_plan.read_csv_route(dep_taxi_plan_file)
dep_node_name_sequence=dep_taxi_plan.get_node_names()
print(" Deparrure: user designed routes:{}".format(dep_node_name_sequence))

#assign the user defined taxiroute as the taxi plan
airportInterface.setUser_defined_surface_taxi_plan(ac_flightid,dep_arpt_name,dep_node_name_sequence)
#confirm
rtn_dep_plan_str=airportInterface.getSurface_taxi_plan(ac_flightid,dep_arpt_name)
print("AC:{} departure plan:{} is confirmed".format(ac_flightid,rtn_dep_plan_str))

#For arrival.

arv_arpt_name=airportInterface.getArrivalAirport(ac_names[0])
print(" AC:{} arrives at {}".format(ac_instance.getAcid(),arv_arpt_name))
arv_arpt_instance=airportInterface.select_airport(arv_arpt_name)
#Step 2. obtain airport layout data and load it
#Read the airport layout for the above aircraft
arv_arpt_nodemap=None;arv_arpt_nodedata=None;arv_arpt_linkdata=None
arv_arpt_nodemap=airportInterface.getLayout_node_map(arv_arpt_name)
arv_arpt_nodedata=airportInterface.getLayout_node_data(arv_arpt_name)
arv_arpt_linkdata=airportInterface.getLayout_links(arv_arpt_name)
arv_rwy_data=airportInterface.getAllRunways(arv_arpt_name)
#Step 3. From the obtained airport layout data, instantiate AirportLayout object.
#from PlotHelpers
arv_arpt_surf=ph.AirportLayout(arv_arpt_name)
arv_arpt_surf.initialize_from_NATS_airport_layout(arv_arpt_nodemap,arv_arpt_nodedata,arv_arpt_linkdata,arv_rwy_data)
arv_arpt_surf.set_altitude_ft(arv_arpt_instance.getElevation())
#Step 4. Design from the airport layout
#
#5. Plot and Save Options
#5.a Specify whether center and/or sector boundaries are displayed on the background.
#---------------------------
include_center=True
include_sector=False

##5.b
#The figure allows for the user to design a taxi plan and save. For saving the designed plan, set
#the following True.
#
write_route_to_file=True

#5.c The airport layout can also be written to a kml file that can be uploaded to Google MyMaps for
# looking at the layout with respect to builds and roads provided by Google Maps.
write_arpt_to_kml=True


#Step 6. Plot
#a.load center data
if include_center:
    centerfile = os.path.join(data_dir,'Centers_CONUS')
    #in Default, include center boundaries
    center_handle = ph.RegionHandler()
    center_handle.read_region_file(centerfile,'CENTER')

#b. load sector data
if include_sector:
    sectorfile = os.path.join(data_dir,'SectorData')  # large file. takes time in loading and plotting
    sector_handle = ph.RegionHandler()
    sector_handle.read_region_file(sectorfile,'SECTOR')

#c. Airport Layout and Route Design
fig=plt.figure(0)
fig.set_size_inches(9*12/7,9)
ax=fig.add_axes([0.05,0.05,0.9,0.9])
ax.set_facecolor('black')
#a.center plot and/or sector plot
include_center=True
if include_center:
    center_handle.plot_regions(plt,color='w')
if include_sector: #takes long time to plot
    sector_handle.plot_regions(plt,color='m')
#b.plot airport layout
#arpt_surf.plot_airport_layout(plt)
arv_arpt_surf.plot_airport_for_taxiroute_design(plt,airportInterface,ac_instance)

#c. when the route design is completed, the default route is also computed and compared
plt.show()

#Now set the designed route to the arrival airport
#a. retrieve
arv_taxi_route = arv_arpt_surf.get_designed_route()
if arv_taxi_route:
    arv_taxi_plan = ph.TaxiPlan(arv_arpt_surf)
    arv_taxi_plan.read_route_from_design_strings(arv_taxi_route)
else:
    example_csv='KJFK_arv_designed_taxi_route.csv'
    arv_taxi_plan = ph.TaxiPlan(arv_arpt_surf)
    arv_taxi_plan.read_csv_route(example_csv)

arv_node_name_sequence = arv_taxi_plan.get_node_names()
print(" user designed arrival routes:{}".format(arv_node_name_sequence))

# assign the user defined taxiroute as the taxi plan
airportInterface.setUser_defined_surface_taxi_plan(ac_flightid, arv_arpt_name, arv_node_name_sequence)
# confirm
rtn_arv_plan_str = airportInterface.getSurface_taxi_plan(ac_flightid, arv_arpt_name)
print("AC:{} arrival plan:{} is confirmed".format(ac_flightid, rtn_arv_plan_str))

#Step 4. dep_taxi_plan+flight plan+arv_taxi_plan

fp_lats=ac_instance.getFlight_plan_latitude_array()
fp_lons=ac_instance.getFlight_plan_longitude_array()

print("fp_lats:{}".format(fp_lats))


fig=plt.figure(1)
fig.set_size_inches(9*12/7,9)
ax=fig.add_axes([0.05,0.05,0.9,0.9])
ax.set_facecolor('black')
#a.center plot and/or sector plot
include_center=True
if include_center:
    center_handle.plot_regions(plt,color='w')
if include_sector: #takes long time to plot
    sector_handle.plot_regions(plt,color='m')
#b.plot airport layout
#arpt_surf.plot_airport_layout(plt)
dep_arpt_surf.plot_airport_layout(plt)
arv_arpt_surf.plot_airport_layout(plt)

plt.plot(fp_lons,fp_lats,'-r')

#TaxiPlans
dep_taxi_plan.plot_route(plt,'departure-taxi',linecolor='r')
arv_taxi_plan.plot_route(plt,'arrival-taxi',linecolor='r')

plt.show()


if write_route_to_file:
    if arv_arpt_surf.have_a_designed_route():
        arv_arpt_surf.write_taxiRoute_to_csv(arv_arpt_surf.get_airport_name()+"_arv_designed_taxi_route.csv")
if write_arpt_to_kml:
    if arv_arpt_surf:
        arv_arpt_surf.write_airport_layout_to_kml()

natsClient.disConnect()
#JVM shutdown
jp.shutdownJVM()