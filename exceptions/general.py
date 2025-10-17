class APIException(Exception):
    def __init__(self, detail: str, status_code: int):
        self.detail = detail
        self.status_code = status_code
        self.message = detail  # Para compatibilidad con el handler
        super().__init__(detail)

    def __str__(self):
        return f"APIException(status_code={self.status_code}, detail={self.detail})"


class ErrorIntegridadReferencial(APIException):
    def __init__(
        self,
        detail: str = "Error de integridad referencial. Verificar los datos ingresados",
        status_code: int = 400,
    ):
        super().__init__(detail=detail, status_code=status_code)


class ErrorBaseDatos(APIException):
    def __init__(
        self,
        detail: str = "Error en la base de datos",
        status_code: int = 500,
    ):
        super().__init__(detail=detail, status_code=status_code)


class ErrorValidacion(APIException):
    def __init__(
        self,
        detail: str = "Error de validación de datos",
        status_code: int = 422,
    ):
        super().__init__(detail=detail, status_code=status_code)


class RecursoNoEncontrado(APIException):
    def __init__(
        self,
        detail: str = "Recurso no encontrado",
        status_code: int = 404,
    ):
        super().__init__(detail=detail, status_code=status_code)
