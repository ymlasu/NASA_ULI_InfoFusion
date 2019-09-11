% NATS sample
%
% Optimal Synthesis Inc.
%
% Oliver Chen
% 06.26.2019
%
% Demo of Conflict Detection and Resolution during trajectory simulation

% Clear java variables in MATLAB
clear java;

env_NATS_CLIENT_HOME = getenv('NATS_CLIENT_HOME');

str_NATS_CLIENT_HOME = '';

if isempty(env_NATS_CLIENT_HOME)
    str_NATS_CLIENT_HOME = '';
else
    str_NATS_CLIENT_HOME = strcat(env_NATS_CLIENT_HOME, '/');
end

javaaddpath(strcat(str_NATS_CLIENT_HOME, 'dist/nats-client.jar'),'-end');
javaaddpath(strcat(str_NATS_CLIENT_HOME, 'dist/nats-shared.jar'),'-end');
javaaddpath(strcat(str_NATS_CLIENT_HOME, 'dist/json.jar'),'-end');
javaaddpath(strcat(str_NATS_CLIENT_HOME, 'dist/rmiio-2.1.2.jar'),'-end');
javaaddpath(strcat(str_NATS_CLIENT_HOME, 'dist/commons-logging-1.2.jar'),'-end');

% NATS simulation status definition
% You can get simulation status from the server and know what it refers to
NATS_SIMULATION_STATUS_READY = com.osi.util.Constants.NATS_SIMULATION_STATUS_READY;
NATS_SIMULATION_STATUS_START = com.osi.util.Constants.NATS_SIMULATION_STATUS_START;
NATS_SIMULATION_STATUS_PAUSE = com.osi.util.Constants.NATS_SIMULATION_STATUS_PAUSE;
NATS_SIMULATION_STATUS_RESUME = com.osi.util.Constants.NATS_SIMULATION_STATUS_RESUME;
NATS_SIMULATION_STATUS_STOP = com.osi.util.Constants.NATS_SIMULATION_STATUS_STOP;
NATS_SIMULATION_STATUS_ENDED = com.osi.util.Constants.NATS_SIMULATION_STATUS_ENDED;

NauticalMilestoFeet = 6076.12;

natsClient = NATSClientFactory.getNATSClient;
simulationInterface = natsClient.getSimulationInterface;

environmentInterface = natsClient.getEnvironmentInterface();

equipmentInterface = natsClient.getEquipmentInterface();
aircraftInterface = equipmentInterface.getAircraftInterface();

entityInterface = natsClient.getEntityInterface();
controllerInterface = entityInterface.getControllerInterface();

natsClient.login('admin');

if not(isempty(simulationInterface))
    simulationInterface.clear_trajectory();
    
    % Here the parameters specify the file and path on server.  Please don't change it.
    environmentInterface.load_rap('share/tg/rap');
    
    aircraftInterface.load_aircraft('share/tg/trx/TRX_DEMO_CDNR_v1.5.trx', 'share/tg/trx/TRX_DEMO_CDNR_mfl_v1.5.trx');
    
    simulationInterface.setupSimulation(36000, 30);
    
    % Set distance parameters of CDNR
    % These functions are optional.  The following values are default in NATS.
    % If users don't call these functions, NATS engine uses default values.
    % controllerInterface.setCDR_initiation_distance_surface(600);
    % controllerInterface.setCDR_initiation_distance_terminal(20 * NauticalMilestoFeet);
    % controllerInterface.setCDR_initiation_distance_enroute(20 * NauticalMilestoFeet);
    % controllerInterface.setCDR_separation_distance_surface(300);
    % controllerInterface.setCDR_separation_distance_terminal(7 * NauticalMilestoFeet);
    % controllerInterface.setCDR_separation_distance_enroute(10 * NauticalMilestoFeet);

    % Enable conflict detection and resolution
    controllerInterface.enableConflictDetectionAndResolution(true);

    % Start simulation for 3180 seconds
    simulationInterface.start(3180);

    while true
        server_runtime_sim_status = simulationInterface.get_runtime_sim_status();
        if (server_runtime_sim_status == NATS_SIMULATION_STATUS_PAUSE)
            break;
        else
            pause(1);
        end
    end
    
    % Result of CDR status is a 2-dimentional array
    % Array elements are: aircraft ID of the held aircraft
    %                     aircraft ID of the conflicting aircraft
    %                     seconds of holding of the held aircraft
    % Format type: [[String, String, float]]
    % Example: [["AC1", "AC_conflicting_with_AC1", heldSeconds_AC1], ["AC2", "AC_conflicting_with_AC2", heldSeconds_AC2]]
    array_cdrStatus = controllerInterface.getCDR_status();
    if not(isempty(array_cdrStatus))
        fprintf('Show CD&R Status:');
        for i = 1: size(array_cdrStatus)
            fprintf('    AC1_held = %s\n', array_cdrStatus(i, 1));
            fprintf('    AC2_conflicting_with_AC1 = %s\n', array_cdrStatus(i, 2));
            fprintf('    Seconds held of AC1 = %f\n', array_cdrStatus(i, 3));
        end
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
