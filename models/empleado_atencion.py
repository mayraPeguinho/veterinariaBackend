from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey


empleado_atencion = Table(
    "Empleados_Atenciones",
    Base.metadata,
    Column("empleado_id", Integer, ForeignKey("Empleados.id"), primary_key=True),
    Column("atencion_id", Integer, ForeignKey("Atenciones.id"), primary_key=True),
)
