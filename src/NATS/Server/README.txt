National Airspace Trajectory-Prediction System(NATS)

Version beta 1.6

Server Program Module

This program module is responsible for all the computations related to the aircraft trajectory propagation and data manipulation.  This module provides several functional interfaces in order to carry out Java RMI communication in the server-client design architecture.  The client side program module contains corresponding functional interfaces corresponding to those on the server module.


Contents of the zip file NATS-Server.zip
========================================
<dependency_library>    Dir    Dependency library
<dist>                  Dir    NATS binary files
<lib_precomp>           Dir    Precompiled dependency library.  You can use them if you have difficulty in compilation.
<log>                   Dir    Log file directory
<share>                 Dir    Background data
<utility>               Dir    Utility program
README.txt
README_Utility.txt
run                            Script to start NATS server
What_is_New.txt


Hardware Requirements
=====================
1. Intel/AMD 64bit CPU 1Ghz and up
2. RAM capacity at least 1GB
   Strategic weather avoidance requires high demand on memory.  We suggest at least 12GB RAM for better system performance. 


Operating System/Software Enviroment Requirements
=================================================
1. Linux 64bit
   This software has been tested on:
   # Ubuntu v12.04, v16.04 with gcc 5.5
   # CentOS 6.9 with gcc 4.4
   # CentOS 7 with gcc 4.8
2. Java 1.7 and later
3. Python 2.7


Starting the NATS server
=========================
This is the first step in using the NATS software. The following steps are required:

1. Modify the run script
   Edit NATS_SERVER_HOME with correct path on your machine.
   Edit correct JDK/JRE path on your machine.(Please use Java 1.7 or later.)
2. Change file permission to executable mode.
   chmod +x ./run
   chmod +x utility/run_nodejs.sh
   chmod +x utility/node-v8.11.1-linux-x64/bin/node
3. Execute the run script in command-line terminal.  Example: ./run
   (It is suggested that you call the run script from the current directory path.)


Stopping the NATS server
========================
This is generally the last step while using the NATS software. The NATS software can be stopped by pressing [Ctrl]-C in the command-line terminal. 


Network Setting
===============
NATS Server utilizes the following ports for data communication with clients.  Please ensure they are accessible from the outside network by configuring your network setting.
TCP port 2017
TCP port 2019




Using NATS Pre-compiled Dependency Libraries(Optional. Only do this if the NATS_Server is not running.)
============================================
Notice: Users don't have to do this unless NATS Server is unable to run on the built-in libraries which came with the distribution.

There are several pre-compiled dependency library zip files in NATS_Server/lib_precomp directory.
Users can use them for running NATS Server if they meet any obstacle while building dependency libraries on Linux systems.

Example
We can use Ubuntu pre-compiled hdf5 library.
# In NATS_Server/lib_precomp directory, unzip hdf5.zip
# Edit NATS_Server/run file
# Append hdf5 pre-compiled lib folder to LD_LIBRARY_PATH environment variable.
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$NATS_SERVER_HOME/dist:$NATS_SERVER_HOME/lib_precomp/Ubuntu_16.04/hdf5/lib
