import TariffService, AlertService, EnergyReading, EnergySummary, ReadingResult

class SmartEnergyMonitor:
    def __init__(self, tariff_svc: TariffService.TariffService,
                 alert_svc: AlertService.Alertervice,
                 anomaly_threshold: float):
        self._tariff_svc = tariff_svc
        self._alert_svc = alert_svc
        self._anomaly_threshold = anomaly_threshold
        self.result = ReadingResult.ReadingResult(True, 0)
        self.summary = EnergySummary.EnergySummary(0, 0, 0)

    def process_reading(self, reading: EnergyReading.EnergyReading) -> ReadingResult.ReadingResult:
        # Code to process the reading
        result: ReadingResult.ReadingResult = ReadingResult(True, reading.watt_hours)

        if reading == None:
            result.is_accepted = False
            raise ValueError('reading is None')
        
        if reading.device_id() == None or len(reading.device_id) == 0:
            result.is_accepted = False
            raise ValueError('device id is invalid')
        
        if reading.watt_hours() <= 0:
            result.is_accepted = False
            raise ValueError('watt_hours is invalid')

        self.summary = EnergySummary.EnergySummary(self.summary.total_watt_hours + reading.watt_hours, self.summary.total_cost + self._tariff_svc.get_current_tariff * reading.watt_hours, self.summary.anomaly_count)
        return ReadingResult.ReadingResult(True, self.result.watt_hours + reading.watt_hours)

    def get_summary(self) -> EnergySummary.EnergySummary:
        # Code to return the session summary
        return self.summary

    

    

    
