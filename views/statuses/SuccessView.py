


class SuccessView:
    def __init__(self,message:str):
        self._message=message
    def print(self)->None:
        print("#####################################")
        print("#               SUCCESS             #")
        print("#####################################")
        if self._message!=None:
            print(self._message)