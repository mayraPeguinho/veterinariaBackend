from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from .configuracionExcepcionEmpleado_jornada import (
    configuracionExcepcionEmpleado_jornada,
)


class ConfiguracionExcepcionEmpleado(Base):
    __tablename__ = "ConfiguracionesExcepcionesEmpleados"

    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, nullable=False)

    empleado_id = Column(Integer, ForeignKey("Empleados.id"))
    empleado = relationship(
        "Empleado", back_populates="configuracion_excepcion_empleado"
    )

    jornadas = relationship(
        "Jornada",
        secondary=configuracionExcepcionEmpleado_jornada,
        back_populates="configuraciones_excepciones_empleados",
    )

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())

    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)
