
from getpass import getpass


class LoginView:
    def __init__(self):
        self._token=None
        self._error_message=None
    def get_token(self)->str:
        return self._token
    def get_error_message(self)->str:
        return self._error_message
    def print(self)->None:
        print("#####################################")
        print("#               LoginVIew           #")
        print("#####################################")
        token1 = getpass("Enter your token: ")
        token2 = getpass("Enter again: ")
        if token1 != token2:
            self._error_message='Error tokens should be equal'
            return
        self._token=token1