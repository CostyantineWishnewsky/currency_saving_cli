
from support.CacheRepository import CacheRepository

from support.dtos.CurrencyExchangeRateRule import CurrencyExchangeRateRule

from models.CurrencyExchangeRate import CurrencyExchangeRate
from models.Currency import Currency
from models.SourceOfInformation import SourceOfInformation
from models.CommandHelpInfo import CommandHelpInfo


class MemoryCacheRepository(CacheRepository):
    
    def __init__(self,token:str):
        super().__init__()
        self._token=None

        self._unique_sources_of_information_references={
            'google.com':1,
        }
        dollor_currency=Currency(id=0,name='usd')
        euro_currency=Currency(id=1,name='eur')
        hrivna_currency=Currency(id=2,name='uah')
        source_of_information1=SourceOfInformation(id=0,name='google.com')

        self._currencies=[
            dollor_currency,
            euro_currency,
            hrivna_currency,
        ]
        self._exchange_rates={
            'usd->eur__google.com':CurrencyExchangeRate(id=0,currency_from=dollor_currency,currency_to=euro_currency,value=1300,amount_of_numbers_after_point=2,source_of_information=source_of_information1),
        }

        self._sources_of_information=[
            source_of_information1,
        ]

        #TODO write examples later
        self._command_infos={
            'today':CommandHelpInfo(id=1,command_name='today',examples=[],short_description="prints today exachange rates",description=''),
            'exchange-rates':CommandHelpInfo(id=2,command_name='exchange-rates',examples=[],short_description='helps to control Your intersting exchange rates.',description=''),
            'sources':CommandHelpInfo(id=3,command_name='sources',examples=[],short_description='helps to control sources of information for exchange rates',description=''),
            'login':CommandHelpInfo(id=4,command_name='login',examples=[],short_description='login user in this program.It requires Your api token.',description=''),
            'logout':CommandHelpInfo(id=5,command_name='logout',examples=[],short_description='logout user from this program',description=''),
            'help':CommandHelpInfo(id=6,command_name='help',examples=[],short_description='prints short description of all commands and full description for specifice command',description=''),
        }

    async def setup(self)->bool:
        return True

    async def get_token(self)->str:
        return self._token
    
    async def set_token(self,token:str)->bool:
        self._token=token
        return True
    
    async def add_currency(self,name:str)->bool:
        new_index=len(self._currencies)
        currency=Currency(id=new_index,name=name)
        self._currencies.append(currency)
        return True

    
    async def get_list_of_currencies(self)->list[str]:
        return self._currencies
    
    async def get_sources_of_information(self)->list[SourceOfInformation]:
        return self._sources_of_information

    async def add_currencies_exchange_rate_rule(self,exchange_rate_rule:CurrencyExchangeRateRule)->bool:
        new_index=len(self._exchange_rates)+1
        for source_of_information in exchange_rate_rule.sources_of_information:
            exchange_rate=CurrencyExchangeRate(id=new_index,currency_from=exchange_rate_rule.currency_from,currency_to=exchange_rate_rule.currency_to,value=None,amount_of_numbers_after_point=None,source_of_information=source_of_information)
            if f'{exchange_rate_rule.currency_from}->{exchange_rate_rule.currency_to}__{source_of_information.name}' in self._exchange_rates.keys():
                continue
            self._exchange_rates[f'{exchange_rate_rule.currency_from}->{exchange_rate_rule.currency_to}__{source_of_information.name}']=exchange_rate
            new_index+=1
        return True

    async def get_today_currencies_exchange_rate(self)->list[CurrencyExchangeRate]:
        return self._exchange_rates.values()
    
    async def get_command_help_info_of(self,command_name:str)->CommandHelpInfo:
        if command_name in self._command_infos.keys():
            return self._command_infos[command_name]
        return None

    async def get_all_command_help_infos(self)->list[CommandHelpInfo]:
        return self._command_infos.values()