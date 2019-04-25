%{
            NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved
          
Author: Hari Iyer
Date: 08/20/2018
%}

%Clear Garbage Variables/Objects
clear all;

%NATS Server location (eg. /home/user/NATS/NATS_Server).
%Please Enter your local NATS Server location here
NATS_Server = 'NATS_SERVER_LOCATION_HERE';

%Flight for which trajectories need to be plotted
aircraftID = 'PLEASE_ENTER_AIRCRAFT_CALLSIGN_HERE';
trajectoryCount = 10;

%Iterate through the number of trajectories to be plotted
for currentTrajectory = 1:trajectoryCount
    %Read trajectory files in  to a table and convert it to an array
    CSVcontents = readtable([NATS_Server '/share/mcSimulation/' aircraftID '-Monte-Carlo-Sim-Trajectory_' num2str(currentTrajectory) '.csv'],'Delimiter',';','ReadVariableNames',false);
    FlightParameters = table2array(CSVcontents);
    
    %Initialize flight parameter variables
    trueAirSpeedReadings = cell(length(FlightParameters) - 10, 1);
    altitudeReadings = cell(length(FlightParameters) - 10, 1);
    timestampReadings = cell(length(FlightParameters) - 10, 1);
    latitudeReadings = cell(length(FlightParameters) - 10, 1);
    longitudeReadings = cell(length(FlightParameters) - 10, 1);
    rocdReadings = cell(length(FlightParameters) - 10, 1);
    courseReadings = cell(length(FlightParameters) - 10, 1);
    
    %Traverse through trajectory points and read flight data
    for count=11:length(FlightParameters)
        trajectoryPoint = strsplit(char(FlightParameters(count)), ',');
        trueAirSpeedReadings{count - 8} = str2num(char(trajectoryPoint(6)));
        altitudeReadings{count - 8} = str2num(char(trajectoryPoint(4)));
        timestampReadings{count - 8} = str2num(char(trajectoryPoint(1)));
        latitudeReadings{count - 8} = str2num(char(trajectoryPoint(2)));
        longitudeReadings{count - 8} = str2num(char(trajectoryPoint(3)));
        rocdReadings{count - 8} = str2num(char(trajectoryPoint(5)));
        courseReadings{count - 8} = str2num(char(trajectoryPoint(7)));
    end

    %Convert cells to matrix in order to plot graphs
    trueAirSpeedMatrix = cell2mat(trueAirSpeedReadings);
    altitudeMatrix = cell2mat(altitudeReadings);
    timestampMatrix = cell2mat(timestampReadings);
    latitudeMatrix = cell2mat(latitudeReadings);
    longitudeMatrix = cell2mat(longitudeReadings);
    rocdMatrix = cell2mat(rocdReadings);
    courseMatrix = cell2mat(courseReadings);
    
    %Graph visualization begins, this can be used as template for custom plots
    
    %Plot altitude vs timestamp
    altitudeSubplot = subplot(3, 2, 1);
    title(altitudeSubplot, 'Altitude vs. Time');
    plot(timestampMatrix, altitudeMatrix);
    xlabel('Time (s)');
    ylabel('Altitude (feet)');
    %Optionally limit the x or y axis limits to focus on part of graph
    %xlim([9000 11000])
    hold on;
    grid on;
    
    %Plot true arispeed vs timestamp
    tasSubplot = subplot(3, 2, 2);
    title(tasSubplot, 'True Airspeed vs. Time');
    plot(timestampMatrix, trueAirSpeedMatrix);
    xlabel('Time (s)');
    ylabel('Cruise True Airspeed (knots)');
    %xlim([9000 11000])
    hold on;
    grid on;
    
    %Plot latitude vs longitude
    latLonSubplot = subplot(3, 2, 3);
    title(latLonSubplot, 'Latitude vs. Longitude');
    plot(longitudeMatrix, latitudeMatrix);
    xlabel('Longitude (degree)');
    ylabel('Latitude (degree)');
    %xlim([-114 -110])
    hold on;
    grid on;
    
    %Plot rate of climb/descent vs timestamp
    rocdSubplot = subplot(3, 2, 4);
    title(rocdSubplot, 'Rate of Climb/Descent vs. Time');
    plot(timestampMatrix, rocdMatrix);
    xlabel('Time (s)');
    ylabel('Rate of Climb/Descent (feet/minute)');
    %xlim([9000 11000])
    hold on;
    grid on;

    %Plot course angle vs timestamp
    courseSubplot = subplot(3, 2, 5);
    title(courseSubplot, 'Course vs. Time');
    plot(timestampMatrix, courseMatrix);
    xlabel('Time (s)');
    ylabel('Course (degree)');
    %xlim([9000 11000])
    hold on;
    grid on;
    
end
