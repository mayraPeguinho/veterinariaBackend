from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .empleado_tipoDeServicios import empleado_tipoDeServicio


class TipoDeServicios(Base):
    __tablename__ = "tipo_de_servicios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(String(600), nullable=True)

    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    categoria = relationship("Categoria", back_populates="tipo_de_servicios")

    empleados = relationship(
        "Empleado",
        secondary=empleado_tipoDeServicio,
        back_populates="tipo_de_servicios",
    )

    servicios = relationship("Servicio", back_populates="tipo_de_servicio")
