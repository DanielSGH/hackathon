class EnergyReading:
        def __init__(self, device_id: str, watt_hours: float):
            self.device_id = device_id
            self.watt_hours = watt_hours

        @property
        def device_id(self) -> str:
            return self.device_id
        
        @property
        def watt_hours(self) -> float:
             return self.watt_hours