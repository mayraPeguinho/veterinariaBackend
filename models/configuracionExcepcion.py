from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship


class ConfiguracionExcepcion(Base):
    __tablename__ = "configuracion_excepcion"

    id = Column(Integer, primary_key=True)
    veterinaria_id = Column(Integer, ForeignKey("veterinarias.id"), nullable=False)
    fecha = Column(String, nullable=False)
    veterinaria = relationship("Veterinaria", back_populates="configuracion_diarias")
