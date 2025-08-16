from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import relationship


class Empleado(Base):
    __tablename__ = "empleados"
    id = Column(Integer, primary_key=True)
    numero_legajo = Column(Integer, nullable=False, unique=True)
    matricula = Column(String, nullable=True)
    fecha_ingreso = Column(String, nullable=False)
    fecha_egreso = Column(String, nullable=True)
    activo = Column(Boolean, nullable=False)
    observacion = Column(String, nullable=True)
    # Falta la relacion con persona
    configuracion_diaria_empleado = relationship(
        "ConfiguracionDiariaEmpleado", back_populates="empleado"
    )
