from exceptions.general import APIException


class NumeroDeLegajoAsignadoException(APIException):
    def __init__(
        self,
        detail: str = "El numero de legajo ya está en uso.",
        status_code: int = 409,
    ):
        super().__init__(detail, status_code)
