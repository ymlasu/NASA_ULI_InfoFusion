/*
NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
Copyright 2018 by Optimal Synthesis Inc. All rights reserved

Author: Oliver Chen
Date: 2017-01-19
*/

import java.util.Calendar;

import com.osi.nats.aircraft.Aircraft;
import com.osi.nats.api.EnvironmentInterface;
import com.osi.nats.api.EquipmentInterface;
import com.osi.nats.api.SimulationInterface;
import com.osi.nats.api.equipment.AircraftInterface;

public class Sample_Java {
	
	public static void main(String[] args) {
		NATSClient natsClient = (NATSClient)NATSClientFactory.getNATSClient();
		EnvironmentInterface environmentInterface = natsClient.getEnvironmentInterface();
		SimulationInterface simulationInterface = natsClient.getSimulationInterface();
		EquipmentInterface equipmentInterface = natsClient.getEquipmentInterface();
		AircraftInterface aircraftInterface = equipmentInterface.getAircraftInterface();
		
		Aircraft curAircraft = null;
		
		String curAcId = null;
		String[] allAircraftIdArray = null;
		String[] collectedAircraftIdArray = null;
		
		if ((simulationInterface != null) && (environmentInterface != null) && (aircraftInterface != null)) {
			// Clear server side trajectory data for a fresh simulation
			simulationInterface.clear_trajectory();
			
			// Here the parameters specify the file and path on server.  Please don't change it.
			environmentInterface.load_rap("share/tg/rap");
			
			// Here the parameters specify the file and path on server.  Please don't change it.
			aircraftInterface.load_aircraft("share/tg/trx/TRX_07132005_noduplicates_cut_crypted.trx", "share/tg/trx/TRX_07132005_noduplicatesOSIMaxFltLvl_cut_crypted.trx");

			if (aircraftInterface != null) {
				curAcId = null;
				// Obtain all aircraft ids
				allAircraftIdArray = aircraftInterface.getAllAircraftId();
				if ((allAircraftIdArray != null) && (allAircraftIdArray.length > 0)) {
					for (int i = 0; i < allAircraftIdArray.length; i++) {
						curAcId = allAircraftIdArray[i];
						if ((curAcId != null) && (!"".equals(curAcId))) {
							System.out.println("Sample_Java --> AllAircraftId --> curAcId = " + curAcId);
						}
					}
				}
			}
			
			// Initialize the simulation
			simulationInterface.setupSimulation(7200, 1); // Set 7200 seconds to propagate.  The propagation time step is 1 second.

			// Start simulation
			simulationInterface.start();
			
			// We use another thread to monitor the simulation status
			Thread thread_runtime_status = new Thread(new Runnable_Runtime_Status(aircraftInterface, environmentInterface, simulationInterface));
			thread_runtime_status.start();
			
			try {
				Thread.sleep(1000);
			} catch (Exception ex) {}
			
			// Pause here
			simulationInterface.pause();
			// We visit all aircrafts and show its current state
			if (aircraftInterface != null) {
				int v_runtime_status = simulationInterface.get_runtime_sim_status();
				if ((v_runtime_status != com.osi.util.Constants.NATS_SIMULATION_STATUS_READY) && (v_runtime_status != com.osi.util.Constants.NATS_SIMULATION_STATUS_STOP) && (v_runtime_status != com.osi.util.Constants.NATS_SIMULATION_STATUS_ENDED)) {
					// Show current parameter of all flights
					if ((allAircraftIdArray != null) && (allAircraftIdArray.length > 0)) {
						for (int i = 0; i < allAircraftIdArray.length; i++) {
							curAcId = (String)allAircraftIdArray[i];
							if ((curAcId != null) && (!"".equals(curAcId))) {
								curAircraft = aircraftInterface.select_aircraft(curAcId);
								if (curAircraft != null) {
									//System.out.println("Sample_Java --> AcId = " + curAcId + ": latitude_deg = " + curAircraft.getLatitude_deg() + ", longitude_deg = " + curAircraft.getLongitude_deg() + ", altitude_ft = " + curAircraft.getAltitude_ft());
								} else {
									System.out.println("Sample_Java --> AcId = " + curAcId + ": Can't find aircraft data!");
								}
							}
						}
					}
					
					// Collect qualified aircraft Id array by setting latitude, longitude and/or altitude parameters
					collectedAircraftIdArray = aircraftInterface.getAircraftIds(30.0f, 35.0f, -115.0f, -90.0f, -1.0f, -1.0f);
					if ((collectedAircraftIdArray != null) && (collectedAircraftIdArray.length > 0)) {
						for (int i = 0; i < collectedAircraftIdArray.length; i++) {
							curAcId = collectedAircraftIdArray[i];
							System.out.println("Sample_Java --> Collected Aircraft Id = " + curAcId);
						}
					}
					
					// Manually select an aircraft and modify value
					curAircraft = aircraftInterface.select_aircraft("ULI16-33855");
					if (curAircraft != null) {
						curAircraft.setAltitude_ft(36000.0f);
					}
				} else {
					System.out.println("Sample_Java --> Server sim status not running");
				}
			}
			
			try {
				Thread.sleep(2000);
			} catch (Exception ex) {}
			simulationInterface.resume();

			// Comment out stop() function.  Let server finish the remaining propagation process
//			try {
//				Thread.sleep(5000);
//			} catch (Exception ex) {}
//			sim.stop();
		}
	}
}


class Runnable_Runtime_Status implements Runnable {
	private AircraftInterface aircraftInterface = null;
	private EnvironmentInterface environmentInterface = null;
	private SimulationInterface simulationInterface = null;
	
	public Runnable_Runtime_Status(AircraftInterface air, EnvironmentInterface env, SimulationInterface sim) {
		this.aircraftInterface = air;
		this.environmentInterface = env;
		this.simulationInterface = sim;
	}
	
	public void run() {
		while (true) {
			int v_runtime_status = simulationInterface.get_runtime_sim_status();
			System.out.println("Runtime flight propagation status code from server = " + v_runtime_status);
			if (v_runtime_status == com.osi.util.Constants.NATS_SIMULATION_STATUS_ENDED) {
				break;
			}

			try {
				Thread.sleep(1000);
			} catch (Exception ex) {}
		}
		
		System.out.println("Outputting trajectory data.  Please wait....");
		// Now the flight propagation finishes.  Let us export the trajectory
		// The output file will be saved on server with the given directory path and filename(relative to the server runtime path)
		simulationInterface.write_trajectories("output_trajectory_" + Calendar.getInstance().getTimeInMillis() + ".xml");
		
		// Remember to release aircraft and RAP data
		aircraftInterface.release_aircraft();
		environmentInterface.release_rap();
	}
}