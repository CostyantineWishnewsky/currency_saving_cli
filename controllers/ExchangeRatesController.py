
from support.CacheRepository import CacheRepository

from views.ExchangeRatesAddView import ExchangeRatesAddView
from views.statuses.SuccessView import SuccessView

from support.ControllerResult import ControllerResult
from support.ControllerResult_factories import result_redirect,result_ok_empty


class ExchangeRatesController:
    def __init__(self,cache_repository:CacheRepository):
        self._cache_repository=cache_repository

    async def add(self,parameters:list[str])->ControllerResult:
        #validate amount of parameters there should be 0
        if len(parameters) == 0:
            currencies=self._cache_repository.get_list_of_currencies()
            #TODO check if currencies is not []

            # view=ExchangeRatesAddView(['uah','usd','euro'])
            view=ExchangeRatesAddView(currencies=currencies)
            view.print()

            if view._is_ok:
                currency_from=view.get_currency_from()
                currency_to=view.get_currency_to()

                

                success_view=SuccessView(message='Rule successfully added')
                success_view.print()
                return result_ok_empty()
            #     return
            #TODO here should be error result
            return result_ok_empty()
            # return
        return result_redirect(route_to='help',arguments=['exchange-rates'])
        #TODO here should be redirect to Help for command 'add'

        #opens input for currency_from separare view with list of currency_to
        #validate all currencies with list of all avaliable in cache
        #opens input for currency_to with list of currencies to
        #validate all currencies with list of all avaliable in cache
        #opens input with source of information and all for all
        #validate source of information input
        #if after validation error display error view
        #Create ExchangeRate and add to cacher
        #display Success View

        pass
    #TODO
    async def remove(self,parameters:list[str])->ControllerResult:
        #validate amount of parameters there should be 1
        #Opens Remove ExchangeRateView
        #input validate exchange rate id
        #if yes
        #   remove from cache
        #   display success view
        #if no
        #   display error view with no such rule with id,not get list currencies exchange use order command
        return result_redirect(route_to='help',arguments=['exchange-rates'])
    #TODO
    async def order(self,parameters:list[str])->ControllerResult:
        #validate amount of parameters there should be 0
        #get amount of ExchateRateViews from cache
        #create ExchangeRateView
        #display ExchangeRateView order
        return result_redirect(route_to='help',arguments=['exchange-rates'])
        