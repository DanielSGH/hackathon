class ReadingResult:
    def __init__(self, is_accepted: bool, total_watt_hours: float):
        self.is_accepted = is_accepted
        self.total_watt_hours = total_watt_hours

    @property
    def is_accepted(self) -> bool:
        return self.is_accepted

    @property
    def watt_hours(self) -> float:
        return self.watt_hours
