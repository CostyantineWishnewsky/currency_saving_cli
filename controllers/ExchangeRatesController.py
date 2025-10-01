
from support.CacheRepository import CacheRepository

from views.ExchangeRatesAddView import ExchangeRatesAddView
from views.statuses.SuccessView import SuccessView

from support.ControllerResult import ControllerResult
from support.ControllerResult_factories import result_redirect,result_ok_empty,result_error


from views.statuses.ErrorView import ErrorView
from views.ExchangeRatesOrderView import ExchangeRatesOrderView

class ExchangeRatesController:
    def __init__(self,cache_repository:CacheRepository):
        self._cache_repository=cache_repository

    async def add(self,parameters:list[str])->ControllerResult:
        if len(parameters) == 0:
            currencies=await self._cache_repository.get_list_of_currencies()
            #TODO check if currencies is not []

            # view=ExchangeRatesAddView(['uah','usd','euro'])
            view=ExchangeRatesAddView(currencies=currencies)
            view.print()

            if view._is_ok:
                currency_from=view.get_currency_from()
                currency_to=view.get_currency_to()

                #TODO add Rule in cache

                success_view=SuccessView(message='Rule successfully added')
                success_view.print()
                return result_ok_empty()
            return result_ok_empty()
        return result_redirect(route_to='help',arguments=['exchange-rates'])
    #TODO
    async def remove(self,parameters:list[str])->ControllerResult:
        # Step 1: validate parameter count
        if len(parameters) == 1:
            # view=ErrorView(message="Exactly 1 parameter (exchange rate id) is required.")
            # view.print()
            # return result_error(error_message="Exactly 1 parameter (exchange rate id) is required.")
            # self._cache_repository.
            
            view=SuccessView(message='Rule has been removed')
            view.print()
        #exchange_rate_id = parameters[0]

        # Step 2: validate exchange rate id exists
        # i#f exchange_rate_id in self.cache:
        #     # Step 3: remove from cache
        #     del self.cache[exchange_rate_id]
        #     return self.success_view(exchange_rate_id)
        # else:
        #     # Step 4: display error
        #     return self.error_view(
        #         f"No such rule with id '{exchange_rate_id}'. "
        #         f"Use 'list_currencies_exchange' command to get available ones."
        #     )
        # validate amount of parameters there should be 1
        # Opens Remove ExchangeRateView
        # input validate exchange rate id
        # if yes
        #   remove from cache
        #   display success view
        # if no
        #   display error view with no such rule with id,not get list currencies exchange use order command
        return result_redirect(route_to='help',arguments=['exchange-rates'])
    #TODO
    async def order(self,parameters:list[str])->ControllerResult:
        #validate amount of parameters there should be 0
        if len(parameters) == 0:
            currency_exchange_rates=await self._cache_repository.get_today_currencies_exchange_rate()
            view=ExchangeRatesOrderView(currency_exchange_rates=currency_exchange_rates)
            view.print()
            return result_ok_empty()

        #get amount of ExchateRateViews from cache
        #create ExchangeRateView
        #display ExchangeRateView order
        return result_redirect(route_to='help',arguments=['exchange-rates'])
        