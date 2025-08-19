from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship


class EstadoTurno(Base):
    __tablename__ = "estados_turno"
    id = Column(Integer, primary_key=True)

    turno_id = Column(Integer, ForeignKey("turnos.id"), primary_key=True)
    estado_id = Column(Integer, ForeignKey("estados.id"), primary_key=True)

    turno = relationship("Turno", back_populates="estados")
    estado = relationship("Estado", back_populates="turnos")

    observacion = Column(String(600), nullable=True)
    fecha = Column(DateTime, nullable=False)
