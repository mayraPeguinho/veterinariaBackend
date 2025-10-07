from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from .empleado_categoria import empleado_categoria
from .empleado_tipoServicio import empleado_tipoServicio
from .empleado_turno import empleado_turno
from .empleado_atencion import empleado_atencion


class Empleado(Base):
    __tablename__ = "Empleados"
    id = Column(Integer, primary_key=True)
    numero_legajo = Column(Integer, nullable=False, unique=True)
    matricula = Column(String(200), nullable=True)
    fecha_ingreso = Column(DateTime, nullable=False)
    fecha_egreso = Column(DateTime, nullable=True)
    # activo = Column(Boolean, nullable=False)
    observacion = Column(String(600), nullable=True)

    persona_id = Column(Integer, ForeignKey("Personas.id"), nullable=False)

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)

    ventas = relationship("Venta", back_populates="empleado")
    persona = relationship("Persona", back_populates="empleado", uselist=False)
    categorias = relationship(
        "Categoria", secondary=empleado_categoria, back_populates="empleados"
    )
    tipo_servicios = relationship(
        "TipoServicio",
        secondary=empleado_tipoServicio,
        back_populates="empleados",
    )
    turnos = relationship("Turno", secondary=empleado_turno, back_populates="empleados")
    atenciones = relationship(
        "Atencion", secondary=empleado_atencion, back_populates="empleados"
    )
    configuracion_diaria_empleado = relationship(
        "ConfiguracionDiariaEmpleado", back_populates="empleado"
    )
    configuracion_excepcion_empleado = relationship(
        "ConfiguracionExcepcionEmpleado", back_populates="empleado"
    )
