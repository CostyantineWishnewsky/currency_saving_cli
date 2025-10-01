
from __globals import CACH_REPOSITORY,API_REPOSITORY

from support.ControllerResult import ControllerResult,ControllerResultStatus,OkData,ErrorData,RedirectData


from controllers.AuthenticationController import AuthenticationController
from controllers.DisplayInfoController import DisplayInfoController
from controllers.ExchangeRatesController import ExchangeRatesController
from controllers.SourcesController import SourcesController
from controllers.HelpController import HelpController

from views.statuses.ErrorView import ErrorView

ROUTER={
    'today':DisplayInfoController(cache_repository=CACH_REPOSITORY,api_repository=API_REPOSITORY).today,
    'exchange-rates':{
        'add':ExchangeRatesController(cache_repository=CACH_REPOSITORY).add,
        'remove':ExchangeRatesController(cache_repository=CACH_REPOSITORY).remove,
        'order':ExchangeRatesController(cache_repository=CACH_REPOSITORY).order,
    },
    'sources':{
        'avaliable':SourcesController(cache_repository=CACH_REPOSITORY,api_repository=API_REPOSITORY).avaliable,
        '':SourcesController(cache_repository=CACH_REPOSITORY,api_repository=API_REPOSITORY).empty,
    },
    'login':AuthenticationController(cache_repository=CACH_REPOSITORY,api_repository=API_REPOSITORY).login,
    'logout':AuthenticationController(cache_repository=CACH_REPOSITORY,api_repository=API_REPOSITORY).logout,
    'help':HelpController(cache_repository=CACH_REPOSITORY).help,
}


async def handle_controller_result(result:ControllerResult)->None:
    print(result)
    if result.status == ControllerResultStatus.Ok:
        return
    if result.status == ControllerResultStatus.Redirect:
        await ROUTER[result.data.route_to](result.data.arguments)
        return
    if result.status == ControllerResultStatus.Error:
        view=ErrorView(message=result.data.error_message)
        view.print()
        return
    return