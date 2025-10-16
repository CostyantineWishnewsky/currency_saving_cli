
from abc import ABC,abstractmethod

from models.ExchangeRate import ExchangeRate
from models.CommandHelpInfo import CommandHelpInfo

class CacheRepository(ABC):
    @abstractmethod
    async def setup(self)->None:
        pass

    @abstractmethod
    async def get_all_command_help_infos(self)->list[CommandHelpInfo]:
        pass

    @abstractmethod
    async def is_table_updated_today(self,table_name:str)->bool:
        pass

    @abstractmethod
    async def get_all_exchange_rates(self)->list[ExchangeRate]:
        pass

    @abstractmethod
    async def update_exchange_rates(self,updated_exchange_rates:list[ExchangeRate])->None:
        pass
    
    
    
