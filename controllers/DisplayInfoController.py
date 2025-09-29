
from datetime import datetime

from support.ApiRepository import ApiRepository
from support.CacheRepository import CacheRepository

from support.dtos.CurrencyInfoRequest import CurrencyInfoRequest,CurrencyInfoFilters

from support.ControllerResult import ControllerResult
from support.ControllerResult_factories import result_redirect,result_ok_empty


class DisplayInfoController:
    def __init__(self,cache_repository:CacheRepository,api_repository:ApiRepository):
        self._cache_repository=cache_repository
        self._api_repository=api_repository
    async def today(self,parameters:list[str])->ControllerResult:
        #validate parameters amount of parameters should be 0 
        if len(parameters) == 0:
            # self._api_repository.get_currencies(request)
            #Check if needed exchange rates


            currencies_exchange_rates=self._cache_repository.get_today_currencies_exchange_rate()
            
            ####Making Request
            if currencies_exchange_rates != []:
                sources_of_information=self._cache_repository.get_sources_of_information()
                currency_exchange_rates=self._cache_repository.get_currencies_exchange_rate()
                token=self._cache_repository.get_token()
                
                time_format='%d-%d-%Y'
                today_datetime=datetime.now().strformat(time_format)
                filters=CurrencyInfoFilters(source_of_information=sources_of_information ,time_from=today_datetime,time_to=today_datetime)  

                request=CurrencyInfoRequest(token=token,currency_from=currency_exchange_rates[0][0] ,currency_to=currency_exchange_rates[0][1] ,filters=filters)

                response=await self._api_repository.get_currency_info(request=request)

            # return
            return result_ok_empty()
        return result_redirect(route_to='help',arguments=['today'])
        #got to the cache and check if there is todays data
        #if yes
        #   display
        #if no
        #go to cache and try to get token
        #if there is no token
        #   print error You need to be loggin
        #if yes
        #send request to server from api_repository
        #If got data
        #   display
        #If got time limite error
        #   print got time limit error status view
        #If got error from api
        #   print error from api status view

        #TODO here should be redirect to ROUTER['help'] for command today
        pass