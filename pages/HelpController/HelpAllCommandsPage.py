
from models.CommandHelpInfo import CommandHelpInfo

class HelpAllCommandsPage:
    def __init__(self,command_help_infos:list[CommandHelpInfo]):
        self._command_help_infos=command_help_infos
    def print(self)->None:
        print("#####################################")
        print("#               HelpView            #")
        print("#####################################")
        for command_info in self._command_help_infos:
            print(f'{command_info.command_name} - {command_info.short_description}')
        