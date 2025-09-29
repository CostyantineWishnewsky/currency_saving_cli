
from dataclasses import dataclass
from models.Currency import Currency
from models.SourceOfInformation import SourceOfInformation

@dataclass
class CurrencyExchangeRateRule:
    id:int
    currency_from:Currency
    currency_to:Currency
    sources_of_information:list[SourceOfInformation]