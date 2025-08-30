from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class ServicioAtencion(Base):
    __tablename__ = "Servicios_Atenciones"

    id = Column(Integer, primary_key=True)
    servicio_id = Column(Integer, ForeignKey("Servicios.id"), nullable=False, primary_key=True)
    atencion_id = Column(Integer, ForeignKey("Atenciones.id"), nullable=False, primary_key=True)

    servicio = relationship("Servicio", back_populates="servicios_atenciones")
    atencion = relationship("Atencion", back_populates="servicios_atenciones")

    observacion = Column(String(255), nullable=True)
