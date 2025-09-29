
from models.CommandHelpInfo import CommandHelpInfo

class HelpForCommandView:
    def __init__(self,command_help_info:CommandHelpInfo):
        self._command_help_info=command_help_info
        
    def print(self)->None:
        print("#####################################")
        print("#      HelpForCommandView           #")
        print("#####################################")
        print(f"{self._command_help_info.command_name} - {self._command_help_info.description}")
        print("##############EXAMPLES###############")
        for line in self._command_help_info.examples:
            print(line)
        