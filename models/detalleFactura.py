from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from .detalleFactura_servicio import detalleFactura_servicio


class DetalleFactura(Base):
    __tablename__ = "DetalleFacturas"

    id = Column(Integer, primary_key=True)
    borrado = Column(Boolean, nullable=False, default=False)  # Marca de borrado lógico

    factura_id = Column(Integer, ForeignKey("Facturas.id"), nullable=False)
    factura = relationship("Factura", back_populates="detalle_factura", uselist=False)

    detallefacturas_productos = relationship(
        "DetalleFacturaProducto", back_populates="detalle_factura"
    )
    servicios = relationship(
        "Servicio", secondary=detalleFactura_servicio, back_populates="detalle_facturas"
    )

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())

    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)
