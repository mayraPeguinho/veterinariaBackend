from exceptions.general_exepct import APIException


class NombreUsuarioUsadoException(APIException):
    def __init__(
        self,
        message: str = "El nombre de usuario ya está en uso.",
        status_code: int = 404,
    ):
        super().__init__(message, status_code)


class PersonaExistenteComoUsuarioException(APIException):
    def __init__(
        self,
        message: str = "La persona ya existe como usuario.",
        status_code: int = 409,
    ):
        super().__init__(message, status_code)


class RolInvalidoException(APIException):
    def __init__(
        self,
        message: str = "Rol inválido.",
        status_code: int = 400,
    ):
        super().__init__(message, status_code)
