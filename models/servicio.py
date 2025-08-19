from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .turno_servicio import turno_servicio
from .servicio_producto import servicio_producto


class Servicio(Base):

    __tablename__ = "servicios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(600), nullable=True)
    precio = Column(Integer, nullable=False)
    modulo = Column(Integer, nullable=False)
    fecha_desde = Column(DateTime, nullable=True)
    fecha_hasta = Column(DateTime, nullable=True)
    borrador_logico = Column(Boolean, nullable=False, default=False)

    tipo_de_servicio_id = Column(
        Integer, ForeignKey("tipo_de_servicios.id"), nullable=False
    )
    tipo_de_servicio = relationship("TipoDeServicio", back_populates="servicios")

    servicio_turno = relationship(
        "Turno", secondary=turno_servicio, back_populates="servicio_turno"
    )
    servicio_producto = relationship(
        "Producto", secondary=servicio_producto, back_populates="servicio_producto"
    )
    servicio_atencion = relationship("ServicioAtencion", back_populates="servicio")
