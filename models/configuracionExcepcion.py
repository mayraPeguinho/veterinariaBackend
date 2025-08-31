from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, String
from sqlalchemy.orm import relationship
from .configuracionExcepcion_jornada import configuracionExcepcion_jornada


class ConfiguracionExcepcion(Base):
    __tablename__ = "ConfiguracionesExcepciones"

    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, nullable=False)
    veterinaria_id = Column(Integer, ForeignKey("Veterinarias.id"), nullable=False)
    veterinaria = relationship(
        "Veterinaria", back_populates="configuraciones_excepciones"
    )

    jornadas = relationship(
        "Jornada",  # Nombre del modelo relacionado
        secondary=configuracionExcepcion_jornada,  # Tabla intermedia que conecta ambos modelos
        back_populates="configuraciones_excepciones",  # Nombre del atributo inverso en Jornada
    )

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())

    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)
