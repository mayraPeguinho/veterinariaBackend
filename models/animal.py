from config.database import Base
from utils.enums import GeneroEnum
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Enum as SqlEnum,
    Boolean,
    DateTime,
    func,
    Date,
)
from sqlalchemy.orm import relationship


class Animal(Base):
    __tablename__ = "Animales"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    especie = Column(String(50), nullable=False)
    raza = Column(String(50), nullable=True)
    color = Column(String(30), nullable=True)
    peso = Column(String(20), nullable=True)
    tamanio = Column(String(30), nullable=True)
    temperamento = Column(String(50), nullable=True)
    sexo = Column(SqlEnum(GeneroEnum), nullable=False)
    alergias = Column(String(200), nullable=True)
    fecha_nacimiento = Column(Date, nullable=True)
    fecha_fallecimiento = Column(Date, nullable=True)
    borrado = Column(Boolean, nullable=False, default=False)

    responsable_id = Column(Integer, ForeignKey("Responsables.id"), nullable=False)
    responsable = relationship("Responsable", back_populates="animales",uselist=False)
    atenciones = relationship("Atencion", back_populates="animal")

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())
    turnos = relationship("Turno", back_populates="animal")
