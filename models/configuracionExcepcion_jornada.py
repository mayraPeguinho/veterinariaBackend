from config.database import Base
from sqlalchemy import (
    Table,
    Column,
    Integer,
    ForeignKey,
)  # Importa clases necesarias para definir tablas y columnas


configuracionExcepcion_jornada = Table(
    "configuraciones_excepciones_jornadas",
    Base.metadata,  # Nombre de la tabla y metadatos
    Column(
        "jornada_id", Integer, ForeignKey("jornadas.id")
    ),  # Columna referenciando a Jornada
    Column(
        "configuracion_excepcion_id", Integer, ForeignKey("configuraciones_excepciones.id")
    ),  # Columna referenciando a ConfiguracionExcepcion
)
