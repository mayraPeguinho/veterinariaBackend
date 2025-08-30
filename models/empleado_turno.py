from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey


empleado_turno = Table(
    "Empleados_Turnos",
    Base.metadata,
    Column("empleado_id", Integer, ForeignKey("Empleados.id"), primary_key=True),
    Column("turno_id", Integer, ForeignKey("Turnos.id"), primary_key=True),
)
