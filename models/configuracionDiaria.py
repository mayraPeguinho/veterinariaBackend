from config.database import Base
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Date,
    Time,
)
from sqlalchemy.orm import relationship
from .configuracionDiaria_jornada import configuracionDiaria_jornada


class ConfiguracionDiaria(Base):
    __tablename__ = "ConfiguracionesDiarias"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)  # Solo fecha
    hora_apertura = Column(Time, nullable=False)  # Solo hora
    hora_cierre = Column(Time, nullable=False)  # Fecha y hora
    veterinaria_id = Column(Integer, ForeignKey("Veterinarias.id"), nullable=False)
    veterinaria = relationship("Veterinaria", back_populates="configuraciones_diarias")

    jornadas = relationship(
        "Jornada",  # Nombre del modelo relacionado
        secondary=configuracionDiaria_jornada,  # Tabla intermedia que conecta ambos modelos
        back_populates="configuraciones_diarias",  # Nombre del atributo inverso en Jornada
    )
