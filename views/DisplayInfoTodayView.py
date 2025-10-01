
from models.CurrencyExchangeRate import CurrencyExchangeRate

class DisplayInfoTodayView:
    def __init__(self,currency_exchange_rates:list[CurrencyExchangeRate]):
        self._currency_exchange_rates=currency_exchange_rates
    def print(self)->None:
        print("#####################################")
        print("#           DisplayInfoView         #")
        print("#####################################")
        for exchange_rate in self._currency_exchange_rates:
            print(f'[{exchange_rate.id}]{exchange_rate.currency_from.name}->{exchange_rate.currency_to.name}:{float(exchange_rate.value/exchange_rate.amount_of_numbers_after_point)} from source {exchange_rate.source_of_information.name}')