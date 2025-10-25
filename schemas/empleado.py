from pydantic import BaseModel, Field, field_validator, model_serializer
from typing import Optional
from datetime import datetime, date


class EmpleadoCreate(BaseModel):
    numero_legajo: int
    matricula: Optional[str] = None
    fecha_ingreso: date = Field(
        example="15/10/2025",
        description="Formato esperado: dd/mm/aaaa",
    )
    observacion: Optional[str] = None

    @field_validator("fecha_ingreso", mode="before")
    def parsear_fecha(cls, v):
        if v is None or v == "":
            return None
        if isinstance(v, date) and not isinstance(v, datetime):
            return v
        if isinstance(v, datetime):
            return v.date()
        return datetime.strptime(v, "%d/%m/%Y").date()


class EmpleadoOut(EmpleadoCreate):
    id: int
    fecha_ingreso: date
    fecha_egreso: date | None = None

    @field_validator("fecha_ingreso", mode="before")
    def normalizar_fecha(cls, v):
        if isinstance(v, datetime):
            return v.date()
        return v

    @model_serializer
    def serialize_empleado(self):
        data = self.__dict__.copy()
        data["fecha_ingreso"] = (
            self.fecha_ingreso.strftime("%d/%m/%Y") if self.fecha_ingreso else None
        )
        data["fecha_egreso"] = (
            self.fecha_egreso.strftime("%d/%m/%Y") if self.fecha_egreso else None
        )
        return data
