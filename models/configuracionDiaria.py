from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship


class ConfiguracionDiaria(Base):
    __tablename__ = "configuracion_diaria"

    id = Column(Integer, primary_key=True)
    fecha = Column(String, nullable=False)
    hora_apertura = Column(String, nullable=False)
    hora_cierre = Column(String, nullable=False)
    veterinaria_id = Column(Integer, ForeignKey("veterinarias.id"), nullable=False)
    veterinaria = relationship("Veterinaria", back_populates="configuracion_diarias")
