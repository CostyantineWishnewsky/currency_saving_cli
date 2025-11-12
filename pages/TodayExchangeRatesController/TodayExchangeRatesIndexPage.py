

from models.ExchangeRate import ExchangeRate



class TodayExchangeRatesIndexPage():
    def __init__(self,exchange_rates:list[ExchangeRate]):
        self._exchange_rates=exchange_rates

    def print(self)->None:
        print("TodayExchangeRates:")
        for item in self._exchange_rates:
            print(f"[{item.id}][{item.currency_from.name}->{item.currency_to.name}]={item.value} from {item.source_of_information.name}")
