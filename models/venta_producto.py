from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Numeric
from sqlalchemy.orm import relationship


class VentaProducto(Base):
    __tablename__ = "Ventas_Productos"

    id = Column(Integer, primary_key=True)
    venta_id = Column(Integer, ForeignKey("Ventas.id"), nullable=False)
    producto_id = Column(Integer, ForeignKey("Productos.id"), nullable=False)

    cantidad = Column(Integer, nullable=False)  # 0 en caso de venderse fraccionado
    observacion = Column(
        String(255)
    )  # descripcion de que se vendio, en caso de que se venda fraccionado
    precio_de_venta = Column(
        Numeric(10, 2), nullable=False
    )  # En caso de que se venda fraccionado

    # Relaciones
    venta = relationship("Venta", back_populates="ventas_productos")
    producto = relationship("Producto", back_populates="ventas_productos")
