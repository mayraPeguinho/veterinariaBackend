from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class VentaProducto(Base):
    __tablename__ = "venta_producto"

    id = Column(Integer, primary_key=True)
    venta_id = Column(Integer, ForeignKey("ventas.id"), nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)

    # Relaciones
    venta = relationship("Venta", back_populates="venta_productos")
    producto = relationship("Producto", back_populates="venta_productos")
