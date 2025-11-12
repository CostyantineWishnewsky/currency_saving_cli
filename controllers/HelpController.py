
from core.Controller import Controller
from core.EventObserver import EventObserver
from core.Events.Controller.ControllerShowViewEvent import ControllerShowViewEvent

from core.Views.PythonStdTerminalView import PythonStdTerminalView

from pages.HelpController.HelpAllCommandsPage import HelpAllCommandsPage
from pages.HelpController.HelpForCommandPage import HelpForCommandPage

def create_HelpController_data(id:int,command_name:str = None)->dict:
    return {'id':id,'command':command_name}

class HelpController(Controller):
    def __init__(self,data:dict):
        super().__init__(data['id'])
        self._command_name=data["command"]
    def index(self):
        commands_infos=self._cache_repository.get_all_command_help_infos()    
        if self._command_name == None:
            self._window=PythonStdTerminalView(HelpAllCommandsPage(command_help_infos=commands_infos))
            return
        for command_info in commands_infos:
            if command_info.name == self._command_name:
                self._window=PythonStdTerminalView(HelpForCommandPage(command_help_info=command_info))
                return
        self._window=PythonStdTerminalView(HelpAllCommandsPage(command_help_infos=commands_infos))
