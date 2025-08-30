from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

class HistorialEstadoAtencion(Base):
    __tablename__ = "Historial_Estados_Atenciones"

    id = Column(Integer, primary_key=True)
    atencion_id = Column(Integer, ForeignKey("Atenciones.id"), nullable=False)
    estado_atencion_id = Column(Integer, ForeignKey("EstadosAtencion.id"), nullable=False)
    
    observacion = Column(String(255), nullable=True)

    # Relaciones
    atencion = relationship("Atencion", back_populates="historial_estados_atenciones")
    estado_atencion = relationship("EstadoAtencion", back_populates="historial_estados_atenciones")

