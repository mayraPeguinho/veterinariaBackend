from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


class Factura(Base):
    __tablename__ = "Facturas"

    id = Column(Integer, primary_key=True)

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)

    venta = relationship("Venta", back_populates="factura", uselist=False)
    detalles_facturas = relationship("DetalleFactura", back_populates="factura")
