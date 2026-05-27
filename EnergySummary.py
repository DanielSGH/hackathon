class EnergySummary:
    def __init__(self, total_watt_hours: float, total_cost: float, anomaly_count: int):
        self.total_watt_hours = total_watt_hours
        self.total_cost = total_cost
        self.anomaly_count = anomaly_count

    @property
    def total_watt_hours(self) -> float:
        return self.total_watt_hours
    @property
    def total_cost(self) -> float:
        return self.total_cost
    
    @property
    def anomaly_count(self) -> int:
        return self.anomaly_count