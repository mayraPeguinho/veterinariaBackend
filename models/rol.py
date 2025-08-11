from db.database import Base
from sqlalchemy import Column, Integer, String, Numeric


class Rol(Base):
    tablename = "roles"

    id = Column(Integer, primary_key=True)
    nombre: Column[str] = Column(String, nullable=False)