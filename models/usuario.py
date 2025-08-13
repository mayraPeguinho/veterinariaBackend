from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric


class Permiso(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nombreDeUsuario: Column[str] = Column(
        String, nullable=False, unique=True, index=True
    )
    contraseña: Column[str] = Column(String, nullable=False)
