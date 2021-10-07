import requests
from rest_framework import exceptions


class Forbidden(exceptions.APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
        self.status_code = 403
        self.code = code or "forbidden"


class LoginTimeout(exceptions.APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
        self.status_code = 440
        self.code = code or "login_timeout"


class InternalServerError(exceptions.APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
        self.status_code = 500
        self.code = code or "internal_server_error"


class BadGateway(exceptions.APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
        self.status_code = 502
        self.code = code or "bad_gateway"


class GatewayTimeout(exceptions.APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
        self.status_code = 504
        self.code = code or "gateway_timeout"


def get_error_from_response(response):
    if not isinstance(response, requests.Response):
        return {"message": str(response)}
    exception_classes = {
        # 4xx
        400: exceptions.ValidationError,
        401: exceptions.PermissionDenied,
        403: Forbidden,
        404: exceptions.NotFound,
        405: exceptions.MethodNotAllowed,
        406: exceptions.NotAcceptable,
        415: exceptions.UnsupportedMediaType,
        440: LoginTimeout,
        # 5xx
        500: InternalServerError,
        502: BadGateway,
        504: GatewayTimeout,
    }
    exception_class = exception_classes.get(response.status_code) or exceptions.APIException
    try:
        errors = response.json().get("errors")
        return exception_class(detail={
            "message": errors[0]["rawMessage"],
            "status_code": response.status_code
        }, code=errors[0]["code"])
    except TypeError:
        # missing 1 required positional argument
        return exception_class(None, detail={
            "message": response.text,
            "status_code": response.status_code
        })
    except:
        return exception_class(detail={
            "message": response.text,
            "status_code": response.status_code
        })
