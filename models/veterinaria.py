from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship


class Veterinaria(Base):
    __tablename__ = "veterinarias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    email = Column(String, nullable=True)
    instagram = Column(String, nullable=True)
    configuracion_diarias = relationship(  # configuracion_diarias hace ref al back_populates
        "ConfiguracionDiaria",
        back_populates="veterinaria",  # este nombre hace ref a la variabe que esta declarada en configuracionDiaria
    )
    configuracion_excepciones = relationship(  # configuracion_excepciones hace ref al back_populates
        "ConfiguracionExcepcion",
        back_populates="veterinaria",  # este nombre hace ref a la variabe que esta declarada en configuracionExcepcion
    )
