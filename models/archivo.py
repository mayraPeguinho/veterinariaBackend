from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship


class Archivo(Base):
    __tablename__ = "Archivos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    ruta = Column(String(255), nullable=False)
    tipo = Column(String(50), nullable=True)  # Ej: "application/pdf"
    tamanio = Column(Integer, nullable=True)  # En bytes

    atencion_id = Column(Integer, ForeignKey("Atenciones.id"), nullable=False)
    atencion = relationship("Atencion", back_populates="archivos")

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())

    usuario_creacion = Column(String(50), nullable=False)
    usuario_modificacion = Column(String(50), nullable=True)
