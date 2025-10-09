from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from schemas.persona import PersonaCreate, PersonaOut
from schemas.rol import RolOut


class UsuarioCreate(BaseModel):
    nombre_de_usuario: str = Field(..., min_length=3, max_length=50)
    contrasenia: str = Field(..., min_length=8)
    # rol_id: int = Field(..., description="ID del rol del usuario", gt=0)
    persona: PersonaCreate


class UsuarioOut(BaseModel):
    id: int
    nombre_de_usuario: str
    rol_id: int
    persona_id: int
    fecha_creacion: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
