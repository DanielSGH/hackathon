import TariffService, AlertService, EnergyReading, EnergySummary, ReadingResult, SmartEnergyMonitor
import random
import string
import sys

# device_id has 2 blocks, 
#   - legal (strings with length >0)
#   - non-legal (empty or null)
# 
# watt_hours has 3 blocks,
#   - legal (>= 0 <= anomaly_threshold)
#   - non-legal (<0)
#   - anomaly (> anomaly_threshold)
# 
# Use all combinations because only 2 blocks for device_id and 3 for watt_hours
# Which will generate 2 * 3 = 6 test cases

def generateLegalString(length):
    return(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length)))


def inputSpacePartitioning():
    
    tariff_service = TariffService.TariffService()
    alert_service = AlertService.Alertervice()
    smart_energy_monitor = SmartEnergyMonitor.SmartEnergyMonitor(tariff_service, alert_service ,100 )

    device_id_input = ["legal", "nonlegal"]
    # device_id_input.append(generateLegalString(random.randint(0,100)))
    # device_id_input.append(random.choice([None, ""]))
    
    watt_hours_input = ["legal", "nonlegal", "anomaly"]
    # watt_hours_input.append(random.randint(0, 100))
    # watt_hours_input.append(random.randint(0,100) * -1)

    for watt in watt_hours_input:
        for id in device_id_input:
            
            if watt == "legal":
                watt_hours = random.randint(0, smart_energy_monitor.anomaly_threshold)
            elif watt == "anomaly":
                watt_hours = random.randint(smart_energy_monitor.anomaly_threshold, sys.maxsize)
            else:
                watt_hours = random.randint(0, sys.maxsize) * -1

            if id == "legal":
                device_id = generateLegalString(random.randint(0,100))
            else:
                device_id = random.choice([None, ""])

            energy_reading = EnergyReading.EnergyReading(device_id, watt_hours)
            reading_result = smart_energy_monitor.process_reading(energy_reading)
            
            if watt == "legal" and id == "legal":
                if reading_result.is_accepted():
                    print("test passed")
                else:
                    print("test failed")
            else:
                if reading_result.is_accepted():
                    print("test failed")
                else:
                    print("test passed")




if __name__ == "__main__":
    inputSpacePartitioning()