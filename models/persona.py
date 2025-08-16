from config.database import Base
from utils.enums import GeneroEnum
from sqlalchemy import Column, Integer, String, Enum as SqlEnum
from sqlalchemy.orm import relationship

class Persona(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True)
    dni = Column(
        String(8), nullable=False, unique=True, index=True
    )
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    telefono = Column(String(50), nullable=True)
    genero = Column(SqlEnum(GeneroEnum), nullable=False)
    direccion = Column(String(100), nullable=True)
    email = Column(String(50), nullable=True)

    usuario = relationship("Usuario", back_populates="persona", uselist=False)
    responsable = relationship("Responsable", back_populates="persona", uselist=False)
    ventas = relationship("Venta", back_populates="persona")


