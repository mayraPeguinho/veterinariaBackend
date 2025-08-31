from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from .turno_servicio import turno_servicio
from .servicio_producto import servicio_producto
from .detalleFactura_servicio import detalleFactura_servicio


class Servicio(Base):

    __tablename__ = "Servicios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(600), nullable=True)
    precio = Column(Integer, nullable=False)
    modulo = Column(Integer, nullable=False)
    fecha_desde = Column(DateTime, nullable=True)
    fecha_hasta = Column(DateTime, nullable=True)
    borrador_logico = Column(Boolean, nullable=False, default=False)

    tipo_servicio_id = Column(Integer, ForeignKey("TiposServicio.id"), nullable=False)
    tipo_servicio = relationship("TipoServicio", back_populates="servicios")

    turnos = relationship("Turno", secondary=turno_servicio, back_populates="servicios")
    productos = relationship(
        "Producto", secondary=servicio_producto, back_populates="servicio_producto"
    )
    servicios_atenciones = relationship("ServicioAtencion", back_populates="servicio")

    detalle_facturas = relationship(
        "DetalleFactura", secondary=detalleFactura_servicio, back_populates="servicios"
    )

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())

    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)
