
from models.CurrencyExchangeRate import CurrencyExchangeRate

from views.statuses.ErrorView import ErrorView

class ExchangeRatesAddView:
    # def __init__(self,currency_exchange_rates:list[CurrencyExchangeRate]):
    #     self._currency_exchange_rates=currency_exchange_rates
    def __init__(self,currencies:list[str]) -> None:
        self._currencies=currencies
        self._currency_from=None
        self._currency_to=None
        self._is_ok=False

    def get_currency_from(self)->str:
        return self._currency_from
    
    def get_currency_to(self)->str:
        return self._currency_to

    def print(self)->None:
        currencies_line=f"[{self._currencies[0]}"
        
        for currency in self._currencies[1:]:
            currencies_line+=f",{currency}"
        currencies_line+="]"
        print("#####################################")
        print("#        ExchangeRatesAddView       #")
        print("#####################################")
        print(currencies_line)
        self._currency_from=input("Enter currency from:")
        if self._currency_from not in self._currencies:
            error_view=ErrorView(message=f'currency_from should be from List,but got {self._currency_from}')
            error_view.print()
            return
        print(currencies_line)
        self._currency_to=input("Enter currency to:")
        if self._currency_to not in self._currencies:
            error_view=ErrorView(message=f'currency_to should be from List,but got {self._currency_to}')
            error_view.print()
            return
        
        if self._currency_to == self._currency_from:
            error_view=ErrorView(message=f'currency_from and currency_to should be different')
            error_view.print()
            return
        self._is_ok=True