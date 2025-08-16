from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from configuracionDiariaJornada import configuracion_diaria_jornada
from configuracionExcepcionJornada import configuracion_excepcion_jornada


class Jornada(Base):
    __tablename__ = "jornadas"
    id = Column(Integer, primary_key=True)
    hora_inicio = Column(String, nullable=False)
    hora_fin = Column(String, nullable=False)

    configuraciones_diarias = relationship(
        "ConfiguracionDiaria",
        secondary=configuracion_diaria_jornada,
        back_populates="jornadas",
    )

    configuraciones_excepciones = relationship(
        "ConfiguracionExcepcion",
        secondary=configuracion_excepcion_jornada,
        back_populates="jornadas",
    )
