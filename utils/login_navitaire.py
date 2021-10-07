import json
import requests

from conf import settings
from rest_framework.request import Request

class LoginNavitaire:
    host = None
    __api_token = None
    request = None
    
    def __init__(self, request: Request):
        settings.NAVITAIRE_HOST = settings.NAVITAIRE_HOST
        self.__api_token = request.user.navitaire_token
        self.request = request

    def get_api_token(self):
        return self.__api_token


class SetNavitaireHost:
    def __init__(self, request):
        settings.NAVITAIRE_HOST = settings.NAVITAIRE_HOST
        self.__api_token = request.user.navitaire_token
        self.request = request

    def get_api_token(self):
        return self.__api_token