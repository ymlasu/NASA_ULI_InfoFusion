'''
NATS API Function unit test suite

This function can be run to ensure appropriate installation of NATS and to verify functions are working.

Date: 15th July, 2019

Author: Vedik Jayaraj

'''


# encoding:utf-8

from jpype import *
from array import *
import PathVisualizer

import os
import time

env_NATS_CLIENT_HOME = os.environ.get('NATS_CLIENT_HOME')

str_NATS_CLIENT_HOME = ""

if not(env_NATS_CLIENT_HOME is None) :
    str_NATS_CLIENT_HOME = env_NATS_CLIENT_HOME + "/"

classpath = str_NATS_CLIENT_HOME + "dist/nats-client.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/nats-shared.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/json.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/rmiio-2.1.2.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/commons-logging-1.2.jar"

startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % classpath)

# Flight phase value definition
# You can detect and know the flight phase by checking its value
FLIGHT_PHASE_PREDEPARTURE = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_PREDEPARTURE;
FLIGHT_PHASE_ORIGIN_GATE = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_ORIGIN_GATE;
FLIGHT_PHASE_PUSHBACK = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_PUSHBACK;
FLIGHT_PHASE_RAMP_DEPARTING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_RAMP_DEPARTING;
FLIGHT_PHASE_TAXI_DEPARTING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TAXI_DEPARTING;
FLIGHT_PHASE_RUNWAY_THRESHOLD_DEPARTING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_RUNWAY_THRESHOLD_DEPARTING;
FLIGHT_PHASE_TAKEOFF = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TAKEOFF;
FLIGHT_PHASE_CLIMBOUT = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_CLIMBOUT;
FLIGHT_PHASE_HOLD_IN_DEPARTURE_PATTERN = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_HOLD_IN_DEPARTURE_PATTERN;
FLIGHT_PHASE_CLIMB_TO_CRUISE_ALTITUDE = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_CLIMB_TO_CRUISE_ALTITUDE;
FLIGHT_PHASE_TOP_OF_CLIMB = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TOP_OF_CLIMB;
FLIGHT_PHASE_CRUISE = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_CRUISE;
FLIGHT_PHASE_HOLD_IN_ENROUTE_PATTERN = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_HOLD_IN_ENROUTE_PATTERN;
FLIGHT_PHASE_TOP_OF_DESCENT = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TOP_OF_DESCENT;
FLIGHT_PHASE_INITIAL_DESCENT = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_INITIAL_DESCENT;
FLIGHT_PHASE_HOLD_IN_ARRIVAL_PATTERN = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_HOLD_IN_ARRIVAL_PATTERN
FLIGHT_PHASE_APPROACH = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_APPROACH;
FLIGHT_PHASE_FINAL_APPROACH = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_FINAL_APPROACH;
FLIGHT_PHASE_GO_AROUND = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_GO_AROUND;
FLIGHT_PHASE_TOUCHDOWN = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TOUCHDOWN;
FLIGHT_PHASE_LAND = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_LAND;
FLIGHT_PHASE_EXIT_RUNWAY = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_EXIT_RUNWAY;
FLIGHT_PHASE_TAXI_ARRIVING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_TAXI_ARRIVING;
FLIGHT_PHASE_RUNWAY_CROSSING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_RUNWAY_CROSSING;
FLIGHT_PHASE_RAMP_ARRIVING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_RAMP_ARRIVING;
FLIGHT_PHASE_DESTINATION_GATE = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_DESTINATION_GATE;
FLIGHT_PHASE_LANDED = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_LANDED;
FLIGHT_PHASE_HOLDING = JPackage('com').osi.util.FlightPhase.FLIGHT_PHASE_HOLDING;

AIRCRAFT_CLEARANCE_PUSHBACK = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_PUSHBACK
AIRCRAFT_CLEARANCE_TAXI_DEPARTING = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_TAXI_DEPARTING
AIRCRAFT_CLEARANCE_TAKEOFF = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_TAKEOFF
AIRCRAFT_CLEARANCE_ENTER_ARTC = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_ENTER_ARTC
AIRCRAFT_CLEARANCE_DESCENT_FROM_CRUISE = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_DESCENT_FROM_CRUISE
AIRCRAFT_CLEARANCE_ENTER_TRACON = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_ENTER_TRACON
AIRCRAFT_CLEARANCE_APPROACH = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_APPROACH
AIRCRAFT_CLEARANCE_TOUCHDOWN = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_TOUCHDOWN
AIRCRAFT_CLEARANCE_TAXI_LANDING = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_TAXI_LANDING
AIRCRAFT_CLEARANCE_RAMP_LANDING = JPackage('com').osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_RAMP_LANDING

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
safetyMetricsInterface = natsClient.getSafetyMetricsInterface()
groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()

environmentInterface = natsClient.getEnvironmentInterface()
airportInterface = environmentInterface.getAirportInterface()
terminalAreaInterface = environmentInterface.getTerminalAreaInterface()

entityInterface = natsClient.getEntityInterface()
controllerInterface = entityInterface.getControllerInterface()
pilotInterface = entityInterface.getPilotInterface()
groundOperatorInterface = entityInterface.getGroundOperatorInterface()

natsClient.login("admin")

# result variable stores flag on successful unit tests
result = 0

try:
	NATSClientFactory    =    JClass('NATSClientFactory')
	natsClient    =    NATSClientFactory.getNATSClient()
	entityInterface    =    natsClient.getEntityInterface()
	assert entityInterface is not None, "getEntityInterface"

	NATSClientFactory    =    JClass('NATSClientFactory')
	natsClient    =    NATSClientFactory.getNATSClient()
	environmentInterface    =    natsClient.getEnvironmentInterface()
	assert environmentInterface is not None, "getEnvironmentInterface"

	NATSClientFactory    =    JClass('NATSClientFactory')
	natsClient    =    NATSClientFactory.getNATSClient()
	equipmentInterface    =    natsClient.getEquipmentInterface()
	assert equipmentInterface is not None, "getEquipmentInterface"

	NATSClientFactory    =    JClass('NATSClientFactory')
	natsClient    =    NATSClientFactory.getNATSClient()
	safetyMetricsInterface    =    natsClient.getSafetyMetricsInterface()
	assert safetyMetricsInterface is not None, "getSafetyMetricsInterface"

	NATSClientFactory    =    JClass('NATSClientFactory')
	natsClient    =    NATSClientFactory.getNATSClient()
	safetyMInterface    =    natsClient.getSafetyMInterface()
	assert safetyMInterface is not None, "getSafetyMInterface"

	NATSClientFactory    =    JClass('NATSClientFactory')
	natsClient    =    NATSClientFactory.getNATSClient()
	natsClient.disConnect()
	#assert safetyMetricsInterface is not None, "getSafetyMetricsInterface"

	NATSClientFactory    =    JClass('NATSClientFactory')
	natsClient    =    NATSClientFactory.getNATSClient()
	natsClient.login('admin')


	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.clear_trajectory()


	simulationInterface    =    natsClient.getSimulationInterface()
	currentTime    =    simulationInterface.get_curr_sim_time()
	assert currentTime == 0.0, "get_curr_sim_time"

	simulationInterface    =    natsClient.getSimulationInterface()
	simulation_id    =    simulationInterface.get_sim_id()
	assert simulation_id == 0, "get_sim_id"

	simulationInterface    =    natsClient.getSimulationInterface()
	currentRuntimeStatus    =    simulationInterface.get_runtime_sim_status()
	assert currentRuntimeStatus == 0, "get_runtime_sim_status"


	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.pause()
	currentRuntimeStatus    =    simulationInterface.get_runtime_sim_status()
	assert currentRuntimeStatus == 0, "pause"

	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.resume()
	currentRuntimeStatus    =    simulationInterface.get_runtime_sim_status()
	assert currentRuntimeStatus == 0, "resume"


	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.resume(1000)
	currentRuntimeStatus    =    simulationInterface.get_runtime_sim_status()
	assert currentRuntimeStatus == 0, "resume"

	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.resume(1000.5)
	currentRuntimeStatus    =    simulationInterface.get_runtime_sim_status()
	assert currentRuntimeStatus == 0, "resume"

	simulationInterface    =    natsClient.getSimulationInterface()
	assert simulationInterface.setupSimulation    (10000,    5) == 0, "setupSimulation"


	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.start()
	currentRuntimeStatus    =    simulationInterface.get_runtime_sim_status()
	assert currentRuntimeStatus == 1, "start"

	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.start(1200)
	currentRuntimeStatus    =    simulationInterface.get_runtime_sim_status()
	assert currentRuntimeStatus == 1, "start"


	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.start(150.65)
	currentRuntimeStatus    =    simulationInterface.get_runtime_sim_status()
	assert currentRuntimeStatus == 1, "start"


	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.startRealTime()
	currentRuntimeStatus    =    simulationInterface.get_runtime_sim_status()
	assert currentRuntimeStatus == 1, "startRealTime"

	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.stop()
	currentRuntimeStatus    =    simulationInterface.get_runtime_sim_status()
	assert currentRuntimeStatus == 	4, "stop"

	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.write_trajectories    ('SimulationTrajectory.csv')


	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraftInterface.load_aircraft("share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx",    "share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx")

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicleInterface.load_groundVehicle('share/tg/trx/TRX_DEMO_11GroundVehicles.trx')

	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.request_aircraft('SWA1897')

	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.request_groundVehicle('BUS123')


	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.externalAircraft_create_trajectory_profile(    
	'ABC173',"B733",    "KPHX",
	'KSFO',    33000.0,    430.0,    37.2,    -122.4,    2500.0,    215.0,    240.0,    318.2,    
	'FLIGHT_PHASE_CRUISE')


	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.externalAircraft_inject_trajectory_state_data("ABC173",    32.61,    -122.39,    3200,
	30,    250,    50,    'FLIGHT_PHASE_CRUISE',    1541784961725)


	simulationInterface    =    natsClient.getSimulationInterface()
	simulationInterface.requestDownloadTrajectoryFile()


	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	assert aircraftInterface is not None, "getAircraftInterface"


	equipmentInterface    =    natsClient.getEquipmentInterface()
	groundVehicleInterface    =    equipmentInterface.getGroundVehicleInterface    ()
	assert groundVehicleInterface is not None, "getGroundVehicleInterface"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	cnsInterface    =    equipmentInterface.getCNSInterface()
	assert cnsInterface is not None, "getCNSInterface"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	BADADataInterface    =    equipmentInterface.getBADADataInterface()
	assert BADADataInterface is not None, "getBADADataInterface"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	#result    =    aircraftInterface.validate_flight_plan_record("TRACK    SWA1897 B733    373628.6    1222248.0    0    0.13    280    ZOA    ZOA46",    "FP_ROUTE #KSFO./.RW01R.SSTIK4.LOSHN..BOILE..BLH.HYDRR1.I07R.RW07R.<>.KPHX",    37000)

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraftIds    =    aircraftInterface.getAircraftIds(28.5,    30.7,    72.8,    74.9,    15000.0,    20000.9)
	assert aircraftIds == None, "getAircraftId"


	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraftIds    =    list(aircraftInterface.getAllAircraftId())
	assert aircraftIds == ['ABC173', 'SWA1897'], "getAircraftId"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	assert aircraft != None, "select_aircraft"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	assert aircraftInterface.synchronize_aircraft_to_server(aircraft) == 0, "synchronize_aircraft_to_server"


	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	assert aircraft != None, "select_aircraft"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	aircraftId    =    aircraft.getAcid()
	assert aircraftId == 'SWA1897', "getAcid"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	aircraftAltitude    =    aircraft.getAltitude_ft    ()
	assert aircraftAltitude == 13, "getAltitude_ft"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	aircraftCruiseAltitude    =    aircraft.getCruise_alt_ft()
	assert aircraftCruiseAltitude == 33000.0, "getCruise_alt_ft"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	aircraftCruiseAirspeed    =    aircraft.getCruise_tas_knots()
	assert aircraftCruiseAirspeed == 430.0, "getCruise_tas_knots"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightDepartureTime    =    aircraft.getDeparture_time_sec()
	assert flightDepartureTime == 0.0, "getDeparture_time_sec"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	destinationAirportElevation    =    aircraft.getDestination_airport_elevation_ft()
	assert destinationAirportElevation == 1135.0, "getDestination_airport_elevation_ft"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightPhase    =    aircraft.getFlight_phase()
	assert flightPhase == 1, "getFlight_phase"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightLatitudeArray    =    list(aircraft.getFlight_plan_latitude_array())
	assert flightLatitudeArray == [37.60769271850586, 37.658206939697266, 37.6783447265625, 37.489784240722656, 37.14235305786133, 36.48748779296875, 35.84760665893555, 34.42243957519531, 33.596065521240234, 33.511531829833984, 33.46272277832031, 33.43552780151367, 33.337242126464844, 33.297386169433594, 33.27430725097656,33.28049850463867, 33.329689025878906, 33.401893615722656, 33.42845153808594, 33.428619384765625, 33.42874526977539, 33.431034088134766, 33.428829193115234, 33.428855895996094, 33.42885971069336]

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightPlanLength    =    aircraft.getFlight_plan_length()
	assert flightPlanLength == 25, "getFlight_plan_length"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightLongitudeArray    =    aircraft.getFlight_plan_longitude_array()
	assert list(flightLongitudeArray) == [-122.38014221191406, -122.34657287597656, -122.36165618896484, -122.47457885742188, -121.93738555908203, -120.94786071777344, -120.00047302246094, -118.0258560180664, -114.76126861572266, -114.32807922363281, -114.08177947998047, -113.94625091552734, -113.46075439453125, -113.23030090332031, -113.06967163085938, -112.82159423828125, -112.69026947021484, -112.50096130371094, -112.4253921508789, -112.35429382324219, -112.28280639648438, -112.2069320678711, -112.21131134033203, -112.14168548583984, -112.027099609375]


	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightWaypointNameArray    =    aircraft.getFlight_plan_waypoint_name_array()
	assert list(flightWaypointNameArray) == ['RW01R-KSFO', 'HEADING OR COURSE_TO_ALTITUDE_RW01R-KSFO', 'SSTIK', 'PORTE', 'TOP_OF_CLIMB_PT', 'KAYEX', 'LOSHN', 'BOILE', 'BLH', 'TOP_OF_DESCENT_PT', 'SCOLE', 'SPINK', 'SNRRA', 'SWOON', 'HYDRR', 'GEELA', 'PUNNT', 'TEICH', 'TESLE', 'FALGO', 'CAGOR', 'FOWLE', 'BALTE', 'TOTIE', 'RW07R-KPHX']

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightAltitudeDescriptionArray    =    aircraft.getFlight_plan_alt_desc_array()
	assert list(flightAltitudeDescriptionArray) == ['+', '+', 'NONE', '-', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', '+', '-', 'NONE', 'B', 'B', 'B', 'B', 'NONE', 'NONE', '+', '+', 'J', 'H', 'NONE']


	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightPlanAltitude1Array    =    aircraft.getFlight_plan_alt_1_array()
	assert list(flightPlanAltitude1Array) == [520.0, 520.0, -10000.0, 10000.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, 25000.0, 24000.0, 22000.0, -10000.0, 19000.0, 17000.0, 12000.0, 9000.0, 7000.0, 6000.0, 5000.0, 4000.0, 4000.0, 3000.0, 1168.0], "getFlight_plan_alt_1_array"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightPlanAltitude2Array    =    aircraft.getFlight_plan_alt_2_array()
	assert list(flightPlanAltitude2Array) == [-10000.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, 15000.0, 11000.0, 10000.0, 8000.0, -10000.0, -10000.0, -10000.0, -10000.0, 3000.0, 3000.0, -10000.0], "getFlight_plan_alt_2_array"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightPlanSpeedLimitArray    =    aircraft.getFlight_plan_speed_limit_array()
	assert list(flightPlanSpeedLimitArray) == [210.0, 210.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0, 280.0, -10000.0, -10000.0, -10000.0, 265.0, 250.0, 230.0, 210.0, -10000.0, 210.0, -10000.0, -10000.0, -10000.0, -10000.0, -10000.0], "getFlight_plan_speed_limit_array"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightSpeedLimitDescriptionArray    =    aircraft.getFlight_plan_speed_limit_desc_array()
	assert list(flightSpeedLimitDescriptionArray) == ['-', '-', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE'], "getFlight_plan_speed_limit_desc_array"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightPathAngle    =    aircraft.getFpa_rad()
	assert flightPathAngle == 0.0, "getFpa_rad"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	courseAngle    =    aircraft.getCourse_rad()
	assert courseAngle == 0.48869219422340393, "getCourse_rad()"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightLandedFlag    =    aircraft.getLanded_flag()
	assert flightLandedFlag == 0, "getLanded_flag"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightCurrentLatitude    =    aircraft.getLatitude_deg()
	assert flightCurrentLatitude == 37.621368408203125, "getLatitude_deg"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	flightCurrentLongitude=    aircraft.getLongitude_deg()
	assert flightCurrentLongitude == -122.39006042480469, "getLongitude_deg"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	originAirportElevation    =    aircraft.getOrigin_airport_elevation_ft()
	assert originAirportElevation == 13, "getOrigin_airport_elevation_ft"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	rateOfClimbOrDescent    =    aircraft.getRocd_fps()
	assert rateOfClimbOrDescent == 0.0, "getRocd_fps"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	sectorIndex    =    aircraft.getSector_index()
	assert sectorIndex == -1, "getSector_index"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	targetWaypointIndex    =    aircraft.getTarget_waypoint_index()
	assert targetWaypointIndex == 1, "getTarget_waypoint_index"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	targetWaypointName    =    aircraft.getTarget_waypoint_name()
	assert targetWaypointName == "Ramp_06_011", "getTarget_waypoint_name"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	currentAirspeed    =    aircraft.getTas_knots()
	assert currentAirspeed == 0.0, "getTas_knots"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	topOfClimbIndex    =    aircraft.getToc_index()
	assert topOfClimbIndex == 4, "getToc_index"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	topOfDescentIndex    =    aircraft.getTod_index()
	assert topOfDescentIndex == 9, "getTod_index"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	aircraft.setAltitude_ft(27500)
	assert aircraft.getAltitude_ft() == 27500, "setAltitude_ft"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')    
	aircraft.setCruise_alt_ft(35000)
	assert aircraft.getCruise_alt_ft() == 35000, "setCruise_alt_ft"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	aircraft.setCruise_tas_knots(455)
	assert aircraft.getCruise_tas_knots() == 455, "setCruise_tas_knots"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')    
	aircraft.setFlight_plan_latitude_deg(5,    34.50)

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	aircraft.setFlight_plan_longitude_deg(5,    -122.63)

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	aircraft.setLatitude_deg(26.58)
	assert aircraft.getLatitude_deg() == 26.579999923706055, "setLatitude_deg"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	aircraft.setLongitude_deg    (-122.36)
	assert aircraft.getLongitude_deg() == -122.36000061035156, "setLongitude_deg"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	aircraft.setRocd_fps(-50)
	assert aircraft.getRocd_fps() == -50, "setRocd_fps"

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	#aircraft.setTarget_waypoint_latitude_deg(35.63)

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	#aircraft.setTarget_waypoint_longitude_deg(-118.25)

	equipmentInterface    =    natsClient.getEquipmentInterface()
	aircraftInterface    =    equipmentInterface.getAircraftInterface()
	aircraft    =    aircraftInterface.select_aircraft('SWA1897')
	aircraft.setTas_knots(400)
	assert aircraft.getTas_knots() == 400, "setTas_knots"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	assert groundVehicleInterface.load_groundVehicle('share/tg/trx/TRX_DEMO_11GroundVehicles.trx') == 0, "load_groundVehicle"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	assert groundVehicleInterface.release_groundVehicle() == 0, "release_groundVehicle"


	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	assignedGroundVehicles = groundVehicleInterface.getAssignedGroundVehicleIds()
	assert list(assignedGroundVehicles) == ['BUS123'], "getAssignedGroundVehicleIds"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	assignedGroundVehicles = groundVehicleInterface.getAssignedGroundVehicleIds("admin")
	assert list(assignedGroundVehicles) == ['BUS123'], "getAssignedGroundVehicleIds"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	assert groundVehicleInterface.externalGroundVehicle_create_trajectory_profile('NEW123', 'DWA1897', 'KSFO', 37, -122, 15, 28) == 0, "externalGroundVehicle_create_trajectory_profile"


	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	assert groundVehicleInterface.externalGroundVehicle_inject_trajectory_state_data('NEW123', 'DWA1897', 37, -122, 15, 28) == 1, "externalGroundVehicle_inject_trajectory_state_data"


	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicleInterface.load_groundVehicle('share/tg/trx/TRX_DEMO_11GroundVehicles.trx') == 0, "load_groundVehicle"
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicleId = groundVehicle.getGvid()
	assert groundVehicleId == 'BUS123', "getGvid"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicleAirportId = groundVehicle.getAirportId()
	assert groundVehicleAirportId == "KPHL", "getAirportId"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	aircraftInService = groundVehicle.getAircraftInService()
	assert aircraftInService == "SWA1898", "aircraftInService"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	isExternalGroundVehicle = groundVehicle.getFlag_external_groundvehicle()
	assert isExternalGroundVehicle == False, "getFlag_external_groundvehicle"


	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	user = groundVehicle.getAssigned_user()
	assert user == None, "getAssigned_user"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	latitude = groundVehicle.getLatitude()
	assert latitude == 39.8608512878418, "getLatitude"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicle.setLatitude(37.8959)
	assert groundVehicle.getLatitude() == 37.89590072631836, "setLatitude" 

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	longitude = groundVehicle.getLongitude()
	assert longitude == -75.2750015258789, "getLongitude"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicle.setLongitude(-112.8594)
	assert groundVehicle.getLongitude() == -112.8593978881836

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	altitude = groundVehicle.getAltitude()
	assert altitude == 36, "getAltitude"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicleSpeed = groundVehicle.getSpeed()
	assert groundVehicleSpeed == 15, "getSpeed"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicle.setSpeed(25)
	assert groundVehicle.getSpeed() == 25, "setSpeed"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicleCourse = groundVehicle.getCourse()
	assert groundVehicle.getSpeed() == 25, "setSpeed"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicle.setCourse(1.5)
	assert groundVehicle.getCourse() == 1.5, "getCourse"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicleDepartureTime = groundVehicle.getDeparture_time()
	assert groundVehicleDepartureTime == 1121238016.0, "getDeparture_time"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicleDrivePlanLatitudeArray = groundVehicle.getDrive_plan_latitude_array()
	assert list(groundVehicleDrivePlanLatitudeArray) == [39.86085891723633, 39.8615608215332, 39.86195373535156, 39.86222839355469, 39.86335372924805, 39.86442947387695, 39.86484146118164, 39.86528778076172, 39.86579132080078, 39.86635971069336, 39.86701965332031, 39.867218017578125, 39.867286682128906, 39.867347717285156, 39.86766815185547, 39.86940002441406, 39.86978530883789, 39.8698844909668, 39.869991302490234, 39.87047576904297, 39.87074661254883, 39.870784759521484, 39.870994567871094, 39.8713493347168, 39.87214660644531, 39.87303161621094, 39.87363815307617, 39.87407302856445, 39.87416076660156], "getDrive_plan_latitude_array"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicleDrivePlanLongitudeArray = groundVehicle.getDrive_plan_longitude_array()
	assert list(groundVehicleDrivePlanLongitudeArray) == [-75.27500915527344, -75.275390625, -75.27523040771484, -75.27379608154297, -75.26821899414062, -75.26856231689453, -75.2686996459961, -75.26885223388672, -75.26901245117188, -75.26919555664062, -75.26912689208984, -75.26807403564453, -75.26701354980469, -75.26642608642578, -75.26558685302734, -75.25774383544922, -75.25584411621094, -75.25531005859375, -75.2547836303711, -75.25492095947266, -75.25504302978516, -75.25445556640625, -75.25346374511719, -75.25358581542969, -75.25385284423828, -75.25373840332031, -75.2535171508789, -75.25334930419922, -75.25212860107422], "getDrive_plan_longitude_array"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicleDrivePlanLength = groundVehicle.getDrive_plan_length()
	assert groundVehicleDrivePlanLength == 29, "getDrive_plan_length"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicleDrivePlanWaypointNames = groundVehicle.getDrive_plan_waypoint_name_array()
	assert list(groundVehicleDrivePlanWaypointNames) == ['Rwy_01_001', 'Txy_S_001', 'Txy_S_102', 'Txy_S_002', 'Txy_S_003', 'Txy_Z_009', 'Txy_Z_010', 'Txy_Z_011', 'Txy_Z_012', 'Txy_Z_013', 'Txy_Z_014', 'Parking_deice1_002', 'Txy_Z_003', 'Txy_Z_016', 'Txy_Z_017', 'Txy_K_001', 'Txy_K_002', 'Txy_K_003', 'Txy_K_004', 'spot_02S', 'Ramp_13_001', 'spot_02E', 'Txy_J_004', 'Ramp_01_001', 'Ramp_01_002', 'Ramp_01_003', 'Ramp_01_004', 'Ramp_01_005', 'Gate_AW_018'], "groundVehicleDrivePlanWaypointNames"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicleTargetWaypointIndex = groundVehicle.getTarget_waypoint_index()
	assert groundVehicleTargetWaypointIndex == -1, "getTarget_waypoint_index"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicleTargetWaypointName = groundVehicle.getTarget_waypoint_name()
	assert groundVehicleTargetWaypointName == "", "getTarget_waypoint_name"

	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicle.setDrive_plan_latitude(2, 37.2518)


	equipmentInterface = natsClient.getEquipmentInterface()
	groundVehicleInterface = equipmentInterface.getGroundVehicleInterface()
	groundVehicle = groundVehicleInterface.select_groundVehicle('BUS123')
	groundVehicle.setDrive_plan_longitude(2, -112.8155)


	#cnsInterface = equipmentInterface.getCNSInterface()
	#assert list(cnsInterface.getLineOfSight(33.440903, -111.992862, 1135, 33.274183,-112.147879, 1500)) == [63941.91097170863, -142.12357110622827, -0.19993744381629813, 1.0], "getLineOfSight"


	cnsInterface = equipmentInterface.getCNSInterface()
	assert cnsInterface.setNavigationLocationError('SWA1897', 'LATITUDE',
	0.00005, 0.00000001, 0.9, 0.2, 1) == 0, "setNavigationLocationError"
	assert cnsInterface.setNavigationLocationError('SWA1897', 'LONGITUDE',
	0.00005, 0.00000001, 0.9, 0.2, 1) == 0, "setNavigationLocationError"


	cnsInterface = equipmentInterface.getCNSInterface()
	assert cnsInterface.setNavigationAltitudeError('SWA1897', .00005, 0.2, 0) == 0, "setNavigationAltitudeError"

	cnsInterface = equipmentInterface.getCNSInterface()
	assert cnsInterface.setRadarError('KSFO', 'RANGE', 25, 0.0000005, 0.2, 1) == 0, "setRadarError"
	assert cnsInterface.setRadarError('KSFO', 'AZIMUTH', 30, 0.0000005, 0.2, 1) == 0, "setRadarError"
	assert cnsInterface.setRadarError('KSFO', 'ELEVATION', 2500,0.0000005,0.2,1) == 0, "setRadarError"


	badaDataInterface    =    equipmentInterface.getBADADataInterface()
	assert badaDataInterface.getBADA_cruiseTas('B733',    15000) == 341.5, "getBADA_cruiseTas"


	badaDataInterface    =    equipmentInterface.getBADADataInterface()
	assert badaDataInterface.getBADA_climbRate_fpm('B733',    150,    'NOMINAL') == 2584.0, "getBADA_climbRate_fpm"


	badaDataInterface    =    equipmentInterface.getBADADataInterface()
	assert badaDataInterface.getBADA_climbTas('B733',    15000) == 371.5, "getBADA_climbTas"


	badaDataInterface    =    equipmentInterface.getBADADataInterface()
	assert badaDataInterface.getBADA_descentRate_fpm('B733',    150,    'NOMINAL') == 776.0, "getBADA_descentRate_fpm"


	badaDataInterface    =    equipmentInterface.getBADADataInterface()
	assert badaDataInterface.getBADA_descentTas('B733',    15000) == 347.5, "getBADA_descentTas"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	assert environmentInterface.load_rap("share/tg/rap") == None, "load_rap"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	assert environmentInterface.release_rap() == 0, "release_rap"


	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	assert airportInterface != None, "getAirportInterface"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terrainInterface    =    environmentInterface.getTerrainInterface()
	assert terrainInterface != None, "getTerrainInterface"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =    environmentInterface.getTerminalAreaInterface()
	assert terminalAreaInterface != None, "getTerminalAreaInterface"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	weatherInterface    =    environmentInterface.getWeatherInterface()
	assert weatherInterface != None, "getWeatherInterface"

	environmentInterface = natsClient.getEnvironmentInterface()
	assert list(environmentInterface.getCenterCodes()) == ['KZAU', 'KZBW', 'KZDC', 'KZDV', 'KZFW', 'KZHU', 'KZID', 'KZJX', 'KZKC', 'KZLA', 'KZLC', 'KZMA', 'KZME', 'KZMP', 'KZNY', 'KZOA', 'KZOB', 'KZSE', 'KZTL', 'PZAN', 'PZHN', 'KZAB']

	environmentInterface = natsClient.getEnvironmentInterface()
	assert len(list(environmentInterface.getFixesInCenter('KZOA'))) == 2399, "getFixesInCenter"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	airport    =    airportInterface.select_airport('KPHX')
	assert airport != None, "select_airport"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	arrivalAirport    =    airportInterface.getArrivalAirport('SWA1897')
	assert arrivalAirport == "KPHX", "getArrivalAirport"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	departureAirport    =    airportInterface.getDepartureAirport('SWA1897')
	assert departureAirport == "KSFO", "getDepartureAirport"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	airportLocation    =    airportInterface.getLocation('KLAX')
	assert list(airportLocation) == [33.94249444444444, -118.40805], "getLocation"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	closestAirport    =    airportInterface.getClosestAirport(35.2,    -118.6)
	assert closestAirport == "KTSP", "getClosestAirport"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	airports    =    airportInterface.getAirportsWithinMiles(35.2, -118.6, 22.5)
	assert list(airports) == ['5CL8', '62CL', '7CA2', 'KTSP', 'L94'], "getAirportsWithinMiles"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	airportFullName    =    airportInterface.getFullName('KJFK')
	assert airportFullName == "JOHN F KENNEDY INTL           ", "getFullName"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	airportRunways    =    airportInterface.getAllRunways('PANC')
	assert airportRunways != None, "getAllRunways"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	runwayExits    =    airportInterface.getRunwayExits('KSFO',    'RW28R')
	assert list(runwayExits) == ['Rwy_04_001', 'Rwy_04_002', 'Rwy_04_003', 'Rwy_04_004', 'Rwy_04_005', 'Rwy_04_006', 'Rwy_04_007', 'Rwy_04_008', 'Rwy_04_009', 'Rwy_04_010', 'Rwy_04_011', 'Rwy_04_012', 'Rwy_04_013', 'Rwy_04_014', 'Rwy_04_015', 'Rwy_04_016', 'Rwy_04_017', 'Rwy_04_018'] , "getRunwayExits"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	airportLayoutNodeMap    =    airportInterface.getLayout_node_map('PHNL')
	assert airportLayoutNodeMap != None, "getLayout_node_map"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	airportLayoutNodeData    =    airportInterface    .getLayout_node_data('PHNL')
	assert airportLayoutNodeData != None, "getLayout_node_data"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	airportLayoutLinks    =    airportInterface.getLayout_links('PHNL')
	assert airportLayoutLinks != None, "getLayout_links"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	surfaceTaxiPlan    =    airportInterface.getSurface_taxi_plan('SWA1897',    'KSFO')
	assert list(surfaceTaxiPlan) == ['Gate_F_086', 'Ramp_06_011', 'Txy_A_B1', 'Txy_A_016', 'Txy_A_015', 'Txy_A_012', 'Txy_A_011', 'Txy_A_D', 'Txy_A_010', 'Txy_A_E', 'Txy_A_009', 'Txy_A_F1', 'Txy_A_008', 'Txy_A_G', 'Txy_A_007', 'Txy_A_006', 'Txy_A_005', 'Txy_A_H', 'Txy_A_004', 'Txy_A_M', 'Txy_A_003', 'Txy_A_002', 'Txy_A_A1', 'Txy_A_001', 'Rwy_02_001', 'Rwy_02_002'], "getSurface_taxi_plan"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	assert airportInterface.setUser_defined_surface_taxi_plan('SWA1898',    
	'KSFO',
	['Gate_01_001',    'Ramp_01_001',    'Txy_01_001',    'Txy_01_002',    
	'Rwy_02_001']) == 1, "setUser_defined_surface_taxi_plan"


	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	departureRunway    =    airportInterface.getDepartureRunway('SWA1897')
	assert departureRunway == "RW01R",  "getDepartureRunway"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	arrivalRunway    =    airportInterface.getArrivalRunway('SWA1897')
	assert arrivalRunway == "RW07R", "getArrivalRunway"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	airportList    =    airportInterface.getAllAirportCodesInNATS()
	assert list(airportList) == ['KABQ', 'KATL', 'KBDL', 'KBOI', 'KBOS', 'KBUR', 'KBWI', 'KCLE', 'KCLT', 'KCVG', 'KDCA', 'KDEN', 'KDFW', 'KDTW', 'KEWR', 'KGYY', 'KHPN', 'KIAD', 'KIAH', 'KISP', 'KJAX', 'KJFK', 'KLAS', 'KLAX', 'KLGA', 'KLGB', 'KMCO', 'KMDW', 'KMEM', 'KMHT', 'KMIA', 'KMSP', 'KOAK', 'KONT', 'KPBI', 'KPDK', 'KPDX', 'KPHL', 'KPHX', 'KPIT', 'KSAN', 'KSDF', 'KSFO', 'KSJC', 'KSLC', 'KSNA', 'KSTL', 'KSWF', 'KTEB', 'KTPA', 'KVGT', 'PHNL', 'PANC', 'KORD', 'KPVD', 'KSEA', 'KDAL'], "getAllAirportCodesInNATS"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	runwayEnds    =    airportInterface.getRunwayEnds('KSFO',    'RW28R')
	assert list(runwayEnds) == ['Rwy_04_001', 'Rwy_04_018'], "getRunwayEnds"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	airport    =    airportInterface.select_airport('KORD')
	airportCode    =    airport.getCode()
	assert airportCode == "KORD", "getCode"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	airport    =    airportInterface.select_airport('KSFO')
	airportElevation    =    airport.getElevation()
	assert airportElevation == 13, "getElevation"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	airport    =    airportInterface.select_airport('KORD')
	airportLatitude    =    airport.getLatitude()
	assert airportLatitude == 41.97452222222223, "getLatitude"

	airportInterface    =    environmentInterface.getAirportInterface()
	airport    =    airportInterface.select_airport('KORD')
	airportLongitude    =    airport.getLongitude()
	assert airportLongitude == -87.90659722222223, "getLongitude"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	airportInterface    =    environmentInterface.getAirportInterface()
	airport    =    airportInterface.select_airport('KORD')
	airportName    =    airport.getName()
	assert airportName == "CHICAGO O'HARE INTL           ", "getName"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =     environmentInterface.getTerminalAreaInterface()
	approaches    =    terminalAreaInterface.getAllApproaches('KORD')
	assert approaches != None, "getAllApproaches"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =     environmentInterface.getTerminalAreaInterface()
	sids    =    terminalAreaInterface.getAllSids('KORD')
	assert sids == None, "getAllSids"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =     environmentInterface.getTerminalAreaInterface()
	stars    =    terminalAreaInterface.getAllStars('KORD')
	assert stars != None, "getAllStars"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =     environmentInterface.getTerminalAreaInterface()
	currentApproach    =    terminalAreaInterface.getCurrentApproach('SWA1897')
	assert currentApproach == "I07R", "getCurrentApproach"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =     environmentInterface.getTerminalAreaInterface()
	currentSid    =    terminalAreaInterface.getCurrentSid('SWA1897')
	assert currentSid == "SSTIK4", "getCurrentSid"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =     environmentInterface.getTerminalAreaInterface()
	currentStar    =    terminalAreaInterface.getCurrentStar('SWA1897')
	assert currentStar == "HYDRR1", "getCurrentStar"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =     environmentInterface.getTerminalAreaInterface()
	sidLegNames    =    terminalAreaInterface.getProcedure_leg_names('SID',    
	'SSTIK4',    'KSFO')
	assert sidLegNames != None, "getProcedure_leg_names"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =     environmentInterface.getTerminalAreaInterface()
	waypointNames    =    terminalAreaInterface.getWaypoints_in_procedure_leg('SID',    
	'SSTIK4',    'KSFO',
	'PORTE')
	assert waypointNames != None, "getWaypoints_in_procedure_leg"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =     environmentInterface.getTerminalAreaInterface()
	waypointLocation    =    terminalAreaInterface.getWaypoint_Latitude_Longitude_deg('BOILE')
	assert waypointLocation != None, "getWaypoint_Latitude_Longitude_deg"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =     environmentInterface.getTerminalAreaInterface()
	procedureAlt1    =    terminalAreaInterface.getProcedure_alt_1('SID',    
	'SSTIK4',    'KSFO',    'PORTE',
	'KAYEX')
	assert procedureAlt1 != None, "getProcedure_alt_1"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =     environmentInterface.getTerminalAreaInterface()
	procedureAlt2    =    terminalAreaInterface.getProcedure_alt_2('SID',    
	'SSTIK4',    'KSFO',    'PORTE',    'KAYEX')
	assert procedureAlt2 != None, "getProcedure_alt_2"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =     environmentInterface.getTerminalAreaInterface()
	procedureSpeedLimit    =    terminalAreaInterface.getProcedure_speed_limit('SID',    'SSTIK3',    
	'KSFO',    'PORTE',    'KAYEX')
	assert procedureSpeedLimit != None, "getProcedure_speed_limit"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =     environmentInterface.getTerminalAreaInterface()
	procedureAltitudeDesc    =    terminalAreaInterface.getProcedure_alt_desc('SID',    'SSTIK3',    'KSFO',
	'PORTE',    'KAYEX')
	assert procedureAltitudeDesc == None, "getProcedure_alt_desc"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terminalAreaInterface    =     environmentInterface.getTerminalAreaInterface()
	procedureSpeedLimitDesc    =    terminalAreaInterface.getProcedure_speed_limit_desc    ('SID',    'SSTIK3',
	'KSFO',    'PORTE',    'KAYEX')
	assert procedureSpeedLimitDesc == None, "getProcedure_speed_limit_desc"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	terrainAreaInterface    =    environmentInterface.getTerrainInterface()
	elevation    =    terrainAreaInterface.getElevation(34.5,    -122.23)
	assert elevation == 0.0, "getElevation"


	environmentInterface    =    natsClient.getEnvironmentInterface()
	terrainAreaInterface    =    environmentInterface.getTerrainInterface()
	elevationMapBounds    =    terrainAreaInterface.getElevationMapBounds()
	assert elevationMapBounds != None, "getElevationMapBounds"

	environmentInterface    =    natsClient.getEnvironmentInterface()
	weatherInterface    =    environmentInterface.getWeatherInterface()
	#weatherInterface.downloadWeatherFiles()


	safetyMetricsInterface    =    natsClient.getSafetyMetricsInterface()
	flightsInRange    =    safetyMetricsInterface.getFlightsInRange('SWA1897')
	assert list(flightsInRange) == [], "getFlightsInRange"

	safetyMetricsInterface    =    natsClient.getSafetyMetricsInterface()
	distance    =    safetyMetricsInterface.getDistanceToRunwayThreshold    ('SWA1897')
	assert distance == 777.8214786823144, ""

	safetyMetricsInterface    =    natsClient.getSafetyMetricsInterface()
	distance    =    safetyMetricsInterface.    getDistanceToRunwayEnd    ('SWA1897')
	assert distance == 762.7762459698514, ""

	safetyMetricsInterface    =    natsClient.getSafetyMetricsInterface()
	alignmentAngle    =    safetyMetricsInterface.    getVelocityAlignmentWithRunway    ('SWA1897',    'DEPARTURE')
	assert alignmentAngle == 0.3312379743062124, ""

	safetyMetricsInterface    =    natsClient.getSafetyMetricsInterface()
	assert safetyMetricsInterface.getFlightsInWakeVortexRange('SWA1897',    200,    
	150,    400,    350,    2,    50) != None, "getFlightsInWakeVortexRange"

	safetyMetricsInterface    =    natsClient.getSafetyMetricsInterface()
	assert safetyMetricsInterface.setAircraftBookValue('SWA1897',    5.6) == 0, "setAircraftBookValue"

	safetyMetricsInterface    =    natsClient.getSafetyMetricsInterface()
	assert safetyMetricsInterface.setTouchdownPointOnRunway('SWA1897',    32.423,    
	-123.123) == 1, "setTouchdownPointOnRunway"

	safetyMetricsInterface    =    natsClient.getSafetyMetricsInterface()
	assert list(safetyMetricsInterface.getTouchdownPointOnRunway('SWA1897')) == [32.423, -123.123], "getTouchdownPointOnRunway"


	safetyMetricsInterface    =    natsClient.getSafetyMetricsInterface()
	assert safetyMetricsInterface.setTakeOffPointOnRunway('SWA1897',    37.625735, -122.368191) == 1, "setTakeOffPointOnRunway"


	safetyMetricsInterface    =    natsClient.getSafetyMetricsInterface()
	assert list(safetyMetricsInterface.getTakeOffPointOnRunway('SWA1897')) == [37.625735, -122.368191], "getTakeOffPointOnRunway"


	safetyMetricsInterface    =    natsClient.getSafetyMetricsInterface()
	assert safetyMetricsInterface.getL1Distance('KSFO', 'SWA1897', 'SWA1898') == -1, "getL1Distance"


	safetyMetricsInterface    =    natsClient.getSafetyMetricsInterface()
	assert safetyMetricsInterface.getDistanceToPavementEdge('KSFO', 'SWA1897') == -1, "getDistanceToPavementEdge"

	'''
	pilotInterface    =    entityInterface.getPilotInterface()
	assert pilotInterface.setActionRepeat('SWA1897',    'COURSE') == 1,  "setActionRepeat"

	pilotInterface    =    entityInterface.getPilotInterface()
	assert pilotInterface.skipFlightPhase('SWA1897', 'FLIGHT_PHASE_CLIMB_TO_CRUISE_ALTITUDE') == 0, "skipFlightPhase"

	pilotInterface    =    entityInterface.getPilotInterface()
	assert pilotInterface.setWrongAction('SWA1897', 'COURSE', 'AIRSPEED') == 0, "setWrongAction"


	pilotInterface    =    entityInterface.getPilotInterface()
	assert pilotInterface.setActionReversal('SWA1897',    'COURSE') == 0, "setActionReversal"


	pilotInterface    =    entityInterface.getPilotInterface()
	assert pilotInterface.setPartialAction('PLEASE_ENTER_AIRCRAFT_CALLSIGN_HERE', 'VERTICAL_SPEED',    200,    25) == 0, "setPartialAction"


	pilotInterface    =    entityInterface.getPilotInterface()
	assert pilotInterface.skipChangeAction('SWA1897',    'COURSE') == 0, "skipChangeAction"


	pilotInterface    =    entityInterface.getPilotInterface()
	assert pilotInterface.setActionLag('SWA1897',    'COURSE',    10,    0.05,    30) == 0, "setActionLag"


	pilotInterface    =    entityInterface.getPilotInterface()
	assert pilotInterface.setFlightPlanReadError('SWA1897',    'VERTICAL_SPEED', 398.0) == 0, "setFlightPlanReadError"

	groundOperatorInterface = entityInterface.getGroundOperatorInterface()
	assert groundOperatorInterface.setGroundOperatorAbsence('BUS123', 4) == 0, "setGroundOperatorAbsence"


	groundOperatorInterface = entityInterface.getGroundOperatorInterface()
	assert groundOperatorInterface.setActionRepeat('BUS123', 'SPEED') == 1, "setActionRepeat"


	groundOperatorInterface = entityInterface.getGroundOperatorInterface()
	assert groundOperatorInterface.setVehicleContact('BUS123') == 0, "setVehicleContact"


	groundOperatorInterface = entityInterface.getGroundOperatorInterface()
	assert groundOperatorInterface.setActionReversal('BUS123', 'COURSE') == 0, "setActionReversal"

	groundOperatorInterface = entityInterface.getGroundOperatorInterface()
	assert groundOperatorInterface.setPartialAction('BUS123', 'SPEED', 8, 50) == 0, "setPartialAction"


	groundOperatorInterface = entityInterface.getGroundOperatorInterface()
	assert groundOperatorInterface.setActionLag('BUS123', 'SPEED', 10, 0.5, 30) == 0, "setActionLag"
	'''
except Exception as e:
    result = 1
    pass

if result == 0:
    print("All NATS API Functions have been tested successfully.")
