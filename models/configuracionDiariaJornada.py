from config.database import Base
from sqlalchemy import (
    Table,
    Column,
    Integer,
    ForeignKey,
)  # Importa clases necesarias para definir tablas y columnas

# Define la tabla intermedia para Jornada y ConfiguracionDiaria (muchos a muchos)
configuracionDiariaJornada = Table(
    "configuracion_diaria_jornada",
    Base.metadata,  # Nombre de la tabla y metadatos
    Column(
        "jornada_id", Integer, ForeignKey("jornadas.id")
    ),  # Columna referenciando a Jornada
    Column(
        "configuracion_diaria_id", Integer, ForeignKey("configuraciones_diarias.id")
    ),  # Columna referenciando a ConfiguracionDiaria
)
