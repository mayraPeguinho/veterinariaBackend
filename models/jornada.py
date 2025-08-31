from config.database import Base
from sqlalchemy import Column, Integer, Time, DateTime, func, String
from sqlalchemy.orm import relationship
from .configuracionDiaria_jornada import configuracionDiaria_jornada
from .configuracionExcepcion_jornada import configuracionExcepcion_jornada
from .configuracionDiariaEmpleado_jornada import configuracionDiariaEmpleado_jornada


class Jornada(Base):
    __tablename__ = "Jornadas"
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

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())

    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)
