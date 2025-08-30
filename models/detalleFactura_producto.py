from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class DetalleFacturaProducto(Base):
    __tablename__ = "DetalleFacturas_Productos"

    id = Column(Integer, primary_key=True)
    detalle_factura_id = Column(Integer, ForeignKey("DetalleFacturas.id"), nullable=False)
    producto_id = Column(Integer, ForeignKey("Productos.id"), nullable=False)
    
    cantidad = Column(Integer, nullable=False)

    # Relaciones
    detalle_factura = relationship("DetalleFactura", back_populates="detallefacturas_productos")
    producto = relationship("Producto", back_populates="detallefacturas_productos")

