from abc import ABC, abstractmethod


class Alertervice(ABC):
    @abstractmethod
    def log_alert(self, device_id: str, watt_hours: float) -> None:
        pass