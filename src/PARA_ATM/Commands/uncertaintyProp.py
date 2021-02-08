'''

NASA NextGen NAS ULI Information Fusion
        
@organization: Southwest Research Institute
@author: Michael Hartnett
@date: 05/30/2019

Command call to interface NATS module with PARA-ATM to fetch generated trajectories.

'''

import PARA_ATM
from PARA_ATM.Commands import runNATS
from PARA_ATM.Commands.Helpers import DataStore
import numpy as np
import centaur
centaur.CentaurUtils.initialize_centaur()

class Command:
    '''
        Class Command wraps the command methods and functions to be executed. For user-defined commands, this name 
        should be kept the same (Command).
    '''
    
    def __init__(self,safety_module):
        """
            uncertaintyProp command propagates uncertainty from given sources through a given safety metric
            args:
                safety_module (str) : the module to calculate the safety metric and its parameters
                n_samples (int) : the number of samples required from the distribution(s)
        """
        #parse the safety_module string
        self.mod_name = safety_module.split('(')[0]
        self.in_file = safety_module.split('(')[1]
        #load the module
        self.safety_module = getattr(PARA_ATM.Commands,self.mod_name)

        #future args for uncertaintyProp
        self.n_samples = 10
        self.states = ['pushbackDelay',
                       'taxiDepartingDelay',
                        'takeoffDelay',
                        'enterARTCDelay',
                        'descentDelay',
                        'enterTRACONDelay',
                        'approachDelay',
                        'touchdownDelay',
                        'taxiLandingDelay',
                        'rampLandingDelay']

    #Method name executeCommand() should not be changed. It executes the query and displays/returns the output.
    def executeCommand(self):
        """
            returns:
                results (list) : [moduleName, aggregated return from the safety module
        """

        #instantiate helper function module for db access
        db_access = DataStore.Access()

        #get Centaur distribution objects from the database
        dist_objs = [db_access.getCentaurDist(key=state) for state in self.states]

        #create random variable matrix
        v = centaur.RV_Vector()
        for obj in dist_objs:
            v.append(obj)

        def min_fpf(rts):
            return np.min(self.safety_module.Command([self.in_file,rts]).executeCommand()[1])
        
        def delay(x):
            data = self.safety_module.Command([self.in_file,{self.states[i]:x[i] for i in range(len(self.states))}]).executeCommand()[1]
            return 1
    

        context = centaur.ReliabilityContext(v,min_fpf,-1,0.2)
        method=centaur.ReliabilityMethod()
        method.new_LHS(self.n_samples)
        context.reliability_analysis(method)

        samps = method.get_output_samples_data(self.n_samples)

        return ["uncertaintyProp", samps]
