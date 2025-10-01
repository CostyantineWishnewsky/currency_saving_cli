
from datetime import datetime

from support.ApiRepository import ApiRepository
from support.CacheRepository import CacheRepository

from support.dtos.CurrencyInfoRequest import CurrencyInfoRequest,CurrencyInfoFilters

from support.ControllerResult import ControllerResult
from support.ControllerResult_factories import result_redirect,result_ok_empty


from views.DisplayInfoTodayView import DisplayInfoTodayView

class DisplayInfoController:
    def __init__(self,cache_repository:CacheRepository,api_repository:ApiRepository):
        self._cache_repository=cache_repository
        self._api_repository=api_repository
    async def today(self,parameters:list[str])->ControllerResult:
        if len(parameters) == 0:
            currencies_exchange_rates=await self._cache_repository.get_today_currencies_exchange_rate()
            # print(len(currencies_exchange_rates))
            ####Making Request
            if len(currencies_exchange_rates)==0 :
                sources_of_information=await self._cache_repository.get_sources_of_information()
                # currency_exchange_rates=await self._cache_repository.get_currencies_exchange_rate()
                currency_exchange_rates=await self._cache_repository.get_today_currencies_exchange_rate()
                token=await self._cache_repository.get_token()
                
                time_format='%d-%d-%Y'
                today_datetime=datetime.now().strftime(time_format)
                filters=CurrencyInfoFilters(source_of_information=sources_of_information ,time_from=today_datetime,time_to=today_datetime)  

                # print(currencies_exchange_rates)
                # print(f'{currencies_exchange_rates[0].id}')
                # request=CurrencyInfoRequest(token=token,currency_from=currency_exchange_rates[0][0] ,currency_to=currency_exchange_rates[0][1] ,filters=filters)
                request=CurrencyInfoRequest(token=token,currency_from=currency_exchange_rates[0].currency_from ,currency_to=currencies_exchange_rates[0].currency_to  ,filters=filters)
                
                currencies_exchange_rates=await self._api_repository.get_currency_info(request=request)
                
            view=DisplayInfoTodayView(currency_exchange_rates=currencies_exchange_rates)
            view.print()
                
            
            return result_ok_empty()
        return result_redirect(route_to='help',arguments=['today'])