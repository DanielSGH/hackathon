class EnergySummary:
    def __init__(self, total_watt_hours: float, total_cost: float, anomaly_count: int):
        self.anomaly_count
        self.total_cost
        self.total_watt_hours
    @property
    def total_watt_hours(self) -> float: ...
    @property
    def total_cost(self) -> float: ...
    @property
    def anomaly_count(self) -> int: ...