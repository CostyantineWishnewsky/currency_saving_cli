
from models.CurrencyExchangeRate import CurrencyExchangeRate

class ExchangeRatesOrderView:
    def __init__(self,currency_exchange_rates:list[CurrencyExchangeRate]):
        self._currency_exchange_rates=currency_exchange_rates
    def print(self)->None:
        print("#####################################")
        print("#           DisplayInfoView         #")
        print("#####################################")
        