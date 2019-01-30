%{
NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
Copyright 2018 by Optimal Synthesis Inc. All rights reserved

for version beta 1.2

Author: Oliver Chen
Date: 2019-01-08
%}

javaaddpath('dist/nats-client.jar','-end');
javaaddpath('dist/nats-shared.jar','-end');

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
    
    aircraftInterface.load_aircraft('share/tg/trx/TRX_DEMO_beta1.0_100rec.trx', 'share/tg/trx/TRX_DEMO_beta1.0_100rec_mfl.trx');
    
    if not(isempty(aircraftInterface))
        allAircraftIdArray = aircraftInterface.getAllAircraftId();
        if not(isempty(allAircraftIdArray))
            for i = 1: (size(allAircraftIdArray))
                curAcId = allAircraftIdArray(i, 1);
                %fprintf('All aircraft --> Current acid = %s\n', char(curAcId));
            end
        end
    end
    
    sim.setupSimulation(13000, 1);
    
    %sim.start();
    sim.start(600);

    while true
        server_runtime_sim_status = sim.get_runtime_sim_status();
        if (server_runtime_sim_status == NATS_SIMULATION_STATUS_PAUSE)
            break;
        else
            pause(1);
        end
    end
    
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
            
        else
            disp('Sample_Matlab --> Server sim status not running');
        end
    end
    
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

natsClient.disConnect();