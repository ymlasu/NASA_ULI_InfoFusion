%{
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Hari Iyer
Date: 01/04/2019
%}

%Clear Garbage Variables/Objects and set NATS Distribution Path
clear all;

javaaddpath('dist/nats-client.jar','-end');
javaaddpath('dist/nats-shared.jar','-end');

%Enter NATS Server location
NATS_Server = 'PLEASE_ENTER_NATS_SERVER_LOCATION_HERE';

fprintf('This module illustrates a Monte Carlo Simulation template to observe changes to flight trajectory when functions affecting ground parameters are used to perturb flight parameters.\nGraphs for vital flight parameters are plotted after the simulation runs through.\n');

% Aircraft Clearance variables
AIRCRAFT_CLEARANCE_PUSHBACK = com.osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_PUSHBACK;
AIRCRAFT_CLEARANCE_TAXI_DEPARTING = com.osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_TAXI_DEPARTING;
AIRCRAFT_CLEARANCE_TAKEOFF = com.osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_TAKEOFF;
AIRCRAFT_CLEARANCE_ENTER_ARTC = com.osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_ENTER_ARTC;
AIRCRAFT_CLEARANCE_DESCENT_FROM_CRUISE = com.osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_DESCENT_FROM_CRUISE;
AIRCRAFT_CLEARANCE_ENTER_TRACON = com.osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_ENTER_TRACON;
AIRCRAFT_CLEARANCE_APPROACH = com.osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_APPROACH;
AIRCRAFT_CLEARANCE_TOUCHDOWN = com.osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_TOUCHDOWN;
AIRCRAFT_CLEARANCE_TAXI_LANDING = com.osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_TAXI_LANDING;
AIRCRAFT_CLEARANCE_RAMP_LANDING = com.osi.util.AircraftClearance.AIRCRAFT_CLEARANCE_RAMP_LANDING;

% NATS simulation status definition
% You can get simulation status from the server and know what it refers to
NATS_SIMULATION_STATUS_READY = com.osi.util.Constants.NATS_SIMULATION_STATUS_READY;
NATS_SIMULATION_STATUS_START = com.osi.util.Constants.NATS_SIMULATION_STATUS_START;
NATS_SIMULATION_STATUS_PAUSE = com.osi.util.Constants.NATS_SIMULATION_STATUS_PAUSE;
NATS_SIMULATION_STATUS_RESUME = com.osi.util.Constants.NATS_SIMULATION_STATUS_RESUME;
NATS_SIMULATION_STATUS_STOP = com.osi.util.Constants.NATS_SIMULATION_STATUS_STOP;
NATS_SIMULATION_STATUS_ENDED = com.osi.util.Constants.NATS_SIMULATION_STATUS_ENDED;

%NATS Client Interface definition
natsClient = NATSClientFactory.getNATSClient();
simulation = natsClient.getSimulationInterface();
equipmentInterface = natsClient.getEquipmentInterface();
entityInterface = natsClient.getEntityInterface();
aircraftInterface = equipmentInterface.getAircraftInterface();
environmentInterface = natsClient.getEnvironmentInterface();
airportInterface = environmentInterface.getAirportInterface();
pilotInterface = entityInterface.getPilotInterface();
controllerInterface = entityInterface.getControllerInterface();

%Flight parameters to perturb, any of the following attributes can be inserted.
%PERTURB_ATTRIBUTES = {'AIRSPEED', 'ALTITUDE', 'WAYPOINT_LATITUDE_AND_LONGITUDE', 'WAYPOINT_LONGITUDE', 'WAYPOINT_LATITUDE', 'CURRENT_LATITUDE', 'CURRENT_LONGITUDE', 'CURRENT_LATITUDE_AND_LONGITUDE'};
PERTURB_ATTRIBUTES = {'CURRENT_LATITUDE_AND_LONGITUDE'};

%{
%Monte-Carlo Simulation setup for perturbing altitude (feet)
%Please enter target aircraft callsign here. SWA1897 is an example.
aircraftID = 'SWA1897';
meanAltitude = 25000;
sampleSize = 10;
altitudeVector = meanAltitude + 1000*randn(sampleSize,1);

%Monte-Carlo Simulation setup for perturbing true air speed (knots)
%Please enter target aircraft callsign here. SWA1897 is an example.
aircraftID = 'SWA1897';
meanAirspeedSpeed = 450;
sampleSize = 10;
airspeedVector = meanAirspeedSpeed + 10*randn(sampleSize,1);

%Monte-Carlo Simulation setup for perturbing geo coordinates (latitude and longitude)
%Please enter target aircraft callsign here. SWA1897 is an example.
aircraftID = 'SWA1897';
meanCourse = 3.14;
sampleSize = 10;
courseVector = meanCourse + 0.1*randn(sampleSize,1);

%Monte-Carlo Simulation setup for perturbing geo coordinates (latitude and longitude)
%Please enter target aircraft callsign here. SWA1897 is an example.
aircraftID = 'SWA1897';
meanRocd = 25;
sampleSize = 10;
rocdVector = meanRocd + randn(sampleSize,1);
%}

%Monte-Carlo Simulation setup for perturbing geo coordinates (latitude and longitude)
%Please enter target aircraft callsign here. SWA1897 is an example.
aircraftID = 'SWA1897';
waypointIndex = 8;
meanLatitude = 34.422439;
meanLongitude = -118.025853;
sampleSize = 10;
latitudeVector = meanLatitude + 0.1*randn(sampleSize,1);
longitudeVector = meanLongitude + 0.1*randn(sampleSize,1);


%{
%Monte-Carlo Simulation setup for perturbing geo coordinates (latitude)
%Please enter target aircraft callsign here. SWA1897 is an example.
aircraftID = 'SWA1897';
waypointIndex = 8;
meanLatitude = 34.422439;
sampleSize = 10;
latitudeVector = meanLatitude + 0.1*randn(sampleSize,1);

%Monte-Carlo Simulation setup for perturbing geo coordinates (longitude)
%Please enter target aircraft callsign here. SWA1897 is an example.
aircraftID = 'SWA1897';
waypointIndex = 8;
meanLongitude = -118.025853;
sampleSize = 10;
longitudeVector = meanLongitude + 0.1*randn(sampleSize,1);
%}

%Monte-Carlo Simulation
for count = 1:sampleSize
    %Clear Trajectory data from previous iteration
    simulation.clear_trajectory();
    
    %Load/Reload wind and flight data since trajectory data had to be cleared from previous iteration
    environmentInterface.load_rap('share/tg/rap');
    aircraftInterface.load_aircraft('share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx', 'share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx');
    
    %Set up simulation (Versions of setupSimulation can be found in the
    %documentation)
    simulation.setupSimulation(11000, 30);
    %Start simulation to go through till 1000 seconds. This time can be
    %changed, and the simulation would pause at the provided time.
    simulation.start(1000.0);
    
    %Wait for simulation to pause
    while 1
        serverStatus = simulation.get_runtime_sim_status();
        if (serverStatus ~= NATS_SIMULATION_STATUS_PAUSE)
           pause(1);
        else
            break;
        end
    end
    
    %Get current state of aircraft
    aircraft = aircraftInterface.select_aircraft(aircraftID);
    
    if (ismember('AIRSPEED',PERTURB_ATTRIBUTES))
        %aircraft.getTas_knots();
        aircraft.setTas_knots(airspeedVector(count));
    end
    if (ismember('ALTITUDE',PERTURB_ATTRIBUTES))
        %aircraft.getAltitude_ft();
        aircraft.setAltitude_ft(altitudeVector(count));
    end
    if (ismember('WAYPOINT_LATITUDE',PERTURB_ATTRIBUTES))
        aircraft.setFlight_plan_latitude_deg(waypointIndex, latitudeVector(count));
    end
    if (ismember('WAYPOINT_LONGITUDE',PERTURB_ATTRIBUTES))
       aircraft.setFlight_plan_longitude_deg(waypointIndex, longitudeVector(count));
    end
    if (ismember('WAYPOINT_LATITUDE_AND_LONGITUDE',PERTURB_ATTRIBUTES))
       aircraft.setFlight_plan_latitude_deg(waypointIndex,  latitudeVector(count));
       aircraft.setFlight_plan_longitude_deg(waypointIndex, longitudeVector(count));
    end

    if (ismember('CURRENT_LATITUDE',PERTURB_ATTRIBUTES))
       %aircraft.getLatitude_deg();
       aircraft.setLatitude_deg(latitudeVector(count));
    end
    if (ismember('CURRENT_LONGITUDE',PERTURB_ATTRIBUTES))
       %aircraft.getLongitude_deg();
        aircraft.setLongitude_deg(longitudeVector(count));
    end
    if (ismember('CURRENT_LATITUDE_AND_LONGITUDE',PERTURB_ATTRIBUTES))
        aircraft.setLatitude_deg(latitudeVector(count));
        aircraft.setLongitude_deg(longitudeVector(count));
    end
    
    %Functions for aircraft ground operation parameters have been listed here.
    %Similarly, other attributes can also be perturbed.
    %THESE PERTURBATIONS MIGHT LEAD TO ERRONEOUS FLIGHT SIMULATION RESULTS
    %airportInterface.setTaxi_tas_knots('SWA1897', 20);
    %aircraft.setCourse_rad(1.54);
    aircraft.setLatitude_deg(latitudeVector(count));
    aircraft.setLongitude_deg(longitudeVector(count));

    simulation.resume();
    
    %Wait for simulation to get done  
    while 1
        serverStatus = simulation.get_runtime_sim_status();
        if (serverStatus ~= NATS_SIMULATION_STATUS_ENDED)
           pause(1);
        else
            break;
        end
    end
   
    %Generating and saving new trajectory
    trajectoryFile = sprintf([char(aircraft.getAcid()) '-Monte-Carlo-Sim-Trajectory_%s.csv'], num2str(count));
    simulation.write_trajectories(['share/mcSimulation/' trajectoryFile]);

    %Wait for updated trajectory to get written
    while true
        if ~isempty(dir([NATS_Server '/share/mcSimulation/',trajectoryFile]))
            break;
        else
            pause(1);
        end
    end

    %Clear simulation data for next iteration
    aircraftInterface.release_aircraft();
    pause(1.5);
    environmentInterface.release_rap();
    pause(1.5);
    
end
natsClient.disConnect()

%Graph plotting routine invoked for visualizing vital flight parameter data 
PlotGraph(aircraftID, sampleSize, 'MATLAB', NATS_Server);
