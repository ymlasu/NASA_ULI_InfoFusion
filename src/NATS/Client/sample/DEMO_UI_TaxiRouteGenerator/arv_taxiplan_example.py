#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This example illustrates how to design arriving taxi plan.

Author: Jun Yang
Date: 03/29/2018
Update: 2019.06.20
"""

import jpype as jp
import PlotHelpers as ph
import matplotlib.pyplot as plt
import os

env_NATS_CLIENT_HOME = os.environ.get('NATS_CLIENT_HOME')

str_NATS_CLIENT_HOME = ""

if not(env_NATS_CLIENT_HOME is None) :
    str_NATS_CLIENT_HOME = env_NATS_CLIENT_HOME + "/"

classpath = str_NATS_CLIENT_HOME + "dist/nats-client.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/nats-shared.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/json.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/rmiio-2.1.2.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/commons-logging-1.2.jar"

# Directory in which Center and Sector data are located
data_dir = './data'

flag_debug = False

# Start JVM and obtain NATS client
jp.startJVM(jp.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % classpath)
NATSClientFactory = jp.JClass('NATSClientFactory')
natsClient = NATSClientFactory.getNATSClient()

#Obtain the airport for the above aircraft
environmentInterface = natsClient.getEnvironmentInterface()
airportInterface = environmentInterface.getAirportInterface()

natsClient.login("admin")

# =============================================================================
# TaxiPlan for the arrival airport
#
# Step 1. Load TRX file and select an aircraft.
equipmentInterface = natsClient.getEquipmentInterface()
ac_if = equipmentInterface.getAircraftInterface()  # aircraft interface

dep_arpt_surf = None
arv_arpt_surf = None

if (not (ac_if)):
    print("cannot get AircraftInterface from NATS server")

ac_if.load_aircraft("share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx", "share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx")
ac_names = ac_if.getAllAircraftId()
print("Aircraft:{} are loaded".format(ac_names))

# Select the first aircraft
ac_instance = ac_if.select_aircraft(ac_names[0])
ac_flightid = ac_instance.getAcid()

dep_taxi_plan = None
arv_taxi_plan = None

dep_taxi_plan_file = 'KSFO_dep_designed_taxi_route.csv'
if not os.path.exists(dep_taxi_plan_file) :
    print dep_taxi_plan_file, "not found\n"
else :
    # For departure, load the designed route at KSFO
    dep_arpt_name = airportInterface.getDepartureAirport(ac_names[0])
    dep_arpt_nodemap = airportInterface.getLayout_node_map(dep_arpt_name)
    dep_arpt_nodedata = airportInterface.getLayout_node_data(dep_arpt_name)
    dep_arpt_linkdata = airportInterface.getLayout_links(dep_arpt_name)
    dep_rwy_data = airportInterface.getAllRunways(dep_arpt_name)
    dep_arpt_surf = ph.AirportLayout(dep_arpt_name)
    dep_arpt_surf.initialize_from_NATS_airport_layout(dep_arpt_nodemap, dep_arpt_nodedata, dep_arpt_linkdata, dep_rwy_data)

    dep_taxi_plan = ph.TaxiPlan(dep_arpt_surf)

    dep_taxi_plan.read_csv_route(dep_taxi_plan_file)
    dep_node_name_sequence = dep_taxi_plan.get_node_names()
    print("Departure: user designed routes:{}".format(dep_node_name_sequence))

    # Assign the user defined taxiroute as the taxi plan
    airportInterface.setUser_defined_surface_taxi_plan(ac_flightid, dep_arpt_name, dep_node_name_sequence)

    rtn_dep_plan_str = airportInterface.getSurface_taxi_plan(ac_flightid, dep_arpt_name)
    print("AC:{} departure plan:{} is confirmed".format(ac_flightid, rtn_dep_plan_str))

# For arrival.
arv_arpt_name = airportInterface.getArrivalAirport(ac_names[0])
print("AC:{} arrives at {}".format(ac_instance.getAcid(), arv_arpt_name))
arv_arpt_instance = airportInterface.select_airport(arv_arpt_name)

# Step 2. Obtain airport layout data and load it
# Read the airport layout for the above aircraft
arv_arpt_nodemap = None; arv_arpt_nodedata=None; arv_arpt_linkdata=None
arv_arpt_nodemap = airportInterface.getLayout_node_map(arv_arpt_name)
arv_arpt_nodedata = airportInterface.getLayout_node_data(arv_arpt_name)
arv_arpt_linkdata = airportInterface.getLayout_links(arv_arpt_name)
arv_rwy_data = airportInterface.getAllRunways(arv_arpt_name)

# Step 3. From the obtained airport layout data, instantiate AirportLayout object from PlotHelpers
arv_arpt_surf = ph.AirportLayout(arv_arpt_name)
arv_arpt_surf.initialize_from_NATS_airport_layout(arv_arpt_nodemap, arv_arpt_nodedata, arv_arpt_linkdata, arv_rwy_data)
arv_arpt_surf.set_altitude_ft(arv_arpt_instance.getElevation())

# Step 4. Plot and Save Options
# 4.a Specify whether center and/or sector boundaries are displayed on the background.
#---------------------------
include_center = True
include_sector = False

# 4.b
# The figure allows for the user to design a taxi plan and save. For saving the designed plan, set
# the following True.
write_route_to_file = True

# 4.c The airport layout can also be written to a kml file that can be uploaded to Google MyMaps for
#     looking at the layout with respect to builds and roads provided by Google Maps.
write_arpt_to_kml = True

# Step 5. Plot
# 5.a.load center data
if include_center:
    centerfile = os.path.join(data_dir, 'Centers_CONUS')
    #in Default, include center boundaries
    center_handle = ph.RegionHandler()
    center_handle.read_region_file(centerfile, 'CENTER')

# 5.b. load sector data
if include_sector:
    sectorfile = os.path.join(data_dir, 'SectorData')  # large file. takes time in loading and plotting
    sector_handle = ph.RegionHandler()
    sector_handle.read_region_file(sectorfile, 'SECTOR')

# 5.c. Airport Layout and Route Design
fig = plt.figure(0)
fig.set_size_inches(9*12/7, 9)
ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
ax.set_facecolor('black')

# center plot and/or sector plot
include_center = True
if include_center:
    center_handle.plot_regions(plt, color='w')
if include_sector: #takes long time to plot
    sector_handle.plot_regions(plt, color='m')

arv_arpt_surf.plot_airport_for_taxiroute_design(plt, airportInterface, ac_instance)

# Show
plt.show()

# =============================================================================

# Now set the designed route to the arrival airport
arv_taxi_route = arv_arpt_surf.get_designed_route()
if arv_taxi_route:
    arv_taxi_plan = ph.TaxiPlan(arv_arpt_surf)
    arv_taxi_plan.read_route_from_design_strings(arv_taxi_route)

fp_lats = None
fp_lons = None

if not(arv_taxi_plan is None) :
    arv_node_name_sequence = arv_taxi_plan.get_node_names()
    print(" user designed arrival routes:{}".format(arv_node_name_sequence))

    # Assign the user defined taxiroute as the taxi plan
    airportInterface.setUser_defined_surface_taxi_plan(ac_flightid, arv_arpt_name, arv_node_name_sequence)

    rtn_arv_plan_str = airportInterface.getSurface_taxi_plan(ac_flightid, arv_arpt_name)
    print("AC:{} arrival plan:{} is confirmed".format(ac_flightid, rtn_arv_plan_str))

    fp_lats = ac_instance.getFlight_plan_latitude_array()
    fp_lons = ac_instance.getFlight_plan_longitude_array()

    if flag_debug :
        print("fp_lats:{}".format(fp_lats))

    fig = plt.figure(1)
    fig.set_size_inches(9*12/7, 9)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_facecolor('black')

    #a.center plot and/or sector plot
    include_center = True
    if include_center:
        center_handle.plot_regions(plt, color='w')
    if include_sector: #takes long time to plot
        sector_handle.plot_regions(plt, color='m')

if not(dep_arpt_surf is None) :
    dep_arpt_surf.plot_airport_layout(plt)
if not(arv_arpt_surf is None) :
    arv_arpt_surf.plot_airport_layout(plt)

if not(fp_lats is None) and not(fp_lons is None) :
    plt.plot(fp_lons, fp_lats, '-r')

# =============================================================================

# Plot available departing/arriving taxi plan
if not(dep_taxi_plan is None) or not(arv_taxi_plan is None) :
    #TaxiPlans
    if not(dep_taxi_plan is None) :
        dep_taxi_plan.plot_route(plt, 'departure-taxi', linecolor='r')
    if not(arv_taxi_plan is None) :
        arv_taxi_plan.plot_route(plt, 'arrival-taxi', linecolor='r')
    
    print "\nShowing departing and arriving taxi plans if available"
    plt.show()

if write_route_to_file:
    if arv_arpt_surf.have_a_designed_route():
        arv_arpt_surf.write_taxiRoute_to_csv(arv_arpt_surf.get_airport_name()+"_arv_designed_taxi_route.csv")

if write_arpt_to_kml:
    if arv_arpt_surf:
        arv_arpt_surf.write_airport_layout_to_kml()

ac_if.release_aircraft()

natsClient.disConnect()

#JVM shutdown
jp.shutdownJVM()