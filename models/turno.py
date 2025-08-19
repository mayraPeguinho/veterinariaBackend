from config.database import Base
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Time,
    Boolean,
    DateTime,
)
from sqlalchemy.orm import (
    relationship,
)
from models.empleado_turno import empleado_turno
from turno_servicio import turno_servicio


class Turno(Base):
    id = Column(Integer, primary_key=True)

    hora_inicio = Column(Time, nullable=False)
    dia = Column(DateTime, nullable=False)
    modulo = Column(Integer, nullable=False)
    observacion = Column(String(600), nullable=True)
    borrador_logico = Column(Boolean, nullable=False, default=False)

    animal_id = Column(Integer, ForeignKey("animales.id"), nullable=False)
    animal = relationship("Animal", back_populates="turno")

    atenciones_id = Column(Integer, ForeignKey("atenciones.id"), nullable=False)
    atenciones = relationship("Atencion", back_populates="turno")

    empleados = relationship(
        "Empleado", secondary=empleado_turno, back_populates="turnos"
    )
    estado_turno = relationship("EstadoTurno", back_populates="turno")

    servicio_turno = relationship(
        "Servicio", secondary=turno_servicio, back_populates="turnos"
    )
