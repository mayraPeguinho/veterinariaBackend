from pydantic import BaseModel, Field, field_validator, model_serializer
from typing import Optional
from datetime import datetime, date


class EmpleadoCreate(BaseModel):
    numero_legajo: int
    matricula: Optional[str] = None
    fecha_ingreso: Optional[date] = Field(
        None,
        example="15/10/2025",
        description="Formato esperado: dd/mm/aaaa",
    )
    observacion: Optional[str] = None

    @field_validator("fecha_ingreso", mode="before")
    def parsear_fecha(cls, v):
        if v is None or v == "":
            return None
        # Si ya es date, devolvelo
        if isinstance(v, date) and not isinstance(v, datetime):
            return v
        # Si es datetime, extraemos la fecha
        if isinstance(v, datetime):
            return v.date()
        # Si es string
        return datetime.strptime(v, "%d/%m/%Y").date()


class EmpleadoOut(BaseModel):
    fecha_ingreso: date
    fecha_egreso: date | None = None

    @field_validator("fecha_ingreso", mode="before")
    def normalizar_fecha(cls, v):
        if isinstance(v, datetime):
            return v.date()
        return v

    @model_serializer
    def serialize_empleado(self):
        return {
            "fecha_ingreso": (
                self.fecha_ingreso.strftime("%d/%m/%Y") if self.fecha_ingreso else None
            ),
            "fecha_egreso": (
                self.fecha_egreso.strftime("%d/%m/%Y") if self.fecha_egreso else None
            ),
        }
