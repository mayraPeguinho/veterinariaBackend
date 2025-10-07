from config.database import Base
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Time,
    Boolean,
    DateTime,
    func,
)
from sqlalchemy.orm import (
    relationship,
)
from .empleado_turno import empleado_turno
from .turno_servicio import turno_servicio


class Turno(Base):

    __tablename__ = "Turnos"
    id = Column(Integer, primary_key=True)

    hora_inicio = Column(Time, nullable=False)
    dia = Column(DateTime, nullable=False)
    modulo = Column(Integer, nullable=False)
    observacion = Column(String(600), nullable=True)

    tipo_turno_id = Column(Integer, ForeignKey("TiposTurno.id"), nullable=False)
    tipo_turno = relationship("TipoTurno", back_populates="turnos")

    animal_id = Column(Integer, ForeignKey("Animales.id"), nullable=False)
    animal = relationship("Animal", back_populates="turnos")

    atencion_id = Column(Integer, ForeignKey("Atenciones.id"), nullable=False)
    atencion = relationship("Atencion", back_populates="turnos")

    empleados = relationship(
        "Empleado", secondary=empleado_turno, back_populates="turnos"
    )
    estados_turnos = relationship("EstadoTurno", back_populates="turno")

    servicios = relationship(
        "Servicio", secondary=turno_servicio, back_populates="turnos"
    )

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())

    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)
