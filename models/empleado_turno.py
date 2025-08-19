from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey


empleado_turno = Table(
    "empleados_turnos",
    Base.metadata,
    Column("empleado_id", Integer, ForeignKey("empleados.id"), primary_key=True),
    Column("turno_id", Integer, ForeignKey("turnos.id"), primary_key=True),
)
