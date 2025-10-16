

from support.CacheRepository import CacheRepository
from support.ControllerResult import ControllerResult
from support.ControllerResult_factories import result_ok_empty,result_redirect

from views.ExchangeRateTodayView import ExchangeRateTodayView

class ExchangeRateController:
    def __init__(self,cache_repository:CacheRepository):
        self._cache_repository=cache_repository

    async def today(self,parameters:list[str])->ControllerResult:
        if len(parameters)!=0:
            if await self._cache_repository.is_table_updated_today('exchange_rates'):
                exchange_rates=await self._cache_repository.get_all_exchange_rates()
                view=ExchangeRateTodayView(exchange_rates=exchange_rates)
                view.print()

            #TODO here should be asking server
            #1 send request to server 
            #if error
            #   return to error view
            #if ok
            #add to cache
            #print ExchangeRateTodayView

            return result_ok_empty()
        return result_redirect("help",["today"])