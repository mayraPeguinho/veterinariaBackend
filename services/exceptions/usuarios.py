from exceptions.general import APIException


class NumeroDocumentoAsignadoException(APIException):
    def __init__(
        self,
        detail: str = "El numero de documento ya está en uso.",
        status_code: int = 409,
    ):
        super().__init__(detail, status_code)


class UsuarioNoEncontradoException(APIException):
    def __init__(
        self,
        detail: str = "Usuario no encontrado",
        status_code: int = 404,
    ):
        super().__init__(detail, status_code)


class EditarUsuarioPropioException(APIException):
    def __init__(
        self,
        detail: str = "No puede editar su propio usuario desde esta sección",
        status_code: int = 400,
    ):
        super().__init__(detail, status_code)


class NombreUsuarioUsadoException(APIException):
    def __init__(
        self,
        detail: str = "El nombre de usuario ya está en uso.",
        status_code: int = 409,
    ):
        super().__init__(detail, status_code)


class EmailUsadoException(APIException):
    def __init__(
        self,
        detail: str = "El email ya está en uso.",
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


class UsuarioNoEncontradoException(APIException):
    def __init__(
        self,
        detail: str = "Usuario no encontrado.",
        status_code: int = 404,
    ):
        super().__init__(detail, status_code)
