
from abc import ABC,abstractmethod

from support.dtos.CurrencyExchangeRateRule import CurrencyExchangeRateRule
from models.SourceOfInformation import SourceOfInformation
from models.CurrencyExchangeRate import CurrencyExchangeRate
from models.CommandHelpInfo import CommandHelpInfo


class CacheRepository(ABC):
    @abstractmethod
    async def setup(self)->bool:
        pass

    @abstractmethod
    async def is_updated_today(self)->bool:
        pass

    @abstractmethod
    async def get_token(self)->str:
        pass
    @abstractmethod
    async def set_token(self,token:str)->bool:
        pass

    @abstractmethod
    async def add_currency(self,name:str)->bool:
        pass

    @abstractmethod
    async def get_list_of_currencies(self)->list[str]:
        pass

    @abstractmethod
    async def get_sources_of_information(self)->list[SourceOfInformation]:
        pass

    @abstractmethod
    async def add_currencies_exchange_rate_rule(self,exchange_rate_rule:CurrencyExchangeRateRule)->bool:
        pass


    @abstractmethod
    async def get_today_currencies_exchange_rate(self)->list[CurrencyExchangeRate]:
        pass
    
    @abstractmethod
    async def get_command_help_info_of(self,command_name:str)->CommandHelpInfo:
        pass

    @abstractmethod
    async def get_all_command_help_infos(self)->list[CommandHelpInfo]:
        pass