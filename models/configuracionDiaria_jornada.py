from config.database import Base
from sqlalchemy import (
    Table,
    Column,
    Integer,
    ForeignKey,
)  # Importa clases necesarias para definir tablas y columnas
from sqlalchemy.ext.declarative import (
    declarative_base,
)  # Importa la función para crear la base de modelos


# Define la tabla intermedia para Jornada y ConfiguracionDiaria (muchos a muchos)
configuracionDiaria_jornada = Table(
    "configuracion_diaria_jornada",
    Base.metadata,  # Nombre de la tabla y metadatos
    Column(
        "jornada_id", Integer, ForeignKey("jornada.id")
    ),  # Columna referenciando a Jornada
    Column(
        "configuracion_diaria_id", Integer, ForeignKey("configuracion_diaria.id")
    ),  # Columna referenciando a ConfiguracionDiaria
)
