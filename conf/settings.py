from pathlib import Path
import environ
import redis
from urllib3.util import Retry
import requests
import logging
# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env(
    # set casting, default value
    NAVITAIRE_HOST=(str, "https://dotrezapi.test.vb.navitaire.com"),
    NAVITAIRE_USERNAME=(str, "AutomaticProcessIT"),
    NAVITAIRE_PASSWORD=(str, "Navitaire-4x"),
    NAVITAIRE_DOMAIN=(str, "EXT"),
    NAVITAIRE_CHANNEL_TYPE=(str, "API"),
    PRISMIC_ENDPOINT=(str, "https://vivaair-cms.cdn.prismic.io/api/v2"),
    PRISMIC_TOKEN=(
        str, "MC5ZQm1sWkJJQUFDRUFHVGpW.du-_vTwvK--_ve-_vRvvv73vv71d77-9Ne-_vUzvv73vv73vv71H77-9IO-_vQAx77-9RFph77-977-9WO-_vQ"),

    # ELASTIC_APM_HOST=(str, "https://local-apm.vivaair.com"),
    # ELASTIC_APM_SERVICE_NAME=(str, "BOOKING"),
    # ELASTIC_APM_SECRET_TOKEN=(str, "7YFDQ3F26hU8HWfb38A03b8o"),
    # ELASTIC_APM_ENVIRONMENT=(str, "development"),
    # ELASTIC_APM_DEBUG=(bool, True),
    # ELASTIC_APM_VERIFY_SERVER_CERT=(bool, False),
    REDIS_HOST=(str, "vivaair-redis-pdn.redis.cache.windows.net"),
    REDIS_PORT=(str, "6380"),
    REDIS_SSL=(bool, True),
    REDIS_DB_CACHE=(int, 0),
    REDIS_PASSWORD=(str, "YnZ00Yc3mr+fb3TcM7XyuVHflDYRWOnJexP152twfDU="),
    DPLY_VERSION=(str, "-1"),
    HTTP_POOL_SIZE=(int, 1),
    DEFAULT_RETRIES=(int, 1),
    REQUEST_TIMEOUT=(int, 20),
    CASHBACK_QUEUE=(str, "FELATA"),
    CASHBACK_ERROR_QUEUE=(str, "FCASER"),
    CASHBACK_ACTIVE=(bool, True),
    CASHBACK_TIME_LIMIT_GENERATION=(str, "2021-09-24 04:59:00Z"),
    CASHBACK_TIME_LIMIT_REDEMPTION=(str, "2021-09-26 11:59 PM"),
    EXTERNAL_EVENT_ID=(int, 11456),
    CASHBACK_PERCENTAGE=(int, 0.5),
    CASHBACK_LIMIT_COP=(float, 100000),
    CASHBACK_LIMIT_USD=(float, 30),
    CASHBACK_USERS=(list, ['FPWWWANONYMOUS'])
)

NAVITAIRE_HOST = env("NAVITAIRE_HOST")
NAVITAIRE_USERNAME = env("NAVITAIRE_USERNAME")
NAVITAIRE_PASSWORD = env("NAVITAIRE_PASSWORD")
NAVITAIRE_DOMAIN = env("NAVITAIRE_DOMAIN")
NAVITAIRE_CHANNEL_TYPE = env("NAVITAIRE_CHANNEL_TYPE")

PRISMIC_ENDPOINT = env("PRISMIC_ENDPOINT")
PRISMIC_TOKEN = env("PRISMIC_TOKEN")

REDIS_HOST = env("REDIS_HOST")
REDIS_PORT = env("REDIS_PORT")
REDIS_SSL = env("REDIS_SSL")
REDIS_PASSWORD = env("REDIS_PASSWORD")
REDIS_DB_CACHE = env("REDIS_DB_CACHE")

# ELASTIC_APM = {
#     # Set the required service name. Allowed characters:
#     # a-z, A-Z, 0-9, -, _, and space
#     'SERVICE_NAME': env("ELASTIC_APM_SERVICE_NAME"),

#     # Use if APM Server requires a secret token
#     'SECRET_TOKEN': env("ELASTIC_APM_SECRET_TOKEN"),

#     # Set the custom APM Server URL (default: http://localhost:8200)
#     'SERVER_URL': env("ELASTIC_APM_HOST"),

#     # Set the service environment
#     'ENVIRONMENT': env("ELASTIC_APM_ENVIRONMENT"),
#     'DEBUG': env("ELASTIC_APM_DEBUG"),
#     'VERIFY_SERVER_CERT': env("ELASTIC_APM_VERIFY_SERVER_CERT"),
#     "LOG_ECS_FORMATTING":"override",
#     "ELASTIC_APM_SANITIZE_FIELD_NAMES":["ACCTNO",]
# }

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'ecs': {
#             '()': 'ecs_logging.StdlibFormatter'
#         }
#     },
#     'handlers': {
#         'elasticapm': {
#             'level': 'WARNING',
#             'class': 'elasticapm.contrib.django.handlers.LoggingHandler',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         },
#         'ecsconsole': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'ecs'
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['console'],
#             'propagate': False,
#         },
#         'django.security': {
#             'handlers': ['console'],
#             'propagate': False,
#         },
#         'business_logic': {
#             'level': 'INFO',
#             'handlers': ['elasticapm'],
#             'propagate': False
#         },
#         'navitaire': {
#             'level': 'INFO',
#             'handlers': ['elasticapm'],
#             'propagate': False
#         },
#         'elasticapm.errors': {
#             'level': 'ERROR',
#             'handlers': ['console'],
#             'propagate': False,
#         },
#     },
# }




REDIS_POOL = redis.BlockingConnectionPool(host=REDIS_HOST,
                                          port='6379',
                                          password=REDIS_PASSWORD,
                                          socket_timeout=30
                                          )




HTTP_POOL_SIZE = env("HTTP_POOL_SIZE")
DEFAULT_RETRIES = env("DEFAULT_RETRIES")
REQUEST_TIMEOUT = env("REQUEST_TIMEOUT")

DEFAULT_TIMEOUT = 5  # seconds

CASHBACK_QUEUE = env("CASHBACK_QUEUE")
CASHBACK_ACTIVE = env("CASHBACK_ACTIVE")
CASHBACK_TIME_LIMIT_GENERATION = env("CASHBACK_TIME_LIMIT_GENERATION")
CASHBACK_TIME_LIMIT_REDEMPTION = env("CASHBACK_TIME_LIMIT_REDEMPTION")
CASHBACK_PERCENTAGE = env("CASHBACK_PERCENTAGE")
CASHBACK_LIMIT_COP = env("CASHBACK_LIMIT_COP")
CASHBACK_LIMIT_USD = env("CASHBACK_LIMIT_USD")
CASHBACK_USERS = env("CASHBACK_USERS")
CASHBACK_ERROR_QUEUE = env("CASHBACK_ERROR_QUEUE")


EXTERNAL_EVENT_ID = env("EXTERNAL_EVENT_ID")


class TimeoutHTTPAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)

SESSION_RETRY = retries = Retry(total=5, backoff_factor=1)

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

RETRY_STRATEGY = Retry(total=DEFAULT_RETRIES, backoff_factor=0.5)

class SessionManager(metaclass=Singleton):
    __init=False
    def initialize(self):
        if self.__init: return
        self.session = requests.Session()
        self.session.mount("http://", TimeoutHTTPAdapter(pool_maxsize=HTTP_POOL_SIZE, pool_block=True,
                                                         max_retries=RETRY_STRATEGY, timeout=int(REQUEST_TIMEOUT)))
        self.session.mount("https://", TimeoutHTTPAdapter(pool_maxsize=HTTP_POOL_SIZE, pool_block=True,
                                                          max_retries=RETRY_STRATEGY, timeout=int(REQUEST_TIMEOUT)))
        self.__init = True

    def get(self):
        return self.session

SessionManager().initialize()
