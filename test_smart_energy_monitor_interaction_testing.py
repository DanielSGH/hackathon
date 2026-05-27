import SmartEnergyMonitor, TariffService, AlertService, EnergyReading, EnergySummary, ReadingResult

class DutchTariff(TariffService.TariffService):
    def get_current_tariff(self) -> float:
        return 1.0

class valueAlert(AlertService.Alertervice):
    def log_alert(self, device_id: str, watt_hours: float) -> None:
        print("device_id:", device_id, "watt_hours:", watt_hours)

def test_interaction_tariff_service():
    device0 = EnergyReading.EnergyReading("0", 3.5)
    tariffservice = DutchTariff()
    alertservice = valueAlert()
    anomalythreshold = 50.0
    sem = SmartEnergyMonitor.SmartEnergyMonitor(tariffservice, alertservice, anomalythreshold)
    if tariffservice == sem._tariff_svc:
        print("pass")
    else:
        print("fail")

def test_interaction_alert_service():
    device0 = EnergyReading.EnergyReading("0", 3.5)
    tariffservice = DutchTariff()
    alertservice = valueAlert()
    anomalythreshold = 50.0
    sem = SmartEnergyMonitor.SmartEnergyMonitor(tariffservice, alertservice, anomalythreshold)
    if alertservice == sem._alert_svc:
        print("pass")
    else:
        print("fail")

test_interaction_tariff_service()
test_interaction_alert_service()