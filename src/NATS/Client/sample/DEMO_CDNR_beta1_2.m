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

NauticalMilestoFeet = 6076.12;

natsClient = NATSClientFactory.getNATSClient;
simulationInterface = natsClient.getSimulationInterface;

environmentInterface = natsClient.getEnvironmentInterface();

equipmentInterface = natsClient.getEquipmentInterface();
aircraftInterface = equipmentInterface.getAircraftInterface();

if not(isempty(simulationInterface))
    simulationInterface.clear_trajectory();
    
    % Here the parameters specify the file and path on server.  Please don't change it.
    environmentInterface.load_rap('share/tg/rap');
    
    aircraftInterface.load_aircraft('share/tg/trx/TRX_DEMO_CDNR.trx', 'share/tg/trx/TRX_DEMO_CDNR_mfl.trx');
    
    simulationInterface.setupSimulation(11000, 30);
    
    % Set distance parameters of CDNR
    % These functions are optional.  The following values are default in NATS.
    % If users don't call these functions, NATS engine uses default values.
    % simulationInterface.setCDNR_distance_of_regard_ft_surface(600);
    % simulationInterface.setCDNR_distance_of_regard_ft_terminal(10 * NauticalMilestoFeet);
    % simulationInterface.setCDNR_distance_of_regard_ft_enroute(10 * NauticalMilestoFeet);
    % simulationInterface.setCDNR_distance_of_resolve_ft_surface(300);
    % simulationInterface.setCDNR_distance_of_resolve_ft_terminal(3 * NauticalMilestoFeet);
    % simulationInterface.setCDNR_distance_of_resolve_ft_enroute(5 * NauticalMilestoFeet);

    % Enable conflict detection and resolution
    simulationInterface.enableConflictDetectionAndResolution(true);

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
