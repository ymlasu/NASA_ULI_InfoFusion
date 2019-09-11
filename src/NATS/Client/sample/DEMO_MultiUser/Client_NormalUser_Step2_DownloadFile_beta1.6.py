# NATS sample
#
# Optimal Synthesis Inc.
#
# Oliver Chen
# 03.29.2019
#
# This program demonstrates Normal User operations.
#
# The client logs into NATS as a normal user, requests to download the latest trajectory file.

from jpype import *
from array import *
from datetime import datetime
import os
import time
import csv

env_NATS_CLIENT_HOME = os.environ.get('NATS_CLIENT_HOME')

str_NATS_CLIENT_HOME = ""

if not(env_NATS_CLIENT_HOME is None) :
    str_NATS_CLIENT_HOME = env_NATS_CLIENT_HOME + "/"

classpath = str_NATS_CLIENT_HOME + "dist/nats-client.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/nats-shared.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/json.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/rmiio-2.1.2.jar"
classpath = classpath + ":" + str_NATS_CLIENT_HOME + "dist/commons-logging-1.2.jar"

startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % classpath)

NATSClientFactory = JClass('NATSClientFactory')
natsClient = NATSClientFactory.getNATSClient()
simulationInterface = natsClient.getSimulationInterface()

natsClient.login("user1")

if simulationInterface is None:
    print "Can't get SimInterface from server"

else:
    local_trajectory_filename = "DL_Trajectory.csv"
    simulationInterface.requestDownloadTrajectoryFile()

# Close connection from NATS Server
natsClient.disConnect()

shutdownJVM()
