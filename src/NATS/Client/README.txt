National Airspace Trajectory-Prediction System(NATS)

Version beta 1.3

Client Program Module

This program module allows the users to access the NATS functions implemented on the server through the Java Remote Method Invocation (RMI) technology. Users can create customized programs by calling server-side RMI functions to create and load gate-to-gate flight plans, weather, Center/Sector definition databases, propagate aircraft trajectories in the National Airspace Ssystem (NAS,output trajectory data and create plots for visualization and analysis.  Please refer to dist/javadoc_client/com/osi/nats/api/package-frame.html for additional information on available functions (API).


Contents of the zip file NATS-Client.zip
===================================
<data>               Dir    Runtime data directory
<dist>               Dir    NATS binary files
<sample>             Dir    NATS sample codes
README.txt
README_Examples.txt
What_is_New.txt


Hardware Requirements
=====================
1. Intel/AMD 64bit CPU 1Ghz and up
2. RAM capacity at least 1GB


Software Requirements
=====================
1. Linux 64bit Operating System
   NATS software has been tested on:
   # Ubuntu v12.04, v16.04 with gcc 4.8
   # CentOS 6.9 with gcc 4.4
   # CentOS 7 with gcc 4.8
2. Java 1.7 and later
3. Jpype(For Python codes)
   Tested on v0.6.0, v0.6.3
   
   To install Jpype 0.6.0
   Go to https://github.com/originell/jpype
   Download jpype-0.6.0.tar.gz
   Unzip it, enter the directory and execute commands.
       sudo python setup.py install
4. MATLAB(if applicable)
   Tested on MATLAB R2014b, R2015b
5. Python 2.7


NATS client config file
=======================
The config file is located at data/nats.config
Two required required parameters are:
1. Hostname/IP address of the target NATS server to connect to.
2. Port number to connect to(default: 2017)


Running sample programs
===========================
NATS interface functions are written in Java and provided through the server-client mechanism to the user for their software development.  Python and MATLAB interfaces are provided for interactive or batch computations by non-Java users.  Certain bridge plugins/wrapers are required to enable this functionality.
===========================
1. Usage with Python Jpype
   (Please install Jpype plugin ready first.)
   1.1 Set the environment variable JAVA_HOME
   1.2 Edit the sample/basic_python_example_beta1.2.py and specify the correct path of nats-client.jar and nats-shared.jar
   1.3 Execute
           python sample/basic_python_example_beta1.2.py

Note: If you are running in a Python IDE, please make sure that you set JAVA_HOME and set the working directory to NATS_Client in the runtime configuration.

2. Usage with MATLAB
   2.1 Edit sample/Sample_Matlab_beta1_2.m and specify the correct path of nats-client.jar and nats-shared.jar
   2.2 Run sample/Sample_Matlab_beta1_2.m.

3. Usage with Octave
   Please refer to "Scilab and Octave Documentation" file for installation and sample file.

4. Usage with SciLab
   Please refer to "Scilab and Octave Documentation" file for installation and sample file.


Q & A
=====
1. The client program throws out an error about not finding the nats.config file.
   Ans. Client program will look for data/nats.config file in runtime.  Please make sure you execute your program under NATS_Client directory.  If you have to execute the client program in different directory, please set the OS environment variable NATS_CLIENT_HOME to the path of NATS_Client folder.
        Example. In Linux command-line terminal, type
            export NATS_CLIENT_HOME=/your_path/NATS_Client

