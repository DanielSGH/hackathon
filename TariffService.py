from abc import ABC, abstractmethod

class TariffService(ABC):
    @abstractmethod
    def get_current_tariff(self) -> float: # returns tariff in €/kWh
        pass