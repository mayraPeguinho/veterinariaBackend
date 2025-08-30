from datetime import datetime
from pydantic import BaseModel, Field


class UsuarioCreacion(BaseModel):
    nombre_de_usuario: str = Field(
        ..., min_length=3, max_length=50, description="Nombre de usuario"
    )
    contrasenia: str = Field(..., min_length=6, description="Contraseña del usuario")
    fecha_creacion: datetime = Field(
        default_factory=datetime.utcnow, description="Fecha de creación"
    )
    fecha_modificacion: datetime = Field(
        default_factory=datetime.utcnow, description="Fecha de modificación"
    )


class Usuario(UsuarioCreacion):
    id: int = Field(..., description="ID del usuario")

    # tambien podemos utilizar class  config  orm_mode = True le dice a Pydantic que acepte objetos que no sean diccionarios, sino instancias de clases (como los modelos de tu base de datos), y extraiga los atributos para construir la respuesta.
