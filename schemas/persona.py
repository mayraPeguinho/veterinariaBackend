from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Annotated
from utils.enums import GeneroEnum


class PersonaCreate(BaseModel):
    nombre: Annotated[str, Field(min_length=1, max_length=50)]
    apellido: Annotated[str, Field(min_length=1, max_length=50)]
    dni: Annotated[str, Field(min_length=6, max_length=20)]
    telefono: Annotated[str, Field(min_length=6, max_length=20)]
    genero: str  # Temporal: volver a string para debug
    direccion: Optional[Annotated[str, Field(max_length=100)]] = None
    email: EmailStr


class PersonaOut(BaseModel):
    id: int
    dni: str
    nombre: str
    apellido: str
    telefono: Optional[str]
    genero: Optional[GeneroEnum]
    direccion: Optional[str]
    email: EmailStr

    class Config:
        from_attributes = True
