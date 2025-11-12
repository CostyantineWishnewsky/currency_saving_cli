

class ErrorPage():
    def __init__(self,error_message:str):
        self._error_message=error_message

    def print(self)->None:
        print(f"Oups Got Error:{self._error_message}")
