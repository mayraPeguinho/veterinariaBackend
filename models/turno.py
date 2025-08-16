from config.database import Base
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Time,
    Boolean,
    DateTime,
)  # Import necessary classes to define tables
from sqlalchemy.orm import (
    relationship,
)  # Import relationship to define many-to-many relationships
from empleadoTurno import empleado_turno


class Turno(Base):
    id = Column(Integer, primary_key=True)  # Primary key for the Turno table

    hora_inicio = Column(Time, nullable=False)
    dia = Column(DateTime, nullable=False)
    modulo = Column(Integer, nullable=False)
    observacion = Column(String(600), nullable=True)
    borrador_logico = Column(Boolean, nullable=False, default=False)

    empleado = relationship("Empleado", back_populates="turnos")
    animal_id = Column(Integer, ForeignKey("animales.id"), nullable=False)
    animal = relationship("Animal", back_populates="turno")
    atenciones_id = Column(Integer, ForeignKey("atenciones.id"), nullable=False)
    atenciones = relationship("Atencion", back_populates="turno")

    empleados = relationship(
        "Empleado", secondary=empleado_turno, back_populates="turnos"
    )
