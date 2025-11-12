
from core.View import View


class PythonStdTerminalView(View):
    def __init__(self,page):
        super().__init__()
        self._page=page

    def show(self)->None:
        self._page.print()

