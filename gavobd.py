# encoding: utf-8
import obd
import time

starttime = time.time()

# connect to the car
connection = obd.OBD()

# Assign OBD Commands to Variables
rpm = obd.commands.RPM # select an OBD command (sensor) - RPM
dtc = obd.commands.GET_DTC # Trouble Codes
intake_pressure = obd.commands.INTAKE_PRESSURE # Pressure
vehicle_speed = obd.commands.SPEED # Vehicle Speed
intake_temp = obd.commands.INTAKE_TEMP
engine_load = obd.commands.ENGINE_LOAD
coolant_temp = obd.commands.COOLANT_TEMP
maf = obd.commands.MAF


# Query with variable name and store in new variable
while True:
	rpm_response = connection.query(rpm) # send the command, and parse the response
	dtc_response = connection.query(dtc)
	intake_pressure_response = connection.query(intake_pressure)
	vehicle_speed_response = connection.query(vehicle_speed)
	intake_temp_response = connection.query(intake_temp)
	engine_load_response = connection.query(engine_load)
	coolant_temp_response = connection.query(coolant_temp)
	maf_response = connection.query(maf)

	# Possible endpoint for labelling the output
	# rpm_endpoint = "RPM:" . rpm_response.value
	# print(rpm_endpoint)

	# Print query responses

	print(rpm_response.value)
	print(dtc_response.value)
	print(intake_pressure_response.value)
	print(vehicle_speed_response.value)
	print(intake_temp_response)
	print(engine_load_response)
	print(coolant_temp_response)
	print(maf_response)
	time.sleep(1)

#print(response.unit)
