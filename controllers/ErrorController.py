
from core.Controller import Controller

from core.Views.PythonStdTerminalView import PythonStdTerminalView

from pages.statuses.ErrorPage import ErrorPage

def create_ErrorController_data(id:int,error_message:str)->dict:
    return {'id':id,'error_message':error_message}

class ErrorController(Controller):
    def __init__(self,data:dict):
        super().__init__(data['id'])
        self._error_message=data['error_message']
        self._window=PythonStdTerminalView(page=ErrorPage(error_message=self._error_message))
    def index(self):
        self._window=PythonStdTerminalView(ErrorPage(error_message=self._error_message))
