from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class VentaServicio(Base):
    __tablename__ = "Ventas_Servicios"

    id = Column(Integer, primary_key=True)
    venta_id = Column(Integer, ForeignKey("Ventas.id"), nullable=False)
    servicio_id = Column(Integer, ForeignKey("Servicios.id"), nullable=False)

    observacion = Column(String(255))

    # Relaciones
    venta = relationship("Venta", back_populates="ventas_servicios")
    servicio = relationship("Servicio", back_populates="ventas_servicios")
