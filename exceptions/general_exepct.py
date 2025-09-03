class APIException(Exception):
    def __init__(self, detail: str, status_code: int):
        self.detail = detail
        self.status_code = status_code
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
