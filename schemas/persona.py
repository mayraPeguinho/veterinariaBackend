from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Optional, Annotated
from utils.enums import GeneroEnum
from schemas.responsable import ResponsableCreate, ResponsableOut
from schemas.empleado import EmpleadoCreate, EmpleadoOut


class PersonaCreate(BaseModel):
    nombre: Annotated[str, Field(min_length=1, max_length=50)]
    apellido: Annotated[str, Field(min_length=1, max_length=50)]
    dni: Annotated[str, Field(min_length=8, max_length=8, pattern="^\d{8}$")]
    telefono: Optional[str] = None
    genero: GeneroEnum
    direccion: Optional[Annotated[str, Field(max_length=100)]] = None
    email: Optional[EmailStr]


class PersonaEdit(PersonaCreate):
    nombre: Annotated[str, Field(min_length=1, max_length=50)]
    apellido: Annotated[str, Field(min_length=1, max_length=50)]
    telefono: Optional[str] = None
    genero: GeneroEnum
    direccion: Optional[Annotated[str, Field(max_length=100)]] = None
    email: Optional[EmailStr]
    responsable: Optional[ResponsableCreate] = None


class PersonaResponsableCreate(PersonaCreate):
    responsable: ResponsableCreate


class PersonaEmpleadoCreate(PersonaCreate):
    empleado: EmpleadoCreate = None


class PersonaOut(BaseModel):
    id: int
    dni: str
    nombre: str
    apellido: str
    telefono: Optional[str]
    genero: GeneroEnum
    direccion: Optional[str]
    email: Optional[EmailStr]

    model_config = ConfigDict(from_attributes=True)


class PersonaResponsableOut(PersonaOut):
    responsable: ResponsableOut


class PersonaEmpleadoOut(PersonaOut):
    empleado: EmpleadoOut
