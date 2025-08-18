from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from .configuracionExcepcionJornada import configuracionExcepcionJornada


class ConfiguracionExcepcion(Base):
    __tablename__ = "configuraciones_excepciones"

    id = Column(Integer, primary_key=True)
    veterinaria_id = Column(Integer, ForeignKey("veterinarias.id"), nullable=False)
    fecha = Column(String, nullable=False)
    veterinaria_id = Column(
        Integer,
        ForeignKey(
            "veterinarias.id",
        ),
        nullable=False,
    )
    veterinaria = relationship(
        "Veterinaria", back_populates="configuracion_excepciones"
    )

    jornadas = relationship(
        "Jornada",  # Nombre del modelo relacionado
        secondary=configuracionExcepcionJornada,  # Tabla intermedia que conecta ambos modelos
        back_populates="configuraciones_excepciones",  # Nombre del atributo inverso en Jornada
    )
