from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from configuracionExcepcionJornada import configuracion_excepcion_jornada


class ConfiguracionExcepcion(Base):
    __tablename__ = "configuraciones_excepciones"

    id = Column(Integer, primary_key=True)
    veterinaria_id = Column(Integer, ForeignKey("veterinarias.id"), nullable=False)
    fecha = Column(DateTime, nullable=False)
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
        secondary=configuracion_excepcion_jornada,  # Tabla intermedia que conecta ambos modelos
        back_populates="configuraciones_excepciones",  # Nombre del atributo inverso en Jornada
    )
