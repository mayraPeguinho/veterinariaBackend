from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class TipoEstadoTurno(Base):
    __tablename__ = "TiposEstadoTurno"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)

    estados_turnos = relationship("EstadoTurno", back_populates="tipo_estado_turno")
