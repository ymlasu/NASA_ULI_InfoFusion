%{
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Hari Iyer
Date: 08/20/2018
%}

%Clear Garbage Variables/Objects and set NATS Distribution Path
clear all;
javaaddpath('dist/nats-client.jar','-end');
javaaddpath('dist/nats-shared.jar','-end');

%NATS Server location (eg. /home/user/NATS/NATS_Server)
NATS_Server = 'NATS_SERVER_LOCATION_HERE';

% NATS Server Status definition
NATS_SIMULATION_STATUS_ENDED = com.osi.util.Constants.NATS_SIMULATION_STATUS_ENDED;

%NATS Client Interface definition
natsClient = NATSClientFactory.getNATSClient();
simulation = natsClient.getSimulationInterface();
equipmentInterface = natsClient.getEquipmentInterface();
aircraftInterface = equipmentInterface.getAircraftInterface();
environmentInterface = natsClient.getEnvironmentInterface();

%Attribute to perturb
%PERTURB_ATTRIBUTES = ['CRUISE_TAS', 'ALTITUDE', 'LATITUDE_AND_LONGITUDE', 'LONGITUDE', 'LATITUDE'];
PERTURB_ATTRIBUTES = ['CRUISE_TAS', 'ALTITUDE', 'LATITUDE_AND_LONGITUDE'];

%Monte-Carlo Simulation setup for perturbing altitude (feet)
%Set aircraft name under simulation
aircraftID = 'AIRCRAFT_CALLSIGN_HERE';
meanCruiseAltitude = 35000;
sampleSize = 10;
cruiseAltitudeVector = meanCruiseAltitude + 1000*randn(sampleSize,1);

%Monte-Carlo Simulation setup for perturbing cruise true air speed (knots)
%Set aircraft name under simulation
aircraftID = 'AIRCRAFT_CALLSIGN_HERE';
meanCruiseSpeed = 450;
sampleSize = 10;
cruiseSpeedVector = meanCruiseSpeed + 10*randn(sampleSize,1);

%Monte-Carlo Simulation setup for perturbing geo coordinates (latitude and longitude)
%Set aircraft name under simulation
aircraftID = 'AIRCRAFT_CALLSIGN_HERE';
waypointIndex = 8;
meanLatitude = 34.422439;
meanLongitude = -118.025853;
sampleSize = 10;
latitudeVector = meanLatitude + 0.1*randn(sampleSize,1);
longitudeVector = meanLongitude + 0.1*randn(sampleSize,1);

%{
%Monte-Carlo Simulation setup for perturbing geo coordinates (latitude)
%Set aircraft name under simulation
aircraftID = 'AIRCRAFT_CALLSIGN_HERE';
waypointIndex = 8;
meanLatitude = 34.422439;
sampleSize = 10;
latitudeVector = meanLatitude + 0.1*randn(sampleSize,1);

%Monte-Carlo Simulation setup for perturbing geo coordinates (longitude)
%Set aircraft name under simulation
aircraftID = 'AIRCRAFT_CALLSIGN_HERE';
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
    
    %Initialize aircraft with parameters depending on attributes to be perturbed
    aircraft = aircraftInterface.select_aircraft(aircraftID);
    
    if (ismember('CRUISE_TAS',PERTURB_ATTRIBUTES))
        aircraft.setCruise_tas_knots(cruiseSpeedVector(count));
    end
    if (ismember('ALTITUDE',PERTURB_ATTRIBUTES))
        aircraft.setCruise_alt_ft(cruiseAltitudeVector(count));
    end
    if (ismember('LATITUDE',PERTURB_ATTRIBUTES))
       aircraft.setFlight_plan_latitude_deg(waypointIndex, latitudeVector(count));
    end
    if (ismember('LONGITUDE',PERTURB_ATTRIBUTES))
       aircraft.setFlight_plan_longitude_deg(waypointIndex, longitudeVector(count));
    end
    if (ismember('LATITUDE_AND_LONGITUDE',PERTURB_ATTRIBUTES))
       aircraft.setFlight_plan_latitude_deg(waypointIndex, latitudeVector(count));
       aircraft.setFlight_plan_longitude_deg(waypointIndex, longitudeVector(count));
    end
    %Set up simulation (Versions of setupSimulation can be found in the
    %documentation)
    aircraftInterface.synchronize_aircraft_to_server(aircraft);
    simulation.setupSimulation(11000.0, 5.0, 5.0, 30.0);

    %Start simulation to go through till end
    simulation.start();
    
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
            pause(0.5);
        end
    end

    %Clear simulation data for next iteration
    aircraftInterface.release_aircraft();
    pause(2.5);
    environmentInterface.release_rap();
    pause(2.5);
    
end
