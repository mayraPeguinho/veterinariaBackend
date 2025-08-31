from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey


empleado_tipoServicio = Table(
    "Empleados_TiposServicio",
    Base.metadata,
    Column("empleado_id", Integer, ForeignKey("Empleados.id"), primary_key=True),
    Column(
        "tipo_servicio_id", Integer, ForeignKey("TiposServicio.id"), primary_key=True
    ),
)
