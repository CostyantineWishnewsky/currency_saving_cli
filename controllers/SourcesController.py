
from support.CacheRepository import CacheRepository
from views.SourcesEmptyView import SourcesEmptyView

from support.ControllerResult import ControllerResult
from support.ControllerResult_factories import result_redirect,result_ok_empty


class SourcesController:
    def __init__(self,cache_repository:CacheRepository):
        self._cache_repository=cache_repository

    # async def empty(self,parameters:list[str])->None:
    async def empty(self,parameters:list[str])->ControllerResult:
        print('empty')
        if len(parameters) == 0:
            sources_of_information=await self._cache_repository.get_sources_of_information()
            view=SourcesEmptyView(sources_of_information=sources_of_information)
            view.print()
            # return 
            return result_ok_empty()
        #TODO here should be redirect to help for the command
        #validate amount of parameters there should be 0
        #get all listenting exchange rates from the cacher
        #display them in the OrderView
        return result_redirect(route_to='help',arguments=['sources'])

    #TODO
    # async def avaliable(self,parameters:list[str])->None:
    async def avaliable(self,parameters:list[str])->ControllerResult:
        #validate amount of parameters there should be 0
        #   check if cache is updated today
        #   if yes
        #       print result from the cache
        #   if no
        #       make request thought api
        #       save result into the cache
        
        return result_redirect(route_to='help',arguments=['sources'])

    # async def add(self,parameters:list[str])->None:
        
    #     pass

    # async def remove(self,parameters:list[str])->None:
    #     pass