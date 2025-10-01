

from support.ApiRepository import ApiRepository
from support.CacheRepository import CacheRepository

from views.LoginView import LoginView
from views.statuses.SuccessView import SuccessView
from views.statuses.ErrorView import ErrorView


from support.ControllerResult import ControllerResult
from support.ControllerResult_factories import result_redirect,result_ok_empty


class AuthenticationController:
    def __init__(self,cache_repository:CacheRepository,api_repository:ApiRepository):
        self._cache_repository=cache_repository
        self._api_repository=api_repository

    async def login(self,parameters:list[str])->ControllerResult:
        if len(parameters) == 0:
            view=LoginView()
            view.print()    
            
            token=view.get_token()
            if token == None:
                error_view=ErrorView(message=view.get_error_message())
                error_view.print()
                return 
            
            if await self._api_repository.check_token(token):
                if await self._cache_repository.set_token(token):
                    success_view=SuccessView(message='Your are logged In')
                    success_view.print()
                    return
                error_view=ErrorView(message='Cannot Save token into the cache')
                error_view.print()
                return
            error_view=ErrorView(message='Authentication forbidden by server')
            error_view.print()
            return
        return result_redirect(route_to='help',arguments=['login'])
    
    async def logout(self,parameters:list[str])->ControllerResult:
        #validate parameters
        if len(parameters) == 0:
            await self._cache_repository.set_token('')
            view=SuccessView(message='You not loggedin')
            view.print()
            return
        return result_redirect(route_to='help',arguments=['logout'])
        