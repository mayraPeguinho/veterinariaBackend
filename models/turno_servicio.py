from config.database import Base
from sqlalchemy import (
    Table,
    Column,
    Integer,
    ForeignKey,
)  # Importa clases necesarias para definir tablas y columnas


turno_servicio = Table(
    "turno_servicio",
    Base.metadata,
    Column("turno_id", Integer, ForeignKey("turnos.id"), primary_key=True),
    Column("servicio_id", Integer, ForeignKey("servicios.id"), primary_key=True),
)
