from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


class Veterinaria(Base):
    __tablename__ = "Veterinarias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    email = Column(String, nullable=True)
    instagram = Column(String, nullable=True)
    configuraciones_diarias = relationship(  # configuracion_diarias hace ref al back_populates
        "ConfiguracionDiaria",
        back_populates="veterinaria",  # este nombre hace ref a la variabe que esta declarada en configuracionDiaria
    )
    configuraciones_excepciones = relationship(  # configuracion_excepciones hace ref al back_populates
        "ConfiguracionExcepcion",
        back_populates="veterinaria",  # este nombre hace ref a la variabe que esta declarada en configuracionExcepcion
    )
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())

    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)
