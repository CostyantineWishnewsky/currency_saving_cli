
from enum import Enum
from typing import Union
from dataclasses import dataclass


class ControllerResultStatus(Enum):
    Ok = 0
    Error = 1
    Redirect = 2

@dataclass
class OkData:
    data:any

@dataclass
class ErrorData:
    error_message:str

@dataclass
class RedirectData:
    route_to:str
    arguments:list[str]



T=Union[OkData,ErrorData,RedirectData]
@dataclass
class ControllerResult:
    status:ControllerResultStatus
    data:T