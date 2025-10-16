from abc import ABC,abstractmethod

from models.ExchangeRate import ExchangeRate
from models.SourceOfInformation import SourceOfInformation

class ApiV1Repository(ABC):
    @abstractmethod
    async def get_today_exchange_rates(self,sources:list[SourceOfInformation])->list[ExchangeRate]:
        pass
    