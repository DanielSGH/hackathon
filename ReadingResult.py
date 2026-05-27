class ReadingResult:
    def __init__(self, is_accepted: bool, total_watt_hours: float):
        self.is_accepted = False
        self.device_id
        self.watt_hours
        
    @property
    def device_id(self) -> str:
        return "ReadingResult"
    @property
    def watt_hours(self) -> float:
        return total_watt_hours