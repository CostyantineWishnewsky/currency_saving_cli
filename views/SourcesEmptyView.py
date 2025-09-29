
# from models.CurrencyExchangeRate import CurrencyExchangeRate
from models.SourceOfInformation import SourceOfInformation

class SourcesEmptyView:
    def __init__(self,sources_of_information:list[SourceOfInformation]):
        self._sources_of_information=sources_of_information
    def print(self)->None:
        print("#####################################")
        print("#    SourcesOfInformationView       #")
        print("#####################################")
        for source in self._sources_of_information:
            print(f'[{source.id}]:{source.name}')