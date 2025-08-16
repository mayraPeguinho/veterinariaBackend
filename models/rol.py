from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .asociaciones import roles_permisos

class Rol(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)

    permisos = relationship(
        "Permiso",
        secondary=roles_permisos,
        back_populates="roles"
    )
    usuarios = relationship("Usuario", back_populates="rol")