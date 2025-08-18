from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, Boolean
from sqlalchemy.orm import relationship

class Responsable(Base):
    __tablename__ = "responsables"

    id = Column(Integer, primary_key=True)
    aceptaRecordatorios = Column(Boolean, nullable=False, default=False)
    borrado = Column(Boolean, nullable=False, default=False)

    persona_id = Column(Integer, ForeignKey("personas.id"), nullable=False, unique=True)
    persona = relationship("Persona", back_populates="responsable")

    animales = relationship("Animal", back_populates="responsable")

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())


