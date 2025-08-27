from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

class HistorialEstadoTurno(Base):
    __tablename__ = "Historial_Estados_Turnos"

    id = Column(Integer, primary_key=True)
    turno_id = Column(Integer, ForeignKey("Turnos.id"), nullable=False)
    estado_turno_id = Column(Integer, ForeignKey("EstadosTurno.id"), nullable=False)
    
    observacion = Column(String(255), nullable=True)

    # Relaciones
    turno = relationship("Turno", back_populates="historial_estados_turnos")
    estado_turno = relationship("EstadoTurno", back_populates="historial_estados_turnos")

