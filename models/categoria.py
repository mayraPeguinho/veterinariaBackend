from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Time, Boolean
from sqlalchemy.orm import relationship
from models.empleado_categoria import empleado_categoria


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    activo = Column(Boolean, nullable=False, default=True)

    empleado = relationship(
        "Empleado", secondary=empleado_categoria, back_populates="categorias"
    )
    tipo_de_servicio = relationship("TipoDeServicios", back_populates="categoria")
