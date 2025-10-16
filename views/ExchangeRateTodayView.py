
from models.ExchangeRate import ExchangeRate

class ExchangeRateTodayView:
    def __init__(self,exchange_rates:list[ExchangeRate]):
        self._exchange_rates=exchange_rates
    def print(self)->None:
        print("#####################################")
        print("#      Exchange Rates Today View    #")
        print("#####################################")
        for exchange_rate in self._exchange_rates:
            print(f"{exchange_rate.currency_from.name}->{exchange_rate.currency_to.name}")
            print(f"{exchange_rate.value/exchange_rate.amount_of_numbers_after_point}")
            print(f"{exchange_rate.source_of_information.name}")
            print(' ')
        # for command_info in self._command_help_infos:
        #     print(f'{command_info.command_name} - {command_info.short_description}')
        