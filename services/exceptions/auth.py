from exceptions.general import APIException


class CredencialesInvalidasException(APIException):
    def __init__(
        self,
        detail: str = "Credenciales inválidas.",
        status_code: int = 401,
    ):
        super().__init__(detail, status_code)


class PermisosInsuficientesException(APIException):
    def __init__(
        self,
        detail: str = "No posee los permisos necesarios.",
        status_code: int = 403,
    ):
        super().__init__(detail, status_code)
