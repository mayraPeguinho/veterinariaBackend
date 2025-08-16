from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from empleadoCategoria import empleados_categorias
from empleadoTipoDeServicios import empleado_tipo_de_servicios
from empleadoTurno import empleado_turno


class Empleado(Base):
    __tablename__ = "empleados"
    id = Column(Integer, primary_key=True)
    numero_legajo = Column(Integer, nullable=False, unique=True)
    matricula = Column(String(200), nullable=True)
    fecha_ingreso = Column(DateTime, nullable=False)
    fecha_egreso = Column(DateTime, nullable=True)
    activo = Column(Boolean, nullable=False)
    observacion = Column(String(600), nullable=True)
    # Falta la relacion con persona
    configuracion_diaria_empleado = relationship(
        "ConfiguracionDiariaEmpleado", back_populates="empleado"
    )
    categorias = relationship(
        "Categoria", secondary=empleados_categorias, back_populates="empleados"
    )
    persona_id = Column(Integer, ForeignKey("personas.id"), nullable=False)

    tipo_de_servicios = relationship(
        "TipoDeServicios",
        secondary=empleado_tipo_de_servicios,
        back_populates="empleados",
    )
    turnos = relationship("Turno", secondary=empleado_turno, back_populates="empleados")
