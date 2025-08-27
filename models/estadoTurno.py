from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class EstadoTurno(Base):
    __tablename__ = "EstadosTurno"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)

    historial_estados_turnos = relationship("HistorialEstadoTurno", back_populates="estado_turno")

