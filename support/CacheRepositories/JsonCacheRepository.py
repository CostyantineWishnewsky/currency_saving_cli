
import json

from support.CacheRepository import CacheRepository

from models.CommandHelpInfo import CommandHelpInfo
from models.ExchangeRate import ExchangeRate


class JsonCacheRepository(CacheRepository):
    def __init__(self,path:str):
        self._path=path

        self._db_schema={
            "header":{
                "updated":{
                    "exchange_rates":"",
                }
            },
            "data":{
                "exchange_rates":{

                }
            }
        }

        self._commands_infos={
            
        }

    async def setup(self)->None:
        try:
            database=self._db_schema
            database["header"]["updated"]["exchange_rates"]=""
            with open(self._path,'w') as f:
                json.dump(database, f)
        except Exception as e:
            #TODO here
            pass
    
    async def get_all_command_help_infos(self)->list[CommandHelpInfo]:
        return []
   

    async def is_table_updated_today(self,table_name:str)->bool:
        pass


    async def get_all_exchange_rates(self)->list[ExchangeRate]:
        pass

    async def update_exchange_rates(self,updated_exchange_rates:list[ExchangeRate])->None:
        pass