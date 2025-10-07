from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .empleado_tipoServicio import empleado_tipoServicio


class TipoServicio(Base):
    __tablename__ = "TiposServicio"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(String(600), nullable=True)

    categoria_id = Column(Integer, ForeignKey("Categorias.id"), nullable=False)
    categoria = relationship("Categoria", back_populates="tipo_servicios")

    empleados = relationship(
        "Empleado",
        secondary=empleado_tipoServicio,
        back_populates="tipo_servicios",
    )

    servicios = relationship("Servicio", back_populates="tipo_servicio")
