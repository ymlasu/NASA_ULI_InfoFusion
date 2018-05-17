%{
NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
Copyright 2018 by Optimal Synthesis Inc. All rights reserved

Author: Oliver Chen
Date: 2017-01-19
%}

javaaddpath('dist/nats-client.jar','-end');
javaaddpath('dist/nats-shared.jar','-end');

% Flight mode value definition
% You can detect and know the flight mode by checking its value
FLIGHT_MODE_PREDEPARTURE = com.osi.util.Constants.FLIGHT_MODE_PREDEPARTURE;
FLIGHT_MODE_CLIMB = com.osi.util.Constants.FLIGHT_MODE_CLIMB;
FLIGHT_MODE_CRUISE = com.osi.util.Constants.FLIGHT_MODE_CRUISE;
FLIGHT_MODE_DESCENT = com.osi.util.Constants.FLIGHT_MODE_DESCENT;
FLIGHT_MODE_LANDED = com.osi.util.Constants.FLIGHT_MODE_LANDED;
FLIGHT_MODE_HOLDING = com.osi.util.Constants.FLIGHT_MODE_HOLDING;
FLIGHT_MODE_GROUND_DEPARTING = com.osi.util.Constants.FLIGHT_MODE_GROUND_DEPARTING;
FLIGHT_MODE_GROUND_LANDING = com.osi.util.Constants.FLIGHT_MODE_GROUND_LANDING;

% NATS simulation status definition
% You can get simulation status from the server and know what it refers to
NATS_SIMULATION_STATUS_READY = com.osi.util.Constants.NATS_SIMULATION_STATUS_READY;
NATS_SIMULATION_STATUS_START = com.osi.util.Constants.NATS_SIMULATION_STATUS_START;
NATS_SIMULATION_STATUS_PAUSE = com.osi.util.Constants.NATS_SIMULATION_STATUS_PAUSE;
NATS_SIMULATION_STATUS_RESUME = com.osi.util.Constants.NATS_SIMULATION_STATUS_RESUME;
NATS_SIMULATION_STATUS_STOP = com.osi.util.Constants.NATS_SIMULATION_STATUS_STOP;
NATS_SIMULATION_STATUS_ENDED = com.osi.util.Constants.NATS_SIMULATION_STATUS_ENDED;


natsClient = NATSClientFactory.getNATSClient;
sim = natsClient.getSimulationInterface;

environmentInterface = natsClient.getEnvironmentInterface();

equipmentInterface = natsClient.getEquipmentInterface();
aircraftInterface = equipmentInterface.getAircraftInterface();

if not(isempty(sim))
    sim.clear_trajectory();
    
    % Here the parameters specify the file and path on server.  Please don't change it.
    environmentInterface.load_rap('share/tg/rap');
    aircraftInterface.load_aircraft('share/tg/trx/TRX_07132005_noduplicates_cut_crypted.trx', 'share/tg/trx/TRX_07132005_noduplicatesOSIMaxFltLvl_cut_crypted.trx');
    
    if not(isempty(aircraftInterface))
        allAircraftIdArray = aircraftInterface.getAllAircraftId();
        if not(isempty(allAircraftIdArray))
            for i = 1: (size(allAircraftIdArray))
                curAcId = allAircraftIdArray(i, 1);
                %fprintf('All aircraft --> Current acid = %s\n', char(curAcId));
            end
        end
    end
    
    sim.setupSimulation(7200, 1); % We set 7200 seconds
    
    %sim.start();
    sim.start(600);
    pause(1);
    
    %sim.pause(); % When using sim.start(N) or sim.resume(N), this sim.pause() is not required.
    if not(isempty(aircraftInterface))
        server_runtime_sim_status = sim.get_runtime_sim_status();
        if ((server_runtime_sim_status ~= NATS_SIMULATION_STATUS_READY) && (server_runtime_sim_status ~= NATS_SIMULATION_STATUS_STOP))
        	% Obtain all aircraft ids
            allAircraftIdArray = aircraftInterface.getAllAircraftId();
            if not(isempty(allAircraftIdArray))
                %fprintf('Length of allAircraftIdArray = %d\n', size(allAircraftIdArray));
                for i = 1: (size(allAircraftIdArray))
                    curAcId = allAircraftIdArray(i, 1);
                    curAircraft = aircraftInterface.select_aircraft(curAcId);
                    fprintf('Sample_Matlab --> Aircraft Id = %s, latitude_deg = %f, longitude_deg = %f, altitude_ft = %f\n', char(curAcId), curAircraft.getLatitude_deg(), curAircraft.getLongitude_deg(), curAircraft.getAltitude_ft());
                end
            else
                disp('Sample_Matlab --> allAircraftIdArray is empty');
            end

            % Collect qualified aircraft Id array by setting latitude, longitude and/or altitude parameters
            collectedAircraftIdArray = aircraftInterface.getAircraftIds(30.0, 35.0, -100.0, -90.0, -1.0, -1.0);
            if not(isempty(collectedAircraftIdArray))
                fprintf('Length of collectedAircraftIdArray = %d\n', size(collectedAircraftIdArray));
                for i = 1: (size(collectedAircraftIdArray))
                    curAcId = collectedAircraftIdArray(i, 1);
                    fprintf('Collected Aircraft Id = %s\n', char(curAcId));
                end
            else
                disp('Sample_Matlab --> collectedAircraftIdArray is empty');
            end
            
            % Manually select an aircraft and modify value
			curAircraft = aircraftInterface.select_aircraft('ULI16-33855');
            if not(isempty(curAircraft))
                curAircraft.setAltitude_ft(36000.0);
            else
                disp('Sample_Matlab --> curAircraft is empty');
            end
        else
            disp('Sample_Matlab --> Server sim status not running');
        end
    end
    
    sim.resume(500);
    pause(2);
    
    sim.resume(); % Be sure to have a resume command to avoid infinite loop on NATS_Server
    % Use a while loop to constantly check server status.  When server simulation finishes, continue to output the trajectory data
    while true
        server_runtime_sim_status = sim.get_runtime_sim_status();
        if (server_runtime_sim_status == NATS_SIMULATION_STATUS_ENDED)
            break;
        else
            pause(1);
        end
    end
    
    % Format epoch time string
    millis = datestr(now, 'yyyymmdd HHMMSS');
    InputDate = datenum(millis, 'yyyymmdd HHMMSS');
    UnixOrigin = datenum('19700101 000000', 'yyyymmdd HHMMSS');
    EpochSecond = round((InputDate-UnixOrigin)*86400000);

    disp('Outputting trajectory data.  Please wait....');
    fileName = sprintf('MATLAB_output_trajectory_%s.csv', num2str(EpochSecond));
    % The trajectory output file will be saved on NATS_Server side
    sim.write_trajectories(fileName);
    
    aircraftInterface.release_aircraft();
    environmentInterface.release_rap();
end
