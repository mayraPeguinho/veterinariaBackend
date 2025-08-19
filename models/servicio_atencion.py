from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship


class ServicioAtencion(Base):
    __tablename__ = "servicios_atenciones"

    id = Column(Integer, primary_key=True)
    servicio_id = Column(Integer, ForeignKey("servicios.id"), nullable=False)
    atencion_id = Column(Integer, ForeignKey("atenciones.id"), nullable=False)

    servicio = relationship("Servicio", back_populates="servicio_atencion")
    atencion = relationship("Atencion", back_populates="servicio_atencion")

    observacion = Column(String(255), nullable=True)
