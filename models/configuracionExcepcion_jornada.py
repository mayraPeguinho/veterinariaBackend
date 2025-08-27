from config.database import Base
from sqlalchemy import (
    Table,
    Column,
    Integer,
    ForeignKey,
)  # Importa clases necesarias para definir tablas y columnas


configuracionExcepcion_jornada = Table(
    "ConfiguracionesExcepcionesJornadas",
    Base.metadata,  # Nombre de la tabla y metadatos
    Column(
        "jornada_id", Integer, ForeignKey("Jornadas.id"),
        
   primary_key=True),  # Columna referenciando a Jornada
    Column(
        "configuracion_excepcion_id", Integer, ForeignKey("ConfiguracionesExcepciones.id"),
    primary_key=True),  # Columna referenciando a ConfiguracionExcepcion
)
