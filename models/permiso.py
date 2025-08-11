from db.database import Base
from sqlalchemy import Column, Integer, String, Numeric


class Permiso(Base):
    tablename = "permisos"

    id = Column(Integer, primary_key=True)
    nombre: Column[str] = Column(String, nullable=False)