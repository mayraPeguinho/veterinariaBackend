from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .rol_permiso import rol_permiso


class Permiso(Base):
    __tablename__ = "Permisos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(40), nullable=False)

    roles = relationship(
        "Rol",
        secondary=rol_permiso,
        back_populates="permisos"
    )
