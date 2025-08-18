from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from .configuracionDiariaJornada import configuracionDiariaJornada
from .configuracionExcepcionJornada import configuracionExcepcionJornada


class Jornada(Base):
    __tablename__ = "jornadas"
    id = Column(Integer, primary_key=True)
    hora_inicio = Column(String, nullable=False)
    hora_fin = Column(String, nullable=False)

    configuraciones_diarias = relationship(
        "ConfiguracionDiaria",
        secondary=configuracionDiariaJornada,
        back_populates="jornadas",
    )

    configuraciones_excepciones = relationship(
        "ConfiguracionExcepcion",
        secondary=configuracionExcepcionJornada,
        back_populates="jornadas",
    )
