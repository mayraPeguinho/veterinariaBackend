from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey


empleado_turno = Table(
    "empleado_turno",
    Base.metadata,
    Column("empleado_id", Integer, ForeignKey("empleados.id"), primary_key=True),
    Column("turno_id", Integer, ForeignKey("turnos.id"), primary_key=True),
)
