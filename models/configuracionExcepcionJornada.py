from config.database import Base
from sqlalchemy import (
    Table,
    Column,
    Integer,
    ForeignKey,
)  # Importa clases necesarias para definir tablas y columnas
from sqlalchemy.ext.declarative import declarative_base


configuracion_excepcion_jornada = Table(
    "configuraciones_excepciones_jornadas",
    Base.metadata,  # Nombre de la tabla y metadatos
    Column(
        "jornada_id", Integer, ForeignKey("jornada.id")
    ),  # Columna referenciando a Jornada
    Column(
        "configuracion_excepcion_id", Integer, ForeignKey("configuracion_excepcion.id")
    ),  # Columna referenciando a ConfiguracionExcepcion
)
