from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .rol_permiso import rol_permiso


class Rol(Base):
    __tablename__ = "Roles"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)

    permisos = relationship("Permiso", secondary=rol_permiso, back_populates="roles")
    usuarios = relationship("Usuario", back_populates="rol")
