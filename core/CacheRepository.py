
from abc import ABC,abstractmethod

from models.ExchangeRate import ExchangeRate
from models.CommandHelpInfo import CommandHelpInfo

class CacheRepository(ABC):
    @abstractmethod
    def setup(self)->None:
        pass

    @abstractmethod
    def is_setupped(self)->bool:
        pass

    @abstractmethod
    def get_all_command_help_infos(self)->list[CommandHelpInfo]:
        pass

    @abstractmethod
    def is_table_updated_today(self,table_name:str)->bool:
        pass

    @abstractmethod
    def get_all_exchange_rates(self)->list[ExchangeRate]:
        pass

    @abstractmethod
    def update_exchange_rates(self,updated_exchange_rates:list[ExchangeRate])->None:
        pass
    
    
    
