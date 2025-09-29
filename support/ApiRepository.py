
from abc import ABC,abstractmethod

from support.dtos.CurrencyInfoRequest import CurrencyInfoRequest
from models.CurrencyExchangeRate import CurrencyExchangeRate


class ApiRepository(ABC):
    @abstractmethod
    async def check_token(self,token:str)->bool:
        pass
    @abstractmethod
    async def get_currency_info(self,request:CurrencyInfoRequest)->list[CurrencyExchangeRate]:
        pass

