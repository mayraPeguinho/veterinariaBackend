from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class EstadoAtencion(Base):
    __tablename__ = "EstadosAtencion"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)

    historial_estados_atenciones = relationship("HistorialEstadoAtencion", back_populates="estado_atencion")

