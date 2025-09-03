from pydantic import BaseModel, constr, EmailStr
from typing import Optional


class PersonaCreate(BaseModel):
    nombre: constr(
        min_length=1, max_length=50, strip_whitespace=True
    )  # pyright: ignore[reportInvalidTypeForm]
    apellido: constr(
        min_length=1, max_length=50, strip_whitespace=True
    )  # pyright: ignore[reportInvalidTypeForm]
    dni: constr(
        min_length=6, max_length=20, strip_whitespace=True
    )  # pyright: ignore[reportInvalidTypeForm]
    telefono: constr(
        min_length=6, max_length=20, strip_whitespace=True
    )  # pyright: ignore[reportInvalidTypeForm]
    genero: constr(
        min_length=1, max_length=20, strip_whitespace=True
    )  # pyright: ignore[reportInvalidTypeForm]
    direccion: Optional[constr(strip_whitespace=True, max_length=100)] = (
        None  # pyright: ignore[reportInvalidTypeForm]
    )
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
