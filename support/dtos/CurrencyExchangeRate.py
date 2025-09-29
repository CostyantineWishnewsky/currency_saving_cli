

from dataclasses import dataclass


@dataclass
class CurrencyExchangeRate:
    currency_from:str
    cyrrency_to:str
    value:int
    amount_of_numbers_after_point:int