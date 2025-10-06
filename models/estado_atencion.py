from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func
from sqlalchemy.orm import relationship


class EstadoAtencion(Base):
    __tablename__ = "Estados_Atenciones"

    id = Column(Integer, primary_key=True)
    atencion_id = Column(Integer, ForeignKey("Atenciones.id"), nullable=False)
    tipo_estado_atencion_id = Column(
        Integer, ForeignKey("TiposEstadoAtencion.id"), nullable=False
    )

    observacion = Column(String(255), nullable=True)

    # Relaciones
    atencion = relationship("Atencion", back_populates="estados_atenciones")
    tipo_estado_atencion = relationship(
        "TipoEstadoAtencion", back_populates="estados_atenciones"
    )

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    usuario_creacion = Column(String(50), nullable=False)
