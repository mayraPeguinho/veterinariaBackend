from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Time, DateTime, func, Enum, String
from sqlalchemy.orm import relationship
from .configuracionDiaria_jornada import configuracionDiaria_jornada
from utils.enums import DiaSemanaEnum


class ConfiguracionDiaria(Base):
    __tablename__ = "ConfiguracionesDiarias"

    id = Column(Integer, primary_key=True)
    dia_semana = Column(Enum(DiaSemanaEnum), nullable=False)
    hora_apertura = Column(Time, nullable=False)  # Solo hora
    hora_cierre = Column(Time, nullable=False)  #  hora
    veterinaria_id = Column(Integer, ForeignKey("Veterinarias.id"), nullable=False)
    veterinaria = relationship("Veterinaria", back_populates="configuraciones_diarias")

    jornadas = relationship(
        "Jornada",  # Nombre del modelo relacionado
        secondary=configuracionDiaria_jornada,  # Tabla intermedia que conecta ambos modelos
        back_populates="configuraciones_diarias",  # Nombre del atributo inverso en Jornada
    )

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())

    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)
