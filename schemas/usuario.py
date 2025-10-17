from pydantic import BaseModel, Field, ConfigDict
from schemas.persona import (
    PersonaResponsableCreate,
    PersonaEmpleadoCreate,
    PersonaEmpleadoOut,
    PersonaResponsableOut,
)
from utils.enums import RolEnum


class UsuarioClienteCreate(BaseModel):
    nombre_de_usuario: str = Field(..., min_length=3, max_length=50)
    contrasenia: str = Field(..., min_length=8)
    persona: PersonaResponsableCreate


class UsuarioCreate(UsuarioClienteCreate):
    rol_id: RolEnum = Field(..., description="ID del rol del usuario")
    persona: PersonaResponsableCreate | PersonaEmpleadoCreate


class UsuarioOutBase(BaseModel):
    id: int
    nombre_de_usuario: str
    rol_id: RolEnum
    persona_id: int
    model_config = ConfigDict(from_attributes=True)


class UsuarioOut(UsuarioOutBase):

    persona: PersonaEmpleadoOut | PersonaResponsableOut
    persona_id: int = Field(exclude=True)
