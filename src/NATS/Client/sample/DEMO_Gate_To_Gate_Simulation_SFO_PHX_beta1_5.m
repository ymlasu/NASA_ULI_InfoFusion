% NATS sample
%
% Optimal Synthesis Inc.
%
% Oliver Chen
% 06.25.2019
%
% Demo of gate-to-gate trajectory simulation.
%
% The aircraft starts from the origin gate, goes through departing taxi plan, takes off, goes through different flight phases to the destination airport, and finally reaches the destination gate.

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
    
    % Controller to set human error: delay time
    % controllerInterface.setDelayPeriod("SWA1897", AIRCRAFT_CLEARANCE_PUSHBACK, 7);
    % controllerInterface.setDelayPeriod("SWA1897", AIRCRAFT_CLEARANCE_TAKEOFF, 20);

    simulationInterface.setupSimulation(11000, 30);
    
    simulationInterface.start(600);

    while true
        server_runtime_sim_status = simulationInterface.get_runtime_sim_status();
        if (server_runtime_sim_status == NATS_SIMULATION_STATUS_PAUSE)
            break;
        else
            pause(1);
        end
    end
    
    % pilotInterface.skipFlightPhase('SWA1897', 'FLIGHT_PHASE_CLIMB_TO_CRUISE_ALTITUDE');
    % pilotInterface.setActionRepeat('SWA1897', "VERTICAL_SPEED");
    % pilotInterface.setWrongAction('SWA1897', "AIRSPEED", "FLIGHT_LEVEL");
    % pilotInterface.setActionReversal('SWA1897', 'VERTICAL_SPEED');
    % pilotInterface.setPartialAction('SWA1897', 'COURSE', 200, 50);
    % pilotInterface.skipChangeAction('SWA1897', 'COURSE');
    pilotInterface.setActionLag('SWA1897', 'COURSE', 10, 0.05, 60);

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
