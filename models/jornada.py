from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Time
from sqlalchemy.orm import relationship
from models.configuracionDiaria_jornada import configuracionDiaria_jornada
from models.configuracionExcepcion_jornada import configuracionExcepcion_jornada
from models.configuracionDiariaEmpleado_jornada import (
    configuracionDiariaEmpleado_jornada,
)


class Jornada(Base):
    __tablename__ = "jornadas"
    id = Column(Integer, primary_key=True)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)

    configuraciones_diarias = relationship(
        "ConfiguracionDiaria",
        secondary=configuracionDiaria_jornada,
        back_populates="jornadas",
    )

    configuraciones_excepciones = relationship(
        "ConfiguracionExcepcion",
        secondary=configuracionExcepcion_jornada,
        back_populates="jornadas",
    )
    configuraciones_diarias_empleados = relationship(
        "ConfiguracionDiariaEmpleado",
        secondary=configuracionDiariaEmpleado_jornada,
        back_populates="jornadas",
    )
