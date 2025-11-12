
from abc import ABC,abstractmethod

class View(ABC):
    @abstractmethod
    def show(self)->None:
        pass
