
from pathlib import Path
from core.patterns.SingletonMeta import SingletonMeta


class UIData(metaclass=SingletonMeta):
    def __init__(self):
        self._pallete=None

        self._min_usuall_window_width=768
        self._min_usuall_window_height=640


        self._icon_pathes={
            "logo":"./assets/icons/logo.svg"
        }

    def set_pallete(self,palette)->None:
        self._pallete=palette

    def get_usuall_window_sizes(self)->(int,int):
        return (self._min_usuall_window_width,self._min_usuall_window_height)

    def get_window_bg_color(self)->str:
        return " "
    
    def get_text_color(self)->str:
        return " "
    
    def get_base_color(self)->str:
        return " "
    
    def get_highlight_color(self)->str:
        return " "
    
    def get_highlist_text_color(self)->str:
        return " "
    
    def load_svg_icon(self,name:str)->list[str]:
        return []
