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
simulationInterface = natsClient.getSimulationInterface;

environmentInterface = natsClient.getEnvironmentInterface();
airportInterface = environmentInterface.getAirportInterface();
terminalAreaInterface = environmentInterface.getTerminalAreaInterface();

equipmentInterface = natsClient.getEquipmentInterface();
aircraftInterface = equipmentInterface.getAircraftInterface();

entityInterface = natsClient.getEntityInterface();
controllerInterface = entityInterface.getControllerInterface();
pilotInterface = entityInterface.getPilotInterface();

if not(isempty(simulationInterface))
    simulationInterface.clear_trajectory();
    
    % Here the parameters specify the file and path on server.  Please don't change it.
    environmentInterface.load_rap('share/tg/rap');
    
    aircraftInterface.load_aircraft('share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx', 'share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx');

    airportName = airportInterface.getFullName('KSFO');
    fprintf('Airport Full Name = %s\n', char(airportName));

    disp('************************************************');

    runways = airportInterface.getAllRunways('KSFO');
    if ~isempty(runways)
        for j = 1 : size(runways)
            fprintf('KSFO --> Runway = %s, waypoing id = %s\n', runways(j, 1), runways(j, 2));
        end
    else
        disp('No runway data');
    end

    disp('************************************************');

    allSids = terminalAreaInterface.getAllSids('KSFO');
    if ~isempty(allSids)
        for j = 1 : size(allSids)
            fprintf('KSFO --> avail sid = %s\n', char(allSids(j, 1)));
        end
    end
    
    disp('************************************************');
    
    allStars = terminalAreaInterface.getAllStars('KSFO');
    if ~isempty(allStars)
        for j = 1 : size(allStars)
            fprintf('KSFO --> avail star = %s\n', char(allStars(j, 1)));
        end
    end
    
    disp('************************************************');
    
    allApproaches = terminalAreaInterface.getAllApproaches('KSFO');
    if ~isempty(allApproaches)
        for j = 1 : size(allApproaches)
            fprintf('KSFO --> avail approach = %s\n', char(allApproaches(j, 1)));
        end
    end
            
    disp('************************************************');
    
    departureRunway = airportInterface.getDepartureRunway('SWA1897');
    fprintf('departureRunway = %s\n', char(departureRunway));
 
    arrivalRunway = airportInterface.getArrivalRunway('SWA1897');
    fprintf('arrivalRunway = %s\n', char(arrivalRunway));

    disp('************************************************');
    
    % Calculate a route from point A to B
    % The resulted route is not loaded in NATS.  It only outputs the array of waypoint ids.
    design_taxi_plan_KSFO = airportInterface.get_taxi_route_from_A_To_B('SWA1897', 'KSFO', 'Gate_F_086', 'Rwy_02_002');
    if ~isempty(design_taxi_plan_KSFO)
        for i = 1 : size(design_taxi_plan_KSFO)
            fprintf('design_taxi_plan_KSFO waypoint id = %s\n', char(design_taxi_plan_KSFO(i, 1)));
        end
    end
    
    disp('************************************************');

    % Calculate a route from point A to B
    % The resulted route is not loaded in NATS.  It only outputs the array of waypoint ids.
    design_taxi_plan_KPHX = airportInterface.get_taxi_route_from_A_To_B('SWA1897', 'KPHX', 'Rwy_03_009', 'Gate_04_C16');
    if ~isempty(design_taxi_plan_KSFO)
        for i = 1 : size(design_taxi_plan_KPHX)
            fprintf('design_taxi_plan_KPHX waypoint id = %s\n', char(design_taxi_plan_KPHX(i, 1)));
        end
    end

    aircraftInterface.release_aircraft();
    environmentInterface.release_rap();
end

% Close connection from NATS Server
natsClient.disConnect();