


class ErrorView:
    def __init__(self,message:str):
        self._message=message
    def print(self)->None:
        print("#####################################")
        print("#               ERROR               #")
        print("#####################################")
        if self._message!=None:
            print(self._message)