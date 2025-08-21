from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from .atencion_producto import atencion_producto
from .empleado_atencion import empleado_atencion


class Atencion(Base):
    __tablename__ = "atenciones"

    id = Column(Integer, primary_key=True)
    causa = Column(String(100), nullable=False)
    diagnostico = Column(String(200), nullable=True)
    observacion = Column(String(200), nullable=True)
    inicio = Column(DateTime, nullable=False)  # Fecha y hora de inicio
    fin = Column(DateTime, nullable=True)  # Fecha y hora de fin
    borrado = Column(Boolean, nullable=False, default=False)

    animal_id = Column(Integer, ForeignKey("animales.id"), nullable=False)
    animal = relationship("Animal", back_populates="atenciones")
    archivos = relationship("Archivo", back_populates="atencion")
    productos = relationship(
        "Producto",
        secondary=atencion_producto,
        back_populates="atenciones"
    )


    turnos = relationship("Turno", back_populates="atencion")
    empleados = relationship(
        "Empleado", secondary=empleado_atencion, back_populates="atenciones"
    )
    servicios_atenciones = relationship("ServicioAtencion", back_populates="atencion")

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())
