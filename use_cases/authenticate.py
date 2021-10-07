from domain.authentication import Token
from repository.login.navitaire import LoginRepository

class Authenticate:
    def __init__(self, login_repository: LoginRepository):
        self.__login_repository = login_repository

    def execute(self) -> Token:
        token = self.__login_repository.login()
        return token