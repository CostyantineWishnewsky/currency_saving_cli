
from datetime import datetime

from support.ApiRepository import ApiRepository
from support.dtos.CurrencyInfoRequest import CurrencyInfoRequest

from models.CurrencyExchangeRate import CurrencyExchangeRate
from models.SourceOfInformation import SourceOfInformation
from models.Currency import Currency

from dataclasses import dataclass

@dataclass
class DateTimeSnapshot:
    data:list[CurrencyExchangeRate]

class MockupApiRepository(ApiRepository):
    def __init__(self):
        super().__init__()
        self._time_format='%d-%m-%Y'
        dollar_currency=Currency(id=0,name='usd')
        euro_currency=Currency(id=1,name='euro')
        hrivna_currency=Currency(id=2,name='uah')

        source_of_information1=SourceOfInformation(id=0,name='google.com')
        source_of_information2=SourceOfInformation(id=1,name='private bank')

        default_snapshot=DateTimeSnapshot(data=[
            CurrencyExchangeRate(id=0,currency_from=dollar_currency,currency_to=euro_currency,value=1300,amount_of_numbers_after_point=2,source_of_information=source_of_information1),
            CurrencyExchangeRate(id=1,currency_from=dollar_currency,currency_to=euro_currency,value=1300,amount_of_numbers_after_point=2,source_of_information=source_of_information2),

            CurrencyExchangeRate(id=2,currency_from=dollar_currency,currency_to=hrivna_currency,value=1300,amount_of_numbers_after_point=2,source_of_information=source_of_information1),
            CurrencyExchangeRate(id=3,currency_from=dollar_currency,currency_to=hrivna_currency,value=1300,amount_of_numbers_after_point=2,source_of_information=source_of_information2),

            CurrencyExchangeRate(id=4,currency_from=euro_currency,currency_to=hrivna_currency,value=1300,amount_of_numbers_after_point=2,source_of_information=source_of_information1),
            CurrencyExchangeRate(id=5,currency_from=euro_currency,currency_to=hrivna_currency,value=1300,amount_of_numbers_after_point=2,source_of_information=source_of_information2),

            CurrencyExchangeRate(id=6,currency_from=hrivna_currency,currency_to=euro_currency,value=1300,amount_of_numbers_after_point=2,source_of_information=source_of_information1),
            CurrencyExchangeRate(id=7,currency_from=hrivna_currency,currency_to=euro_currency,value=1300,amount_of_numbers_after_point=2,source_of_information=source_of_information2),

        ])  

        self._currency_info={
            datetime(year=2025,month=9,day=28,hour=0,minute=0,second=1):default_snapshot,
            datetime(year=2025,month=9,day=29,hour=0,minute=0,second=1):default_snapshot,
            datetime(year=2025,month=9,day=30,hour=0,minute=0,second=1):default_snapshot,
            datetime(year=2025,month=10,day=1,hour=0,minute=0,second=1):default_snapshot,

        }

    async def check_token(self,token:str)->bool:
        return True
    
    async def get_currency_info(self,request:CurrencyInfoRequest)->list[CurrencyExchangeRate]:
        output=[]
        for date,date_snapshot in self._currency_info.items():
            if date > request.filters.time_from and date < request.filters.time_to:
                for exchange_rate in self._currency_info[date].data:
                    if exchange_rate.source_of_information == request.filters.source_of_information:
                        output.append(exchange_rate)
                        continue
                    continue
            continue
        return output
        