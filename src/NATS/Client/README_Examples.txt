National Airspace Trajectory-Prediction System(NATS)

Version beta 1.5

Following are the description of the examples:

1. sample/DEMO_MC_Simulation/Example_MC_code.py: This is the Monte Carlo simulation frontend. You can create samples and insert it in NATS for simulation.
   sample/DEMO_MC_Simulation/NATS_header.py: This module contains all the frontmatter that has to be inserted in any given NATS Client program.
   sample/DEMO_MC_Simulation/NATS_MonteCarlo_Interface.py: This is the Monte Carlo simulation backend. It takes in all the inputs from the Monte Carlo frontend, processes it, run the simulation and produces outputs in form of csv files.
   sample/DEMO_MC_Simulation/PostProcessor.py: It is the visualization and post processing module for NATS simulations. It takes in MC simulation results and produces histograms and plots for state variables.

2. sample/DEMO_Procedure_Display/displayProcs.py: This module is used to display procedure. GIve it a list of airport(s). It will give out SIDs, STARs and Approaches in that order. Usage: python sample/DEMO_Procedure_Display/displayProcs.py <list of airports> eg: python sample/DEMO_Procedure_Display/displayProcs.py KSFO KMSP KDFW
   sample/DEMO_Procedure_Display/Flight_Plan_Display_and_Creation.py: Shows how to create a flight plan with example going from SFO to PHX. 
   sample/DEMO_Procedure_Display/NATS_header.py: This module contains all the frontmatter that has to be inserted in any given NATS Client program. 
   sample/DEMO_Procedure_Display/PlotHelpers.py: Used for plotting procedures. It has a bunch of routines using matplotlib libraries. 
   sample/DEMO_Procedure_Display/PostProcessor.py:  It is the visualization and post processing module for NATS simulations. It takes in MC simulation results and produces histograms and plots for state variables.
   sample/DEMO_Procedure_Display/ProcedureDisplay.py: This is the backend that handles the display of procedures using displayProcs.py module. 

3. sample/DEMO_XPlane/XPlane_NATS_Integration_Client_beta1.5.py: The client code that reads data from a live X-Plane flight simulation, and feeds it into NATS for trajectory generation. This sample code can be used for extending real time simulation from other simulators as well.

4. sample/basic_python_example_beta1.5.py: This program runs a basic simulation of NATS for a given flight plan. 

5. sample/DEMO_Aircraft_Functions_beta1.5.py: Basic aircraft function examples.
   sample/DEMO_Aircraft_Functions_beta1_5.m: MATLAB sample.

6. sample/DEMO_Aircraft_State_Change_beta1.5.py: Sample program demonstrating how to change aircraft state.
   sample/DEMO_Aircraft_State_Change_beta1_5.m: MATLAB sample.

7. sample/DEMO_Airport_Functions_beta1.5.py: Basic airport function examples.
   sample/DEMO_Airport_Functions_beta1_5.m: MATLAB sample.

8. sample/DEMO_CDNR_beta1.5.py: Enable "Conflict Detection and Resolution" in flight simulation.
   sample/DEMO_CDNR_beta1_5.m: MATLAB sample.

9. sample/DEMO_ControllerInterface_beta1.5.py: Demo of Controller module functionality.

10. sample/DEMO_Gate_To_Gate_Simulation_SFO_PHX_beta1.5.py: Gate-to-gate simulation from SFO to PHX.
    sample/DEMO_Gate_To_Gate_Simulation_SFO_PHX_beta1_5.m: MATLAB sample.

11. sample/DEMO_SafetyMetricsInterface_beta1.5.py: Demo of SafetyMetrics module functionality.

12. sample/DEMO_SFO_PHX_Hold_Pattern_beta1.5.py: Demo of several hold patterns of a aircraft.

13. sample/DEMO_Simulation_100rec_beta1.5.py: Simulation of 100 flights for 24 hours period.
    sample/DEMO_Simulation_100rec_beta1_5.m: MATLAB sample.

14. sample/DEMO_StrategicWeatherAvoidance_beta1.5.py: Strategic weather avoidance in flight simulation.
    sample/DEMO_StrategicWeatherAvoidance_beta1_5.m: MATLAB sample.

15. sample/DEMO_TacticalWeatherAvoidance_beta1.5.py: Tactical weather avoidance in flight simulation.
    sample/DEMO_TacticalWeatherAvoidance_beta1.5.py: MATLAB sample.

16. sample/GateToGateFp.py: This module can be run as a client program with NATS Server running in the background. The description is available in the GateToGateFpReadme.pdf file.

17. sample/Octave_SampleMonteCarloController_Beta_1.5.m: GNU Octave program of Monte Carlo simulation by changing Controller behavior. It plots out the graph showing crucial flight parameters after simulation runs through.

18. sample/Octave_SampleMonteCarloPilot_Beta_1.5.m: GNU Octave program of Monte Carlo simulation by changing Pilot behavior. It plots out the graph showing crucial flight parameters after simulation runs through.

19. sample/Octave_SampleMonteCarloSafetyMetrics_Beta_1.5.m: GNU Octave program of Monte Carlo simulation by changing safety metrics. It plots out the graph showing crucial flight parameters after simulation runs through.

20. sample/Octave_SampleMonteCarloGroudParameters_Beta_1.5.m: GNU Octave program of Monte Carlo simulation by changing aircraft ground parameters. It plots out the graph showing crucial flight parameters after simulation runs through.

21. sample/PlotGraph.m: This is a supplementary function to SampleMonteCarlo modules. It is used to plot out graphs for desired flight parameters.

22. sample/SampleMonteCarloController_Beta_1_5.m: MATLAB program of Monte Carlo simulation by changing Controller behavior. It plots out the graph showing crucial flight parameters after simulation runs through.

23. sample/SampleMonteCarloPilot_Beta_1_5.m: MATLAB program of Monte Carlo simulation by changing Pilot behavior. It plots out the graph showing crucial flight parameters after simulation runs through.

24. sample/SampleMonteCarloSafetyMetrics_Beta_1_5.m: MATLAB program of Monte Carlo simulation by changing safety metrics. It plots out the graph showing crucial flight parameters after simulation runs through.

25. sample/SampleMonteCarloGroundParameters_Beta_1_5.m: MATLAB program of Monte Carlo simulation by changing aircraft ground parameters. It plots out the graph showing crucial flight parameters after simulation runs through.

26. sample/PathVisualizer.py: This python module is a helper function to plot trajectories on Google Map after the simulation goes through. Pre-requisite for this is Google Chrome or Mozilla Firefox browser.

27. sample/Scilab_SampleMonteCarloController_Beta_1.5.sce: Scilab program of Monte Carlo simulation by changing Controller behavior. It plots out the graph showing crucial flight parameters after simulation runs through.

28. sample/Scilab_SampleMonteCarloPilot_Beta_1.5.sce: Scilab program of Monte Carlo simulation by changing Pilot behavior. It plots out the graph showing crucial flight parameters after simulation runs through.

29. sample/Scilab_SampleMonteCarloSafetyMetrics_Beta_1.5.sce: Scilab program of Monte Carlo simulation by changing safety metrics. It plots out the graph showing crucial flight parameters after simulation runs through.

30. sample/Scilab_SampleMonteCarloGroudParameters_Beta_1.5.sce: Scilab program of Monte Carlo simulation by changing aircraft ground parameters. It plots out the graph showing crucial flight parameters after simulation runs through.

31. sample/DEMO_UI_TaxiRouteGenerator/arv_taxiplan_example.py: This example illustrates how to use NATS functions of airport interfaces.
    sample/DEMO_UI_TaxiRouteGenerator/dep_taxiplan_example.py: This example illustrates how to use NATS functions for plotting airport layout and
	    design a user-designed taxi plan. This compares the user-designed taxiplan with the one
	    generated by the shortest path, which is a default method employed in NATS.
    sample/DEMO_UI_TaxiRouteGenerator/PlotHelpers.py: Module to plot and read/write data, used as helper functions to the arrival and departure taxiplan generator.

32. sample/DEMO_MultiUser: This directory demonstrates the feature of real-time simulation to serve multiple users.
    Please see sample/DEMO_MultiUser/README.doc file for the detail.
    
33. sample/DEMO_ADSB/DEMO_ADSB_Live_Simulation_Beta_1.5.py: This example reads the ADS-B flight data in real time, and simulates them within NATS. The detailed documentation is available at NATS_Client/sample/DEMO_ADSB/ADS-B Documentation Beta 1.5.pdf.

34. sample/DEMO_AircraftLoadAndCostFunctions_beta1.5.py: Python module to demonstrate use of the aircraft and cargo load and cost functions. The API documentation has the function usage information.

35. sample/DEMO_MergingAndSpacing_beta1.5.py: This Python module simulates three flights to demonstrate them being held at the meter fix while entering TRACON for spacing in the airport arrival flight stream.

36. sample/DEMO_WakeVortexModel_beta1.5.py: This example demonstrates the function to model a wake vortex scenario, it yields the aircraft that would be within hazard range.

37. sample/DEMO_SimulationSubscription_beta1.5.py: This example demonstrates a simulation situation with subscription to flight state data at every time step. The code contains documentation to explain the concept in further detail.

38. sample/GateToGateFpWithoutBaseTRX.py: This example generates gate to gate flight plan without needing an existing FAA TRX flight plan.

39. sample/DEMO_AircraftTakeOffAndTouchDownPoint_beta1.5.py: This example demontrates the functions to get and set aircraft take off and touch down points.

40. sample/DEMO_ARTCC_Functions_beta1.5.py: Example usage of ARTCC functions to get center data including fixes contained in a given center.

41. sample/DEMO_CNSInterface_beta1.5.py: Demonstrates examples of functions within the CNS Interface.

42. sample/DEMO_GroundVehicle_beta1.5.py: This example demonstrates functions for ground vehicle simulation.

43. sample/DEMO_GroundOperator_beta1.5.py: This example demonstrates functions for ground operator errors that may impact ground vehicle simulation.

44. sample/DEMO_GroundSafetyFunctions_beta1.5.py: This examples demonstrates usage of functions to calculate L1 distance and the distance to pavement edge for when the aircraft is on the ground.

45. sample/DEMO_Aircraft_Validator_Flight_Plan_Record_beta1.5.py: Validator of aircraft flight plan record.

46. sample/DEMO_Weather_Functions_beta1.6.py: Demo program of weather-related functions.
    The program shows examples about handling wind and weather data.
    Notice. The weather polygon functions is not fully tested over generic cases.  If you experience problems, please contact NATS development team.

47. sample/DEMO_Interactive_NATS_Client_beta1.6.py: Demo program to run NATS Interactive Session.

48. sample/DEMO_Unittests_beta1.6.py: Unit test case suite for NATS functions.
    Notice. This program is in continuous revision and will provide comprehensive test cases.  If you experience problems, please contact NATS development team.
