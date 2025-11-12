
from abc import ABC,abstractmethod 


class Application(ABC):
    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def run(self):
        pass
