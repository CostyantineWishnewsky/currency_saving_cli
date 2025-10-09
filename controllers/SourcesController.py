
from support.CacheRepository import CacheRepository
from support.ApiRepository import ApiRepository

from support.ControllerResult import ControllerResult
from support.ControllerResult_factories import result_redirect,result_ok_empty

from views.SourcesAvaliable import SourcesAvaliableView
from views.SourcesEmptyView import SourcesEmptyView

class SourcesController:
    def __init__(self,cache_repository:CacheRepository,api_repository:ApiRepository):
        self._cache_repository=cache_repository
        self._api_repository=api_repository

    async def empty(self,parameters:list[str])->ControllerResult:
        if len(parameters) == 0:
            sources_of_information=await self._cache_repository.get_sources_of_information()
            view=SourcesEmptyView(sources_of_information=sources_of_information)
            view.print()
            return result_ok_empty()
        return result_redirect(route_to='help',arguments=['sources'])
    async def avaliable(self,parameters:list[str])->ControllerResult:
        if len(parameters) == 0:
            sources_of_information=await self._api_repository.get_avaliable_sources_of_information()
            view=SourcesAvaliableView(sources_of_information=sources_of_information)
            view.print()
            return result_ok_empty()
        return result_redirect(route_to='help',arguments=['sources'])