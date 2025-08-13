from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric


class Permiso(Base):
    __tablename__ = "permisos"

    id = Column(Integer, primary_key=True)
    nombre: Column[str] = Column(String, nullable=False)
