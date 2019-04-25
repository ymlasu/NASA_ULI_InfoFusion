//{
//            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
//          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
//          
//Author: Hari Iyer
//Date: 02/07/2019
//
//Update: 03/26/2019  Oliver Chen
//}

warning('off');

//Please enter NATS Client and NATS Server locations here
NATS_Client = 'PLEASE_ENTER_NATS_CLIENT_LOCATION_HERE';
NATS_Server = 'PLEASE_ENTER_NATS_SERVER_LOCATION_HERE';

if (~isdir(NATS_Server)) then
    disp("Directory NATS_Server does not exist");
elseif (~isdir(NATS_Client)) then
    disp("Directory NATS_Client does not exist");
else
    chdir(NATS_Client);
    
    javaclasspath(NATS_Client + '/dist/nats-client.jar');
    javaclasspath(NATS_Client + '/dist/nats-shared.jar');
    javaclasspath(NATS_Client + '/dist/json.jar');
    javaclasspath(NATS_Client + '/dist/rmiio-2.1.2.jar');
    javaclasspath(NATS_Client + '/dist/commons-logging-1.2.jar');
    
    SimulationStatus = jimport('com.osi.util.Constants', %f);
    AircraftClearance = jimport('com.osi.util.AircraftClearance', %f);
    NATSClientFactory = jimport('NATSClientFactory', %f);
    
    //Aircraft Clearance variables
    AIRCRAFT_CLEARANCE_PUSHBACK = jgetfield(AircraftClearance, "AIRCRAFT_CLEARANCE_PUSHBACK");
    AIRCRAFT_CLEARANCE_TAXI_DEPARTING = jgetfield(AircraftClearance, "AIRCRAFT_CLEARANCE_TAXI_DEPARTING");
    AIRCRAFT_CLEARANCE_TAKEOFF = jgetfield(AircraftClearance, "AIRCRAFT_CLEARANCE_TAKEOFF");
    AIRCRAFT_CLEARANCE_ENTER_ARTC = jgetfield(AircraftClearance, "AIRCRAFT_CLEARANCE_ENTER_ARTC");
    AIRCRAFT_CLEARANCE_DESCENT_FROM_CRUISE = jgetfield(AircraftClearance, "AIRCRAFT_CLEARANCE_DESCENT_FROM_CRUISE");
    AIRCRAFT_CLEARANCE_ENTER_TRACON = jgetfield(AircraftClearance, "AIRCRAFT_CLEARANCE_ENTER_TRACON");
    AIRCRAFT_CLEARANCE_APPROACH = jgetfield(AircraftClearance, "AIRCRAFT_CLEARANCE_APPROACH");
    AIRCRAFT_CLEARANCE_TOUCHDOWN = jgetfield(AircraftClearance, "AIRCRAFT_CLEARANCE_TOUCHDOWN");
    AIRCRAFT_CLEARANCE_TAXI_LANDING = jgetfield(AircraftClearance, "AIRCRAFT_CLEARANCE_TAXI_LANDING");
    AIRCRAFT_CLEARANCE_RAMP_LANDING = jgetfield(AircraftClearance, "AIRCRAFT_CLEARANCE_RAMP_LANDING");
    
    //NATS simulation status definition
    //You can get simulation status from the server and know what it refers to
    NATS_SIMULATION_STATUS_READY = jgetfield(SimulationStatus, "DEFAULT_GRAVITY");
    NATS_SIMULATION_STATUS_START = jgetfield(SimulationStatus, "NATS_SIMULATION_STATUS_START");
    NATS_SIMULATION_STATUS_sleep = jgetfield(SimulationStatus, "NATS_SIMULATION_STATUS_PAUSE");
    NATS_SIMULATION_STATUS_RESUME = jgetfield(SimulationStatus, "NATS_SIMULATION_STATUS_RESUME");
    NATS_SIMULATION_STATUS_STOP = jgetfield(SimulationStatus, "NATS_SIMULATION_STATUS_STOP");
    NATS_SIMULATION_STATUS_ENDED = jgetfield(SimulationStatus, "NATS_SIMULATION_STATUS_ENDED");

    //NATS Client Interface definition
    natsClient = NATSClientFactory.getNATSClient();
    simulation = natsClient.getSimulationInterface();
    equipmentInterface = natsClient.getEquipmentInterface();
    entityInterface = natsClient.getEntityInterface();
    aircraftInterface = equipmentInterface.getAircraftInterface();
    environmentInterface = natsClient.getEnvironmentInterface();
    airportInterface = environmentInterface.getAirportInterface();
    pilotInterface = entityInterface.getPilotInterface();
    controllerInterface = entityInterface.getControllerInterface();
    
    natsClient.login("admin");
    
    //Flight parameters to perturb, any of the following attributes can be inserted.
    //PERTURB_ATTRIBUTES = 'AIRSPEED,ALTITUDE,WAYPOINT_LATITUDE_AND_LONGITUDE,WAYPOINT_LONGITUDE,WAYPOINT_LATITUDE,CURRENT_LATITUDE,CURRENT_LONGITUDE,CURRENT_LATITUDE_AND_LONGITUDE';
    PERTURB_ATTRIBUTES = '';
    
    //{
    //Monte-Carlo Simulation setup for perturbing altitude (feet)
    //Please enter target aircraft callsign here. SWA1897 is an example.
    //aircraftID = 'SWA1897';
    //meanAltitude = 25000;
    //sampleSize = 10;
    //altitudeVector = meanAltitude + 1000*int8(rand(sampleSize,1,'normal'));
    //
    //Monte-Carlo Simulation setup for perturbing true air speed (knots)
    //Please enter target aircraft callsign here. SWA1897 is an example.
    //aircraftID = 'SWA1897';
    //meanAirspeedSpeed = 450;
    //sampleSize = 10;
    //airspeedVector = meanAirspeedSpeed + 10*int8(rand(sampleSize,1,'normal'));
    //
    //Monte-Carlo Simulation setup for perturbing geo coordinates (latitude and longitude)
    //Please enter target aircraft callsign here. SWA1897 is an example.
    //aircraftID = 'SWA1897';
    //meanCourse = 3.14;
    //sampleSize = 10;
    //courseVector = meanCourse + 0.1*int8(rand(sampleSize,1,'normal'));
    //
    //Monte-Carlo Simulation setup for perturbing geo coordinates (latitude and longitude)
    //Please enter target aircraft callsign here. SWA1897 is an example.
    //aircraftID = 'SWA1897';
    //meanRocd = 25;
    //sampleSize = 10;
    //rocdVector = meanRocd + int8(rand(sampleSize,1,'normal'));
    //
    //Monte-Carlo Simulation setup for perturbing geo coordinates (latitude and longitude)
    //Please enter target aircraft callsign here. SWA1897 is an example.
    //aircraftID = 'SWA1897';
    //waypointIndex = 8;
    //meanLatitude = 34.422439;
    //meanLongitude = -118.025853;
    //sampleSize = 10;
    //latitudeVector = meanLatitude + 0.1*int8(rand(sampleSize,1,'normal'));
    //longitudeVector = meanLongitude + 0.1*int8(rand(sampleSize,1,'normal'));
    //}
    
    //Monte-Carlo Simulation setup for perturbing geo coordinates (latitude and longitude)
    //Please enter target aircraft callsign here. SWA1897 is an example.
    aircraftID = 'SWA1897';
    waypointIndex = 8;
    meanLatitude = 34.422439;
    meanLongitude = -118.025853;
    sampleSize = 10;
    latitudeVector = meanLatitude + double(0.1*int8(rand(sampleSize,1,'normal')));
    longitudeVector = meanLongitude + double(0.1*int8(rand(sampleSize,1,'normal')));
    
    //{
    //Monte-Carlo Simulation setup for perturbing geo coordinates (latitude)
    //Please enter target aircraft callsign here. SWA1897 is an example.
    //aircraftID = 'PLEASE_ENTER_AIRCRAFT_CALLSIGN_HERE';
    //waypointIndex = 8;
    //meanLatitude = 34.422439;
    //sampleSize = 10;
    //latitudeVector = meanLatitude + 0.1*int8(rand(sampleSize,1,'normal'));
    
    //Monte-Carlo Simulation setup for perturbing geo coordinates (longitude)
    //Please enter target aircraft callsign here. SWA1897 is an example.
    //aircraftID = 'PLEASE_ENTER_AIRCRAFT_CALLSIGN_HERE';
    //waypointIndex = 8;
    //meanLongitude = -118.025853;
    //sampleSize = 10;
    //longitudeVector = meanLongitude + 0.1*int8(rand(sampleSize,1,'normal'));
    //}
    
    //Monte-Carlo Simulation
    for count = 1:sampleSize
        //Clear Trajectory data from previous iteration
        simulation.clear_trajectory();
        
        //Load/Reload wind and flight data since trajectory data had to be cleared from previous iteration
        environmentInterface.load_rap('share/tg/rap');
        aircraftInterface.load_aircraft('share/tg/trx/TRX_DEMO_SFO_PHX_GateToGate.trx', 'share/tg/trx/TRX_DEMO_SFO_PHX_mfl.trx');
        
        //Set up simulation (Versions of setupSimulation can be found in the
        //documentation)
        simulation.setupSimulation(11000, 30);
        //Start simulation to go through till 1000 seconds. This time can be
        //changed, and the simulation would sleep at the provided time.
        simulation.start(1000.0);
        
        //Wait for simulation to sleep
        while 1
            serverStatus = simulation.get_runtime_sim_status();
            if (serverStatus ~= NATS_SIMULATION_STATUS_sleep)
               sleep(1000);
            else
                break;
            end
        end
        
        //Get current state of aircraft
        aircraft = aircraftInterface.select_aircraft(aircraftID);
        
        if (strstr(PERTURB_ATTRIBUTES, 'AIRSPEED') ~= '')
            //aircraft.getTas_knots();
            aircraft.setTas_knots(airspeedVector(count));
        end
        if (strstr(PERTURB_ATTRIBUTES, 'ALTITUDE') ~= '')
            //aircraft.getAltitude_ft();
            aircraft.setAltitude_ft(altitudeVector(count));
        end
        if (strstr(PERTURB_ATTRIBUTES, 'WAYPOINT_LATITUDE') ~= '')
            aircraft.setFlight_plan_latitude_deg(waypointIndex, latitudeVector(count));
        end
        if (strstr(PERTURB_ATTRIBUTES, 'WAYPOINT_LONGITUDE') ~= '')
           aircraft.setFlight_plan_longitude_deg(waypointIndex, longitudeVector(count));
        end
        if (strstr(PERTURB_ATTRIBUTES, 'WAYPOINT_LATITUDE_AND_LONGITUDE') ~= '')
           aircraft.setFlight_plan_latitude_deg(waypointIndex,  latitudeVector(count));
           aircraft.setFlight_plan_longitude_deg(waypointIndex, longitudeVector(count));
        end
    
        if (strstr(PERTURB_ATTRIBUTES, 'CURRENT_LATITUDE') ~= '')
           //aircraft.getLatitude_deg();
           aircraft.setLatitude_deg(latitudeVector(count));
        end
        if (strstr(PERTURB_ATTRIBUTES, 'CURRENT_LONGITUDE') ~= '')
           //aircraft.getLongitude_deg();
            aircraft.setLongitude_deg(longitudeVector(count));
        end
        if (strstr(PERTURB_ATTRIBUTES, 'CURRENT_LATITUDE_AND_LONGITUDE') ~= '')
            aircraft.setLatitude_deg(latitudeVector(count));
            aircraft.setLongitude_deg(longitudeVector(count));
        end
        
        //Functions for aircraft ground operation parameters have been listed here.
        //Similarly, other attributes can also be perturbed.
        //THESE PERTURBATIONS MIGHT LEAD TO ERRONEOUS FLIGHT SIMULATION RESULTS
        //airportInterface.setTaxi_tas_knots('SWA1897', 20);
        //aircraft.setCourse_rad(1.54);
        aircraft.setLatitude_deg(double(latitudeVector(count)));
        aircraft.setLongitude_deg(double(longitudeVector(count)));
    
        simulation.resume();
        
        //Wait for simulation to get done  
        while 1
            serverStatus = simulation.get_runtime_sim_status();
            if (serverStatus ~= NATS_SIMULATION_STATUS_ENDED)
               sleep(1000);
            else
                break;
            end
        end
       
        //Generating and saving new trajectory
        trajectoryFile = msprintf(strcat([aircraft.getAcid(), '-Scilab-Monte-Carlo-Sim-Trajectory_', string(count),'.csv']));
        simulation.write_trajectories(strcat(['share/mcSimulation/' trajectoryFile]));
    
        //Wait for updated trajectory to get written
        sleep(2000);
    
        //Clear simulation data for next iteration
        aircraftInterface.release_aircraft();
        sleep(1500);
        environmentInterface.release_rap();
        sleep(1500);
        
    end
    
    
    natsClient.disConnect()
    
    //Plot graph for the Monte Carlo Simulation output
    trajectoryCount = sampleSize
    
    //Iterate through the number of trajectories to be plotted
    for currentTrajectory = 1:trajectoryCount
        //Read trajectory files in  to a table and convert it to an array.
        csvFile = mopen(strcat([NATS_Server '/share/mcSimulation/' aircraftID '-Scilab-Monte-Carlo-Sim-Trajectory_' string(currentTrajectory) '.csv']),'r');
        FlightParameters = mgetl(csvFile);
        lengthFlightParameters = size(FlightParameters, 'r') - 10;
        
        //Initialize flight parameter variables
        trueAirSpeedReadings = zeros(lengthFlightParameters, 1);
        altitudeReadings = zeros(lengthFlightParameters, 1);
        timestampReadings = zeros(lengthFlightParameters, 1);
        latitudeReadings = zeros(lengthFlightParameters, 1);
        longitudeReadings = zeros(lengthFlightParameters, 1);
        rocdReadings = zeros(lengthFlightParameters, 1);
        courseReadings = zeros(lengthFlightParameters, 1);
    
        startIndex = 1;
        //Get relevant flight data starting line number from simulation CSV output
        for count=1:size(FlightParameters, 'r')
            trajectoryPoint = strsplit(char(FlightParameters(count)), ',');
            if(size(trajectoryPoint, 'r') > 3)
                if(~strcmp(string(trajectoryPoint(3)), aircraftID))
                    startIndex = count + 1;
                end
            end
        end
    
        trajectoryPoint = strsplit(char(FlightParameters(startIndex)), ',');
    
            
        //Traverse through trajectory points and read flight data
        for count=startIndex:size(FlightParameters, 'r')
            trajectoryPoint = strsplit(string(FlightParameters(count)), ',');
            if(~strcmp(string(trajectoryPoint(1)), ''))
                break;
            end
    
            trueAirSpeedReadings(count - 8,1) = strtod(string(trajectoryPoint(6)));
            altitudeReadings(count - 8,1) = strtod(string(trajectoryPoint(4)));
            timestampReadings(count - 8,1) = strtod(string(trajectoryPoint(1)));
            latitudeReadings(count - 8,1) = strtod(string(trajectoryPoint(2)));
            longitudeReadings(count - 8,1) = strtod(string(trajectoryPoint(3)));
            rocdReadings(count - 8,1) = strtod(string(trajectoryPoint(5)));
            courseReadings(count - 8,1) = strtod(string(trajectoryPoint(7)));
        end
    
        //Convert cells to matrix in order to plot graphs
        trueAirSpeedMatrix = trueAirSpeedReadings;
        altitudeMatrix = altitudeReadings;
        timestampMatrix = timestampReadings;
        latitudeMatrix = latitudeReadings;
        longitudeMatrix = longitudeReadings;
        rocdMatrix = rocdReadings;
        courseMatrix = courseReadings;
    
        //Graph visualization begins, this can be used as template for custom plots
    
    
        //Plot altitude vs timestamp
        subplot(3, 2, 1);
        title( 'Altitude vs. Time');
        plot(timestampMatrix, altitudeMatrix);
        xlabel('Time (s)');
        ylabel('Altitude (feet)');
        //Optionally limit the x or y axis limits to focus on part of graph
        //xlim([9000 11000])
    
        //Plot true arispeed vs timestamp
        subplot(3, 2, 2);
        title( 'True Airspeed vs. Time');
        plot(timestampMatrix, trueAirSpeedMatrix);
        xlabel('Time (s)');
        ylabel('Cruise True Airspeed (knots)');
        //xlim([9000 11000])
    
        //Plot latitude vs longitude
        subplot(3, 2, 3);
        title( 'Latitude vs. Longitude');
        plot(longitudeMatrix, latitudeMatrix);
        xlabel('Longitude (degree)');
        ylabel('Latitude (degree)');
        //xlim([-114 -110])
    
        //Plot rate of climb/descent vs timestamp
        subplot(3, 2, 4);
        title( 'Rate of Climb/Descent vs. Time');
        plot(timestampMatrix, rocdMatrix);
        xlabel('Time (s)');
        ylabel('Rate of Climb/Descent (feet/minute)');
        //xlim([9000 11000])
        
        //Plot course angle vs timestamp
        subplot(3, 2, 5);
        title( 'Course vs. Time');
        plot(timestampMatrix, courseMatrix);
        xlabel('Time (s)');
        ylabel('Course (degree)');
        //xlim([9000 11000])
        
        mclose(csvFile);
    
    end
end
