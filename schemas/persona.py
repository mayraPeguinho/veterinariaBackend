from pydantic import BaseModel, EmailStr, constr, field_validator, Field
from typing import Optional


class PersonaCreate(BaseModel):
    dni: str = Field(..., min_length=6, max_length=20, strip_whitespace=True)
    nombre: str = Field(..., min_length=1, max_length=50, strip_whitespace=True)
    apellido: str = Field(..., min_length=1, max_length=50, strip_whitespace=True)
    telefono: Optional[str] = None
    genero: Optional[str] = None
    direccion: Optional[str] = None
    email: EmailStr


class PersonaOut(BaseModel):
    id: int
    dni: str
    nombre: str
    apellido: str
    telefono: Optional[str]
    genero: Optional[str]
    direccion: Optional[str]
    email: EmailStr

    class Config:
        from_attributes = True
