
from dataclasses import dataclass


@dataclass
class CommandHelpInfo:
    id:int
    command_name:str
    examples:list[str]
    short_description:str
    description:str