from config.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    ForeignKey,
    Date,
    Time,
    DateTime,
)
from sqlalchemy.orm import relationship
from .configuracionDiariaJornada import configuracionDiariaJornada


class ConfiguracionDiaria(Base):
    __tablename__ = "configuraciones_diarias"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)  # Solo fecha
    hora_apertura = Column(DateTime, nullable=False)  # Solo hora
    hora_cierre = Column(DateTime, nullable=False)  # Fecha y hora
    veterinaria_id = Column(Integer, ForeignKey("veterinarias.id"), nullable=False)
    veterinaria = relationship("Veterinaria", back_populates="configuracion_diarias")

    jornadas = relationship(
        "Jornada",  # Nombre del modelo relacionado
        secondary=configuracionDiariaJornada,  # Tabla intermedia que conecta ambos modelos
        back_populates="configuraciones_diarias",  # Nombre del atributo inverso en Jornada
    )
