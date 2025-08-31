from config.database import Base
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime,
    func,
    Numeric,
    Date,
    String,
)
from sqlalchemy.orm import relationship
from .atencion_producto import atencion_producto
from .servicio_producto import servicio_producto


class Producto(Base):
    __tablename__ = "Productos"

    id = Column(Integer, primary_key=True)
    costo = Column(Numeric(10, 2), nullable=False)  # Precio de costo actual
    stock = Column(Integer, nullable=False)  # Cantidad disponible
    precio = Column(Numeric(10, 2), nullable=False)  # Precio de venta actual
    fecha_desde = Column(Date, nullable=False)  # Inicio de vigencia
    fecha_hasta = Column(
        Date, nullable=True
    )  # Fin de vigencia (puede ser null si sigue vigente)

    tipo_producto_id = Column(
        Integer, ForeignKey("TiposProducto.id"), nullable=False
    )  # FK a tabla tipo de producto
    tipo_producto = relationship("TipoProducto", back_populates="productos")
    detallefacturas_productos = relationship(
        "DetalleFacturaProducto", back_populates="producto"
    )

    atenciones = relationship(
        "Atencion", secondary=atencion_producto, back_populates="productos"
    )

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())

    servicios = relationship(
        "Servicio", secondary=servicio_producto, back_populates="productos"
    )

    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)
