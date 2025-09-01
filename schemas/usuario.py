from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from schemas.persona import PersonaCreate, PersonaOut


class UsuarioCreate(BaseModel):
    nombre_de_usuario: str = Field(..., min_length=3, max_length=50)
    contrasenia: str = Field(..., min_length=8)  # puedes agregar regex de complejidad
    rol: str = Field(..., description="Rol del usuario")
    persona: PersonaCreate


class UsuarioOut(BaseModel):
    id: int
    nombre_de_usuario: str
    rol: str
    persona: PersonaOut
    fecha_creacion: Optional[str] = None

    class Config:
        from_attributes = True
