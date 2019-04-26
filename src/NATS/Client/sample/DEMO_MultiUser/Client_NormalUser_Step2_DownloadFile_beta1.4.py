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

classpath = "dist/nats-client.jar:dist/nats-shared.jar:dist/json.jar:dist/rmiio-2.1.2.jar:dist/commons-logging-1.2.jar"

startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % classpath)

NATSClientFactory = JClass('NATSClientFactory')
natsClient = NATSClientFactory.getNATSClient()
simulationInterface = natsClient.getSimulationInterface()

natsClient.login("user1")

if simulationInterface is None:
    print "Can't get SimInterface from server"

else:
    local_trajectory_filename = "DL_Trajectory.csv"
    simulationInterface.requestDownloadTrajectoryFile(local_trajectory_filename)

# Close connection from NATS Server
natsClient.disConnect()

shutdownJVM()
