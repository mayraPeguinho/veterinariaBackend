from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nombre_de_usuario = Column(
        String(50), nullable=False, unique=True, index=True
    )
    contrasenia = Column(String(128), nullable=False)

    rol_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    rol = relationship("Rol", back_populates="usuarios")

    persona_id = Column(Integer, ForeignKey("personas.id"), nullable=False, unique=True)
    persona = relationship("Persona", back_populates="usuario", uselist=False)

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())