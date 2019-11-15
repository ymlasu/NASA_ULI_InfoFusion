try:
    from jpype import startJVM,getDefaultJVMPath,JPackage,JClass,shutdownJVM
except ImportError:
    pass
from pathlib import Path
import os

#------------PUT THE FOLLOWING IN EACH PROGRAM--------------------

client = str(Path(__file__).parent)+'/'
os.environ['NATS_CLIENT_HOME'] = client

classpath = client+"dist/nats-client.jar:"+client+"dist/nats-shared.jar:"+client+"dist/rmiio-2.1.2.jar:"+client+"dist/json.jar"

startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % classpath)

'''This class initializes the NATS client.'''
class NATS_Config:
    def __init__(self, duration = 86400,
                 interval = 1,
                 client_dir = client,
                 wind_dir = 'share/tg/rap',
                 track_file = "share/tg/trx/swim_example_aug.trx",
                 max_flt_lev_file = "share/tg/trx/swim_example_mfl.trx"):
        self.endTime = duration
        self.interval = interval
        self.initializeJVM(client_dir)
        self.wind_dir = wind_dir
        self.trx_file = track_file
        self.mfl_file = max_flt_lev_file

    '''Initialize the NATS client'''
    def initializeJVM(self, client_dir = client):

        self.NATS_SIMULATION_STATUS_ENDED = NATS_SIMULATION_STATUS_ENDED;
        NATSClientFactory = JClass('NATSClientFactory')
        self.natsClient = NATSClientFactory.getNATSClient()

        self.equipmentInterface = self.natsClient.getEquipmentInterface()

        # Get EnvironmentInterface
        self.environmentInterface = self.natsClient.getEnvironmentInterface()
        # Get AirportInterface
        self.airportInterface = self.environmentInterface.getAirportInterface()
        # Get TerminalAreaInterface
        self.terminalAreaInterface = self.environmentInterface.getTerminalAreaInterface()

        self.sim = self.natsClient.getSimulationInterface()

        self.aircraftInterface = self.equipmentInterface.getAircraftInterface()

        self.entityInterface = self.natsClient.getEntityInterface()

        self.controllerInterface = self.entityInterface.getControllerInterface()
        
        self.pilotInterface = self.entityInterface.getPilotInterface()

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

# Aircraft clearance definition
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
