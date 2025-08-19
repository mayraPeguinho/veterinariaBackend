from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey


empleado_atencion = Table(
    "empleado_atencion",
    Base.metadata,
    Column("empleado_id", Integer, ForeignKey("empleados.id"), primary_key=True),
    Column("atencion_id", Integer, ForeignKey("atenciones.id"), primary_key=True),
)
