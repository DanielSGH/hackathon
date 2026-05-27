import TariffService, AlertService, EnergyReading, EnergySummary, ReadingResult, SmartEnergyMonitor
import random, string, sys

# For the edge cases we will test specific edge cases conserning our device_id and watt_hours variables
# We are going to use boundary value analysis
#  
# device_id:
# for device id we made 2 blocks, legal and nonlegal strings,
#   - the nonlegal strings were only 2 strings, so there really is no edge case there
#   - for the legal strings we took any string with length > 0
#       + therefore the edge cases for this block are strings with length 1 and intMAX      (normal)
# 
# watt_hours:
# for watt_hours we made 3 blocks, legal, nonlegal and anomaly,
#   - the legal block we defined as (>= 0 <= anomaly_threshold)     (normal)
#       + so the edge cases are: 0 && anomaly_threshold
#   - the nonlegal block we defined as (<0)     (error)
#       + so the edge cases are: -1 && -intMAX
#   - the anomaly block we defined as (> anomaly_threshold)     (error)
#       + so the edge cases are: anomaly_threshold+1 && intMax

# For the normal test value we again use AC because this will result in 2*2=4 test cases

# And then use EC for the error test cases because we have 1 error block for device_id and 2 for watt_hours
# We only need 2 tests for EC covarage

def generateLegalString(length):
    return(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length)))


def normal(smart_energy_monitor):
    watt_hours_input = [0, smart_energy_monitor.anomaly_threshold]
    device_id_input = []
    device_id_input.append(generateLegalString(1))
    device_id_input.append(generateLegalString(sys.maxsize))

    for id in device_id_input:
        for watt in watt_hours_input:

            energy_reading = EnergyReading(id, watt)
            reading_result = smart_energy_monitor.process_reading(energy_reading)

            if reading_result.is_accepted():
                print("test passed")
            else:
                print("test failed")


def error(smart_energy_monitor):
    watt_hours_nonlegal = [-1 , sys.maxsize * -1]
    watt_hours_anomaly = [smart_energy_monitor.anomaly_threshold+1, sys.maxsize]
    device_id_input = [None, ""]

    # test 1
    energy_reading = EnergyReading(random.choice(device_id_input), random.choice(watt_hours_nonlegal))
    reading_result = smart_energy_monitor.process_reading(energy_reading)

    if reading_result.is_accepted():
        print("test failed")
    else:
        print("test passed")

    # test 2
    energy_reading = EnergyReading(random.choice(device_id_input), random.choice(watt_hours_anomaly))
    reading_result = smart_energy_monitor.process_reading(energy_reading)

    if reading_result.is_accepted():
        print("test failed")
    else:
        print("test passed")


def edgeCaseTesting():

    tariff_service = TariffService
    alert_service = AlertService
    smart_energy_monitor = SmartEnergyMonitor(tariff_service, alert_service ,100 )

    normal(smart_energy_monitor)
    error(smart_energy_monitor)



if __name__ == "__main__":
    edgeCaseTesting()