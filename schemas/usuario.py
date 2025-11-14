from pydantic import BaseModel, Field, ConfigDict, EmailStr
from schemas.persona import (
    PersonaResponsableCreate,
    PersonaEmpleadoCreate,
    PersonaEmpleadoOut,
    PersonaResponsableOut,
    PersonaEdit,
)
from utils.enums import RolEnum
from typing import Optional, List


class UsuarioEdit(BaseModel):
    nombre_de_usuario: Optional[str] = None
    email: Optional[EmailStr] = None
    # rol_id: RolEnum = Field(..., description="ID del rol del usuario")
    activo: bool = Field(..., description="Indica si el usuario está activo o inactivo")


class UsuarioActualEdit(BaseModel):
    persona: PersonaEdit
    nombre_de_usuario: Optional[str] = None
    email: Optional[EmailStr] = None
    contrasenia_nueva: Optional[str] = None
    contrasenia_actual: Optional[str] = None


class UsuarioExternoCreate(BaseModel):
    nombre_de_usuario: str = Field(..., min_length=3, max_length=50)
    contrasenia: str = Field(..., min_length=8)
    persona: PersonaResponsableCreate
    email: EmailStr


class UsuarioInternoCreate(UsuarioExternoCreate):
    rol_id: RolEnum = Field(..., description="ID del rol del usuario")
    persona: PersonaEmpleadoCreate


class UsuarioOutBase(BaseModel):
    id: int
    nombre_de_usuario: str
    rol_id: RolEnum
    persona_id: int
    email: EmailStr
    activo: bool = Field(..., description="Indica si el usuario está activo o inactivo")
    model_config = ConfigDict(from_attributes=True)


class UsuariosPaginado(BaseModel):
    total: int
    usuarios: List[UsuarioOutBase]


class UsuarioOut(UsuarioOutBase):
    persona: PersonaEmpleadoOut | PersonaResponsableOut
    persona_id: int = Field(exclude=True)
