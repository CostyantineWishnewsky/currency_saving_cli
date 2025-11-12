from dataclasses import dataclass
 
@dataclass
class CreateHelpControllerEvent:
    id:int 
    command_name:str = None
