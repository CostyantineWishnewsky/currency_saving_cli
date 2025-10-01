
from models.CurrencyExchangeRate import CurrencyExchangeRate
from models.Currency import Currency
from views.statuses.ErrorView import ErrorView

class ExchangeRatesAddView:
    def __init__(self,currencies:list[Currency]):
    # def __init__(self,currencies:list[str]) -> None:
        self._currencies=currencies
        self._currency_from=None
        self._currency_to=None
        self._is_ok=False

    def get_currency_from(self)->str:
        return self._currency_from
    
    def get_currency_to(self)->str:
        return self._currency_to

    def print(self)->None:
        currency_names=[]
        for currency in self._currencies:
            currency_names.append(currency.name)
        currencies_line=f"[{currency_names[0]}"
        for currency in currency_names[1:]:
            currencies_line+=f",{currency}"
        currencies_line+="]"
        print("#####################################")
        print("#        ExchangeRatesAddView       #")
        print("#####################################")
        print(currencies_line)
        self._currency_from=input("Enter currency from:")
        if self._currency_from not in currency_names:
            error_view=ErrorView(message=f'currency_from should be from List,but got {self._currency_from}')
            error_view.print()
            return
        self._currency_to=input("Enter currency to:")
        if self._currency_to not in currency_names:
            error_view=ErrorView(message=f'currency_to should be from List,but got {self._currency_to}')
            error_view.print()
            return
        
        if self._currency_to == self._currency_from:
            error_view=ErrorView(message=f'currency_from and currency_to should be different')
            error_view.print()
            return
        self._is_ok=True