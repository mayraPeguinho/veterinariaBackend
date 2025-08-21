from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .empleado_categoria import empleado_categoria
from .empleado_tipoDeServicio import empleado_tipoDeServicio
from .empleado_turno import empleado_turno
from .empleado_atencion import empleado_atencion


class Empleado(Base):
    __tablename__ = "empleados"
    id = Column(Integer, primary_key=True)
    numero_legajo = Column(Integer, nullable=False, unique=True)
    matricula = Column(String(200), nullable=True)
    fecha_ingreso = Column(DateTime, nullable=False)
    fecha_egreso = Column(DateTime, nullable=True)
    activo = Column(Boolean, nullable=False)
    observacion = Column(String(600), nullable=True)

    configuracion_diaria_empleado = relationship(
        "ConfiguracionDiariaEmpleado", back_populates="empleado"
    )
    ventas = relationship("Venta", back_populates="empleado")
    categorias = relationship(
        "Categoria", secondary=empleado_categoria, back_populates="empleados"
    )
    persona_id = Column(Integer, ForeignKey("personas.id"), nullable=False)
    persona = relationship("Persona", back_populates="empleado", uselist=False)

    tipo_de_servicios = relationship(
        "TipoDeServicio",
        secondary=empleado_tipoDeServicio,
        back_populates="empleados",
    )
    turnos = relationship("Turno", secondary=empleado_turno, back_populates="empleados")
    atenciones = relationship(
        "Atencion", secondary=empleado_atencion, back_populates="empleados"
    )
