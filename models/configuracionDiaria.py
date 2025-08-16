from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from configuracionDiariaJornada import configuracion_diaria_jornada


class ConfiguracionDiaria(Base):
    __tablename__ = "configuraciones_diarias"

    id = Column(Integer, primary_key=True)
    fecha = Column(String, nullable=False)
    hora_apertura = Column(String, nullable=False)
    hora_cierre = Column(String, nullable=False)
    veterinaria_id = Column(Integer, ForeignKey("veterinarias.id"), nullable=False)
    veterinaria = relationship("Veterinaria", back_populates="configuracion_diarias")

    jornadas = relationship(
        "Jornada",  # Nombre del modelo relacionado
        secondary=configuracion_diaria_jornada,  # Tabla intermedia que conecta ambos modelos
        back_populates="configuraciones_diarias",  # Nombre del atributo inverso en Jornada
    )
