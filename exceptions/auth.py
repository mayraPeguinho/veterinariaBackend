from exceptions.generalRepo import APIException


class NombreUsuarioUsadoException(APIException):
    def __init__(
        self,
        detail: str = "El nombre de usuario ya está en uso.",
        status_code: int = 409,
    ):
        super().__init__(detail, status_code)


class PersonaExistenteComoUsuarioException(APIException):
    def __init__(
        self,
        detail: str = "La persona ya existe como usuario.",
        status_code: int = 409,
    ):
        super().__init__(detail, status_code)


class RolInvalidoException(APIException):
    def __init__(
        self,
        detail: str = "Rol inválido.",
        status_code: int = 400,
    ):
        super().__init__(detail, status_code)


class CredencialesInvalidasException(APIException):
    def __init__(
        self,
        detail: str = "Credenciales inválidas.",
        status_code: int = 401,
    ):
        super().__init__(detail, status_code)


class UsuarioNoEncontradoException(APIException):
    def __init__(
        self,
        detail: str = "Usuario no encontrado.",
        status_code: int = 404,
    ):
        super().__init__(detail, status_code)
