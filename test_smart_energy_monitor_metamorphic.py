import SmartEnergyMonitor, TariffService, AlertService, EnergyReading, EnergySummary, ReadingResult

class DutchTariff(TariffService.TariffService):
    def get_current_tariff(self) -> float:
        return 1.0

class valueAlert(AlertService.Alertervice):
    def log_alert(self, device_id: str, watt_hours: float) -> None:
        print("device_id:", device_id, "watt_hours:", watt_hours)

#The value of get_summary should be equal to the sum of all devices' value
def test_metamorphic_summary():
    device0 = EnergyReading.EnergyReading("0", 3.5)
    device1 = EnergyReading.EnergyReading("1", 6.5)
    device2 = EnergyReading.EnergyReading("2", 10)
    tariffservice = DutchTariff()
    alertservice = valueAlert()
    anomalythreshold = 50.0
    sem = SmartEnergyMonitor.SmartEnergyMonitor(tariffservice, alertservice, anomalythreshold)
    sem.process_reading(device0)
    sem.process_reading(device1)
    sem.process_reading(device2)
    if sem.get_summary == device0.watt_hours + device1.watt_hours + device2.watt_hours:
        print("pass")
    else:
        print("fail")

#Reading order shouldn't affect the summary answer
def test_metamorphic_order():
    device0 = EnergyReading.EnergyReading("1", 3.5)
    device1 = EnergyReading.EnergyReading("2", 6.5)
    device2 = EnergyReading.EnergyReading("3", 10)
    tariffservice = DutchTariff()
    alertservice = valueAlert()
    anomalythreshold = 50.0
    sem0 = SmartEnergyMonitor.SmartEnergyMonitor(tariffservice, alertservice, anomalythreshold)
    sem0.process_reading(device0)
    sem0.process_reading(device1)
    sem0.process_reading(device2)
    sem1 = SmartEnergyMonitor.SmartEnergyMonitor(tariffservice, alertservice, anomalythreshold)
    sem1.process_reading(device2)
    sem1.process_reading(device1)
    sem1.process_reading(device0)
    if sem0.get_summary == sem1.get_summary:
        print("pass")
    else:
        print("fail")

test_metamorphic_summary()
test_metamorphic_order()