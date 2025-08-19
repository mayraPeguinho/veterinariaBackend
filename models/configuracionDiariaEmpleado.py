from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from configuracionDiariaEmpleadoJornada import configuracion_diaria_empleado_jornada


class ConfiguracionDiariaEmpleado(Base):
    __tablename__ = "configuracion_diaria_empleado"

    id = Column(Integer, primary_key=True)
    fecha_dia_actual = Column(DateTime, nullable=False)
    observacion = Column(String(600), nullable=True)
    id_empleado = Column(Integer, ForeignKey("empleados.id"))

    empleado = relationship("Empleado", back_populates="configuracion_diaria_empleado")

    jornadas = relationship(
        "ConfiguracionDiariaEmpleadoJornada",
        secondary=configuracion_diaria_empleado_jornada,
        back_populates="configuraciones_diarias_empleados",
    )
