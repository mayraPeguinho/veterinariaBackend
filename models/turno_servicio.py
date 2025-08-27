from config.database import Base
from sqlalchemy import (
    Table,
    Column,
    Integer,
    ForeignKey,
)  # Importa clases necesarias para definir tablas y columnas


turno_servicio = Table(
    "Turnos_Servicios",
    Base.metadata,
    Column("turno_id", Integer, ForeignKey("Turnos.id"), primary_key=True),
    Column("servicio_id", Integer, ForeignKey("Servicios.id"), primary_key=True),
)
