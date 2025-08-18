from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class ConfiguracionDiariaEmpleado(Base):
    __tablename__ = "configuracion_diaria_empleado"
    id = Column(Integer, primary_key=True)
    fecha_dia_actual = Column(String, nullable=False)
    observacion = Column(String, nullable=True)
    id_empleado = Column(Integer, ForeignKey("empleados.id"))
    empleado = relationship("Empleado", back_populates="configuracion_diaria_empleado")
