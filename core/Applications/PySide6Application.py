
from PySide6.QtWidgets import QApplication

from core.Application import Application


class PySide6Appliction(Application):
    def __init__(self,command_line_parameters:list[str]):
        #sys.argv
        self._appliction=QApplication(command_line_parameters)

    def setup(self):
        pass

    def stop(self):
        pass

    def run(self):
        self._application.exec()
