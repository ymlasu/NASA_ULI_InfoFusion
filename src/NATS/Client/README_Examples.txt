Following are the description of the examples:

1. GateToGateFp.py: This module can be run as a client program with NATS Server running in the background. The description is available in the GateToGateFpReadme.pdf file.

2. SampleMonteCarlo.m: This is matlab code that can be run by opening it within MATLAB. The path needs to be set to NATS_Client in order for it to have access to the jar files. It simulates and saves trajectories inside NATS_Server/share/mcSimulation directory. Details are provided within the code comments.

3. PlotGraph.m: This is a supplementary function to SampleMonteCarlo module. It is used to plot out graphs for desired flight parameters.

4. DEMO_Aircraft_Functions_beta1.0.py: Basic aircraft function examples.

5. DEMO_Airport_Functions_beta1.0.py: Basic airport function examples.

6. DEMO_Gate_To_Gate_Simulation_SFO_PHX_beta1.0.py: Gate-to-gate simulation from SFO to PHX.

7. DEMO_Simulation_100rec_beta1.0.py: Simulation of 100 flights for 24 hours period.

8. basic_python_example_beta1.0.py: This program runs a basic simulation of NATS for a given flight plan. 

9. Example_MC_code.py: This is the Monte Carlo simulation frontend. You can create samples and insert it in NATS for simulation.

10. NATS_header.py: This module contains all the frontmatter that has to be inserted in any given NATS Client program.

11. NATS_MonteCarlo_Interface.py: This is the Monte Carlo simulation backend. It takes in all the inputs from the Monte Carlo frontend, processes it, run the simulation and produces outputs in form of csv files.

12. PostProcessor.py: It is the visualization and post processing module for NATS simulations. It takes in MC simulation results and produces histograms and plots for state variables.  