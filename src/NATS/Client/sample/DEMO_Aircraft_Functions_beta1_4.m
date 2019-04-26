% Clear java variables in MATLAB
clear java;

javaaddpath('dist/nats-client.jar','-end');
javaaddpath('dist/nats-shared.jar','-end');
javaaddpath('dist/json.jar','-end');
javaaddpath('dist/rmiio-2.1.2.jar','-end');
javaaddpath('dist/commons-logging-1.2.jar','-end');

% NATS simulation status definition
% You can get simulation status from the server and know what it refers to
NATS_SIMULATION_STATUS_READY = com.osi.util.Constants.NATS_SIMULATION_STATUS_READY;
NATS_SIMULATION_STATUS_START = com.osi.util.Constants.NATS_SIMULATION_STATUS_START;
NATS_SIMULATION_STATUS_PAUSE = com.osi.util.Constants.NATS_SIMULATION_STATUS_PAUSE;
NATS_SIMULATION_STATUS_RESUME = com.osi.util.Constants.NATS_SIMULATION_STATUS_RESUME;
NATS_SIMULATION_STATUS_STOP = com.osi.util.Constants.NATS_SIMULATION_STATUS_STOP;
NATS_SIMULATION_STATUS_ENDED = com.osi.util.Constants.NATS_SIMULATION_STATUS_ENDED;

natsClient = NATSClientFactory.getNATSClient;
simulationInterface = natsClient.getSimulationInterface;

environmentInterface = natsClient.getEnvironmentInterface();

equipmentInterface = natsClient.getEquipmentInterface();
aircraftInterface = equipmentInterface.getAircraftInterface();

entityInterface = natsClient.getEntityInterface();
controllerInterface = entityInterface.getControllerInterface();
pilotInterface = entityInterface.getPilotInterface();

natsClient.login('admin');

if not(isempty(simulationInterface))
    simulationInterface.clear_trajectory();
    
    % Here the parameters specify the file and path on server.  Please don't change it.
    environmentInterface.load_rap('share/tg/rap');
    
    aircraftInterface.load_aircraft('share/tg/trx/TRX_DEMO_beta1.0_100rec.trx', 'share/tg/trx/TRX_DEMO_beta1.0_100rec_mfl.trx');

    aircraftIdArray_withinZone = aircraftInterface.getAircraftIds(30.0, 35.0, -115.0, -90.0, -1.0, -1.0);

    if ((~isempty(aircraftIdArray_withinZone)) & (size(aircraftIdArray_withinZone) > 0))
        for i = 1: size(aircraftIdArray_withinZone)
            curAcId = aircraftIdArray_withinZone(i);

            fprintf('Aircraft id in selected zone = %s\n', char(curAcId));
        end
    end
    
    disp('****************************************');

    curAircraft = aircraftInterface.select_aircraft('ULI-3AFSD3DC24');
    if ~isempty(curAircraft)
        airborne_flight_plan_waypoint_name_array = curAircraft.getFlight_plan_waypoint_name_array();

        for i = 1: (size(airborne_flight_plan_waypoint_name_array))
            fprintf('ULI-3AFSD3DC24 airborne flight plan waypoint name = %s\n', char(airborne_flight_plan_waypoint_name_array(i, 1)));
        end
    end
    
    aircraft_3E6A0495F1 = aircraftInterface.select_aircraft('ULI-3E6A0495F1');
    aircraft_3E6A0495F1.delay_departure(100); % Delay the departure time for 100 sec

    simulationInterface.setupSimulation(10000, 10);
    
    simulationInterface.start(1000);

    while true
        server_runtime_sim_status = simulationInterface.get_runtime_sim_status();
        if (server_runtime_sim_status == NATS_SIMULATION_STATUS_PAUSE)
            break;
        else
            pause(1);
        end
    end
    
    aircraft_3E6A0495F1 = aircraftInterface.select_aircraft('ULI-3E6A0495F1');
    if not(isempty(aircraft_3E6A0495F1))
        disp('****************************************');
        fprintf('ULI-3E6A0495F1 (pausing at %f', simulationInterface.get_curr_sim_time());
        fprintf(' sec, latitude = %f', aircraft_3E6A0495F1.getLatitude_deg());
        fprintf(', longitude = %f', aircraft_3E6A0495F1.getLongitude_deg());
        fprintf(', altitude = %f\n', aircraft_3E6A0495F1.getAltitude_ft());
        disp('****************************************');
    end

	simulationInterface.resume();

    % Use a while loop to constantly check server status.  When server simulation finishes, continue to output the trajectory data
    while true
        server_runtime_sim_status = simulationInterface.get_runtime_sim_status();
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

	S = dbstack();
    cur_filename = char(S(1).file);
    strIndexArray = strfind(cur_filename, '.m');

    disp('Outputting trajectory data.  Please wait....');
    fileName = sprintf('%s_%s.csv', cur_filename(1: strIndexArray(1)-1), num2str(EpochSecond));
    % The trajectory output file will be saved on NATS_Server side
    simulationInterface.write_trajectories(fileName);
    
    aircraftInterface.release_aircraft();
    environmentInterface.release_rap();
end


% Close connection from NATS Server
natsClient.disConnect();