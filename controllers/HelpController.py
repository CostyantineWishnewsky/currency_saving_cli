

from support.CacheRepository import CacheRepository
from support.ControllerResult import ControllerResult
from support.ControllerResult_factories import result_ok_empty

from views.HelpView import HelpView
from views.HelpForCommandView import HelpForCommandView


class HelpController:
    def __init__(self,cache_repository:CacheRepository):
        self._cache_repository=cache_repository

    async def help(self,parameters:list[str])->ControllerResult:
        if len(parameters)==1:
            command_info=await self._cache_repository.get_command_help_info_of(command_name=parameters[0])
            view=HelpForCommandView(command_help_info=command_info)
            view.print()
            return
        command_infos=await self._cache_repository.get_all_command_help_infos()
        view=HelpView(command_help_infos=command_infos)
        view.print()
        # return
        return result_ok_empty()