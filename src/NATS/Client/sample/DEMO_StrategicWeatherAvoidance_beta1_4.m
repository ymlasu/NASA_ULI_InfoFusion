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
weatherInterface = environmentInterface.getWeatherInterface();

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
    
    aircraftInterface.load_aircraft('share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx', 'share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx');

    simulationInterface.setupSimulation(11000, 30);
    
    % Set polygon file for Strategic Weather Avoidance
    % Detail path and filename are required if you would like to use a specific file.  Example: share/rg/polygons/YYYYMMDD_HHMMSS.dat
    %
    % If inputing '', NATS engine will look for the latest file with name format YYYYMMDD_HHMMSS.dat
    %
    % Notice!!!!
    % If Sigmet file is used, polygon file will be ignored
    controllerInterface.setStrategicWeatherAvoidance_polygonFile('share/rg/polygons/MACS_scenario.dat');
    %controllerInterface.setStrategicWeatherAvoidance_polygonFile('') % NATS automatically pick latest file
    %controllerInterface.setStrategicWeatherAvoidance_polygonFile('NONE') % Disable file
    
    % Set sigmet file for Strategic Weather Avoidance
    % Detail path and filename are required if you would like to use a specific file.  Example: share/rg/polygons/YYYYMMDD_HHMMSS.dat
    %
    % If inputing '', NATS engine will look for the latest file with name format YYYYMMDD_HHMMSS.sigmet
    %
    % Notice!!!!
    % If Sigmet file is used, polygon file will be ignored
    %controllerInterface.setStrategicWeatherAvoidance_sigmetFile('') % NATS automatically pick latest file
    %controllerInterface.setStrategicWeatherAvoidance_sigmetFile('NONE') % Disable file
    
    % Enable strategic weather avoidance capability
    % This function must be called before setting up simulation so NATS Server can load required database files.
    controllerInterface.enableStrategicWeatherAvoidance(true);
    
    
    simulationInterface.start();

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