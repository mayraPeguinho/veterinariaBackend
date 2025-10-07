from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship


class Venta(Base):
    __tablename__ = "Ventas"

    id = Column(Integer, primary_key=True)

    fecha_venta = Column(DateTime, nullable=False)  # Fecha de la venta
    modo_pago = Column(String(50), nullable=True)  # Ej: "Efectivo", "Tarjeta", etc.
    observacion = Column(String(255), nullable=True)  # Observaciones opcionales
    nombre_cliente = Column(String(100), nullable=False)  # Nombre del cliente

    factura_id = Column(Integer, ForeignKey("Facturas.id"))
    persona_id = Column(Integer, ForeignKey("Personas.id"))
    empleado_id = Column(Integer, ForeignKey("Empleados.id"), nullable=False)

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)

    factura = relationship("Factura", back_populates="venta", uselist=False)
    persona = relationship("Persona", back_populates="ventas")
    empleado = relationship("Empleado", back_populates="ventas")
    ventas_productos = relationship("VentaProducto", back_populates="venta")
    ventas_servicios = relationship("VentaServicio", back_populates="venta")
