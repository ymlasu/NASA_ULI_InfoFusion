# NATS sample
#
# Optimal Synthesis Inc.
#
# Oliver Chen
# 09.10.2019
#
# Demo of weather-related functions
#

from jpype import *
from array import *

import os
import time
import sys

env_NATS_CLIENT_HOME = os.environ.get('NATS_CLIENT_HOME')

str_NATS_CLIENT_HOME = ""

if not(env_NATS_CLIENT_HOME is None) :
    str_NATS_CLIENT_HOME = env_NATS_CLIENT_HOME + "/"

classpath = str_NATS_CLIENT_HOME + "dist/nats-client.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/nats-shared.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/json.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/commons-logging-1.2.jar"

startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % classpath)

# NATS simulation status definition
# You can get simulation status from the server and know what it refers to
NATS_SIMULATION_STATUS_READY = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_READY
NATS_SIMULATION_STATUS_START = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_START
NATS_SIMULATION_STATUS_PAUSE = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_PAUSE
NATS_SIMULATION_STATUS_RESUME = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_RESUME
NATS_SIMULATION_STATUS_STOP = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_STOP
NATS_SIMULATION_STATUS_ENDED = JPackage('com').osi.util.Constants.NATS_SIMULATION_STATUS_ENDED

NATSClientFactory = JClass('NATSClientFactory')
natsClient = NATSClientFactory.getNATSClient()
simulationInterface = natsClient.getSimulationInterface()
equipmentInterface = natsClient.getEquipmentInterface()
aircraftInterface = equipmentInterface.getAircraftInterface()

environmentInterface = natsClient.getEnvironmentInterface()
airportInterface = environmentInterface.getAirportInterface()
terminalAreaInterface = environmentInterface.getTerminalAreaInterface()
weatherInterface = environmentInterface.getWeatherInterface()

entityInterface = natsClient.getEntityInterface()
controllerInterface = entityInterface.getControllerInterface()
pilotInterface = entityInterface.getPilotInterface()


natsClient.login("admin")

environmentInterface.load_rap("share/tg/rap")

print ""
print "************************************************"
print "Get wind data"
print "************************************************"
print ""

# Demo of getting wind data -------------------------------
t = 6600
lat_deg = 40.0
lon_deg = -73.0
alt_ft = 20000.0

windResultArray = weatherInterface.getWind(t, lat_deg, lon_deg, alt_ft)
if not(windResultArray is None) :
    print "Wind result(t=", t, ", lat=", lat_deg, ", lon=", lon_deg, ", altitude=", alt_ft, ") = [", windResultArray[0], ", ", windResultArray[1], "]"
# end - Demo of getting wind data -------------------------


print ""
print "********************************************************"
print "Simulate trajectory and get weather polygons when paused"
print "********************************************************"
print ""

# Demo of getting conflicting weather polygon data ----------------------------

# Download weather data files(not the severe traffic-blocking weather definition)
# This function is only needed to be called when new weather files are required
#weatherInterface.downloadWeatherFiles();

aircraftInterface.load_aircraft("share/tg/trx/test_KLAX_KSFO.trx", "share/tg/trx/test_KLAX_KSFO_mfl.trx")

simulationInterface.setupSimulation(11000, 30)

simulationInterface.start(3210)
             
# Use a while loop to constantly check server status.  When server simulation finishes, continue to output the trajectory data
while True:
    server_runtime_sim_status = simulationInterface.get_runtime_sim_status()
    if (server_runtime_sim_status == NATS_SIMULATION_STATUS_PAUSE) :
        break
    else:
        time.sleep(1)

# Till here, the simulation paused
# We can work on getting the weather polygon info as follows

ac_id = "ULI-3533A88AE5"

curAircraft = aircraftInterface.select_aircraft(ac_id)
if not(curAircraft is None):
    lat_deg = curAircraft.getLatitude_deg() # Set latitude
        
    lon_deg = curAircraft.getLongitude_deg() # Set longitude
        
    alt_ft = 33000.0 # Set altitude
    nauticalMile_radius = 100.0 # Set nautical mile radius
        
    #controllerInterface.setWeather_pirepFile("") # NATS automatically pick latest file

    #controllerInterface.setWeather_polygonFile("share/rg/polygons/MACS_scenario.dat")
    #controllerInterface.setWeather_polygonFile("") # NATS automatically pick latest file

    controllerInterface.setWeather_sigmetFile("share/tg/weather/demo_20190906_182626.sigmet")
    #controllerInterface.setWeather_sigmetFile("") # NATS automatically pick latest file

    # Get weather polygons
    weatherPolygonArray = weatherInterface.getWeatherPolygons(ac_id, lat_deg, lon_deg, alt_ft, nauticalMile_radius)
    if not(weatherPolygonArray is None) :
        for i in range(0, len(weatherPolygonArray)) :
            curWeatherPolygon = weatherPolygonArray[i]
            if not(curWeatherPolygon is None) and (0 < len(curWeatherPolygon.getX_data())):
                x_data_array = curWeatherPolygon.getX_data()
                y_data_array = curWeatherPolygon.getY_data()
                print "WeatherPolygon", i, ", number of vertices = ", curWeatherPolygon.getNum_vertices()
                
# Print more data
#                 print "    xmin = ", curWeatherPolygon.getXmin(), " xmax = ", curWeatherPolygon.getXmax(), \
#                 ", ymin = ", curWeatherPolygon.getYmin(), " ymax = ", curWeatherPolygon.getYmax(), \
#                 ", x_centroid = ", curWeatherPolygon.getX_centroid(), ", y_centroid = ", curWeatherPolygon.getY_centroid(), \
#                 ", poly_type = ", curWeatherPolygon.getPoly_type(), \
#                 ", start_hr = ", curWeatherPolygon.getStart_hr(), ", end_hr = ", curWeatherPolygon.getEnd_hr()
                
                for j in range(0, len(curWeatherPolygon.getX_data())) :
                    print "    x_data = ", x_data_array[j], ", y_data = ", y_data_array[j]
                
                print ""
    else :
        print "No weather polygon data found"

simulationInterface.resume()

while True:
    server_runtime_sim_status = simulationInterface.get_runtime_sim_status()
    if (server_runtime_sim_status == NATS_SIMULATION_STATUS_ENDED) :
        break
    else:
        time.sleep(1)

aircraftInterface.release_aircraft()
# end - Demo of getting conflicting weather polygon data ----------------------


environmentInterface.release_rap()

# Close connection from NATS Server
natsClient.disConnect()

shutdownJVM()
