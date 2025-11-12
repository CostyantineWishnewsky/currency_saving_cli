
from core.Controller import Controller
from core.Views.PythonStdTerminalView import PythonStdTerminalView

from core.EventObserver import EventObserver
from core.Events.ControllerCreator.GotErrorEvent import GotErrorEvent


from pages.TodayExchangeRatesController.TodayExchangeRatesIndexPage import TodayExchangeRatesIndexPage

def create_TodayExchangeRatesController_data(id:int)->dict:
    return {'id':id}


class TodayExchangeRatesController(Controller):
    def __init__(self,data:dict):
        super().__init__(data['id'])

    def index(self):
        try:
            if self._cache_repository.is_setupped()==False:
                self._cache_repository.setup()
            if self._cache_repository.is_table_updated_today('exchange_rates'):
                exchange_rates=self._cache_repository.get_all_exchange_rates()
                self._window=PythonStdTerminalView(TodayExchangeRatesIndexPage(exchange_rates))
                return
            exchange_rates=self._api_repository.get_today_exchange_rates()
            if exchange_rates == None:
                return
            self._cache_repository.update_exchange_rates(exchange_rates)
            self._window=PythonStdTerminalView(TodayExchangeRatesIndexPage(exchange_rates))
        except Exception as e:
            event_observer=EventObserver()

            error_handling_id=event_observer.get_id_by_name('error_handling')
            event_observer.notify(GotErrorEvent(error_handling_id,error_message=e))
            return
