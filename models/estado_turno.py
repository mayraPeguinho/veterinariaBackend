from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func
from sqlalchemy.orm import relationship


class EstadoTurno(Base):
    __tablename__ = "Estados_Turnos"

    id = Column(Integer, primary_key=True)
    turno_id = Column(Integer, ForeignKey("Turnos.id"), nullable=False)
    tipo_estado_turno_id = Column(
        Integer, ForeignKey("TiposEstadoTurno.id"), nullable=False
    )

    observacion = Column(String(255), nullable=True)

    # Relaciones
    turno = relationship("Turno", back_populates="estados_turnos")
    tipo_estado_turno = relationship("TipoEstadoTurno", back_populates="estados_turnos")

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    usuario_creacion = Column(String(50), nullable=False)
