
from PySide6.QtWidgets import QWidget

from core.View import View


class PySide6View(View):
    def __init__(self,page_widget:QWidget):
        self._page_widget=page_widget

    def show(self)->None:
        self._page_widget.show()
