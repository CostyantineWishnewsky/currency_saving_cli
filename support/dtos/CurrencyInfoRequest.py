from dataclasses import dataclass
from datetime import datetime

@dataclass
class CurrencyInfoFilters:
    source_of_information:str
    time_from:datetime
    time_to:datetime

@dataclass
class CurrencyInfoRequest:
    token:str 
    currency_from:str 
    currency_to:str
    filters:CurrencyInfoFilters