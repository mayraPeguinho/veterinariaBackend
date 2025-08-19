from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Estado(Base):
    __tablename__ = "estados"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)

    estado_turno = relationship("EstadoTurno", back_populates="estado")
