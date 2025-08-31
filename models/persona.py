from config.database import Base
from utils.enums import GeneroEnum
from sqlalchemy import Column, Integer, String, Enum as SqlEnum, DateTime, func
from sqlalchemy.orm import relationship


class Persona(Base):
    __tablename__ = "Personas"

    id = Column(Integer, primary_key=True)
    dni = Column(String(8), nullable=False, unique=True, index=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    telefono = Column(String(50), nullable=True)
    genero = Column(SqlEnum(GeneroEnum), nullable=False)
    direccion = Column(String(100), nullable=True)
    email = Column(String(50), nullable=True)

    usuario = relationship("Usuario", back_populates="persona", uselist=False)
    responsable = relationship("Responsable", back_populates="persona", uselist=False)
    facturas = relationship("Factura", back_populates="persona")
    empleado = relationship("Empleado", back_populates="persona", uselist=False)

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())

    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)
