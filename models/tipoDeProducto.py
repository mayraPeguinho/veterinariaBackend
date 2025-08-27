from config.database import Base
from sqlalchemy import Column, Integer, DateTime, func, String, Boolean
from sqlalchemy.orm import relationship


class TipoDeProducto(Base):
    __tablename__ = "TipoDeProductos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)  # Nombre del tipo de producto
    descripcion = Column(String(255), nullable=True)  # Descripción opcional
    marca = Column(String(100), nullable=True)  # Marca asociada
    venta_libre = Column(
        Boolean, nullable=False
    )  # Si es de venta libre o requiere receta

    productos = relationship("Producto", back_populates="tipo_de_producto")

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())
