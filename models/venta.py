from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True)
    fecha_venta = Column(DateTime, nullable=False)        # Fecha de la venta
    modo_pago = Column(String(50), nullable=True)     # Ej: "Efectivo", "Tarjeta", etc.
    observacion = Column(String(255), nullable=True)  # Observaciones opcionales
    nombre_cliente = Column(String(100), nullable=False)      # Nombre del cliente
    borrado = Column(Boolean, nullable=False, default=False)  # Marca de borrado lógico

    persona_id = Column(Integer, ForeignKey("personas.id"), nullable=True)  # FK a tabla tipo de producto
    persona = relationship("Persona", back_populates="ventas", uselist=False)

    empleado_id = Column(Integer, ForeignKey("empleados.id"), nullable=True)  # FK a tabla tipo de producto
    empleado = relationship("Empleado", back_populates="ventas", uselist=False)

    venta_productos = relationship("VentaProducto", back_populates="venta")

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())
