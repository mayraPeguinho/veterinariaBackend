from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from .configuracionDiariaEmpleado_jornada import configuracionDiariaEmpleado_jornada


class ConfiguracionDiariaEmpleado(Base):
    __tablename__ = "ConfiguracionesDiariasEmpleados"

    id = Column(Integer, primary_key=True)
    fecha_dia_actual = Column(DateTime, nullable=False)
    observacion = Column(String(600), nullable=True)
    empleado_id = Column(Integer, ForeignKey("Empleados.id"))

    empleado = relationship("Empleado", back_populates="configuracion_diaria_empleado")

    jornadas = relationship(
        "Jornada",
        secondary=configuracionDiariaEmpleado_jornada,
        back_populates="configuraciones_diarias_empleados",
    )

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())

    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)
