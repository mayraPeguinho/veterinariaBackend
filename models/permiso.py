from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .asociaciones import roles_permisos


class Permiso(Base):
    __tablename__ = "permisos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(40), nullable=False)

    roles = relationship("Rol", secondary=roles_permisos, back_populates="permisos")
