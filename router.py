
# from __globals import CACH_REPOSITORY,API_REPOSITORY
from __globals import CACH_REPOSITORY

from support.ControllerResult import ControllerResult,ControllerResultStatus,OkData,ErrorData,RedirectData


# from controllers.AuthenticationController import AuthenticationController
# from controllers.DisplayInfoController import DisplayInfoController
# from controllers.ExchangeRatesController import ExchangeRatesController
# from controllers.SourcesController import SourcesController
from controllers.ExchangeRateController import ExchangeRateController
from controllers.HelpController import HelpController

from views.statuses.ErrorView import ErrorView

ROUTER={
    # 'today':DisplayInfoController(cache_repository=CACH_REPOSITORY,api_repository=API_REPOSITORY).today,
    # 'exchange-rates':{
    #     'add':ExchangeRatesController(cache_repository=CACH_REPOSITORY).add,
    #     'remove':ExchangeRatesController(cache_repository=CACH_REPOSITORY).remove,
    #     'order':ExchangeRatesController(cache_repository=CACH_REPOSITORY).order,
    # },
    # 'sources':{
    #     'avaliable':SourcesController(cache_repository=CACH_REPOSITORY,api_repository=API_REPOSITORY).avaliable,
    #     '':SourcesController(cache_repository=CACH_REPOSITORY,api_repository=API_REPOSITORY).empty,
    # },
    # 'login':AuthenticationController(cache_repository=CACH_REPOSITORY,api_repository=API_REPOSITORY).login,
    # 'logout':AuthenticationController(cache_repository=CACH_REPOSITORY,api_repository=API_REPOSITORY).logout,
    'today':ExchangeRateController(cache_repository=CACH_REPOSITORY).today,
    'help':HelpController(cache_repository=CACH_REPOSITORY).help,
}


async def handle_controller_result(result:ControllerResult)->None:
    # print(result)
    if result.status == ControllerResultStatus.Ok:
        return
    if result.status == ControllerResultStatus.Redirect:
        # await ROUTER[result.data.route_to](result.data.arguments)
        handle_controller_result(await ROUTER[result.data.route_to](result.data.arguments))
        # handle_controller_result(await)
        return
    if result.status == ControllerResultStatus.Error:
        view=ErrorView(message=result.data.error_message)
        view.print()
        return
    return