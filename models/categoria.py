from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from models.empleado_categoria import empleado_categoria


class Categoria(Base):
    __tablename__ = "Categorias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    activo = Column(Boolean, nullable=False, default=True)

    empleados = relationship(
        "Empleado", secondary=empleado_categoria, back_populates="categorias"
    )
    tipo_servicios = relationship("TipoServicio", back_populates="categoria")

    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())
