import TariffService, AlertService, EnergyReading, EnergySummary, ReadingResult, SmartEnergyMonitor
import random
import string
import sys

def driver():
    # TariffService
    smart_energy_monitor = SmartEnergyMonitor(TariffService, AlertService, 100)
    # make an energyreading and process it, then call the tariffservice and see if the output is what is expected
    energy_reading = EnergyReading("testID", 50)
    smart_energy_monitor.process_reading(energy_reading)
    get_energy_summary = smart_energy_monitor.get_summary()
    
    # stub
    expected_energy_summary = EnergySummary(50 , 0.05 * smart_energy_monitor._tariff_svc.get_current_tariff, 0)
    
    if get_energy_summary == expected_energy_summary:
        print("pass")
    else:
        print("fail")

    # AlertService


