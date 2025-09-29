
from dataclasses import dataclass

from models.Currency import Currency
from models.SourceOfInformation import SourceOfInformation


@dataclass
class CurrencyExchangeRate:
    id:int
    currency_from:Currency
    currency_to:Currency
    value:int 
    amount_of_numbers_after_point:int
    source_of_information:SourceOfInformation
