
from abc import ABC,abstractmethod

from support.dtos.CurrencyInfoRequest import CurrencyInfoRequest
from models.CurrencyExchangeRate import CurrencyExchangeRate
from models.SourceOfInformation import SourceOfInformation

class ApiRepository(ABC):
    @abstractmethod
    async def check_token(self,token:str)->bool:
        pass
    @abstractmethod
    async def get_currency_info(self,request:CurrencyInfoRequest)->list[CurrencyExchangeRate]:
        pass

    @abstractmethod
    async def get_avaliable_sources_of_information(self)->list[SourceOfInformation]:
        pass

