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
    
    aircraftInterface.load_aircraft('share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx', 'share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx');

    simulationInterface.setupSimulation(11000, 30);
    
    simulationInterface.start(1020);

    % Check simulation status.  Continue to next code when it is at PAUSE status
    % !!!!
    %      Why we do this?
    %      NATS_Server and Client are running on different machines or system
    %      processes.
    %      The actuall execution time on NATS_Server is not predictable(could be fast or slow).
    %      The accurate way for NATS_Client to know the simulation status is to
    %      call simulationInterface.get_runtime_sim_status() and check its
    %      value.
    % !!!!
    while true
        server_runtime_sim_status = simulationInterface.get_runtime_sim_status();
        if (server_runtime_sim_status == NATS_SIMULATION_STATUS_PAUSE)
            break;
        else
            pause(1);
        end
    end
    
    curAircraft = aircraftInterface.select_aircraft('SWA1897');
    
    % Set new state value
    % curAircraft.setCruise_tas_knots(450);
    % curAircraft.setCruise_alt_ft(35000);
    
    curAircraft.setLatitude_deg(36.0);
    curAircraft.setLongitude_deg(-120.0);

	simulationInterface.resume(7110);

    while true
        server_runtime_sim_status = simulationInterface.get_runtime_sim_status();
        if (server_runtime_sim_status == NATS_SIMULATION_STATUS_PAUSE)
            break;
        else
            pause(1);
        end
    end
    
    curAircraft = aircraftInterface.select_aircraft('SWA1897');
    
    % Set new state value
    % curAircraft.setCruise_tas_knots(450);
    % curAircraft.setCruise_alt_ft(35000);
    
    curAircraft.setLatitude_deg(36.0);
    curAircraft.setLongitude_deg(-120.0);
    curAircraft.setAltitude_ft(32000.0);
    curAircraft.setTas_knots(400.0);
    curAircraft.setCourse_rad(110.0 * 3.1415926 / 180);
    curAircraft.setRocd_fps(50.0);
    
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