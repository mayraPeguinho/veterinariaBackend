from config.database import Base
from sqlalchemy import (
    Table,
    Column,
    Integer,
    ForeignKey,
)  # Importa clases necesarias para definir tablas y columnas

# Define la tabla intermedia para Jornada y ConfiguracionDiaria (muchos a muchos)
configuracionDiaria_jornada = Table(
    "ConfiguracionesDiarias_Jornadas",
    Base.metadata,  # Nombre de la tabla y metadatos
    Column(
        "jornada_id", Integer, ForeignKey("Jornadas.id"), primary_key=True),  # Columna referenciando a Jornada
    Column(
        "configuracion_diaria_id", Integer, ForeignKey("ConfiguracionesDiarias.id"), primary_key=True),  # Columna referenciando a ConfiguracionDiaria
)
