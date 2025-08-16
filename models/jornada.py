from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Time
from sqlalchemy.orm import relationship
from configuracionDiariaJornada import configuracion_diaria_jornada
from configuracionExcepcionJornada import configuracion_excepcion_jornada
from configuracionDiariaEmpleadoJornada import configuracion_diaria_empleado_jornada


class Jornada(Base):
    __tablename__ = "jornadas"
    id = Column(Integer, primary_key=True)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)

    configuraciones_diarias = relationship(
        "ConfiguracionDiaria",
        secondary=configuracion_diaria_jornada,
        back_populates="jornadas",
    )

    configuraciones_excepciones = relationship(
        "ConfiguracionExcepcion",
        secondary=configuracion_excepcion_jornada,
        back_populates="jornadas",
    )
    configuraciones_diarias_empleados = relationship(
        "ConfiguracionDiariaEmpleado",
        secondary=configuracion_diaria_empleado_jornada,
        back_populates="jornadas",
    )
