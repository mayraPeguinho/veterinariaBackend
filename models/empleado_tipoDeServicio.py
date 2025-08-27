from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey


empleado_tipoDeServicio = Table(
    "Empleados_TipoDeServicios",
    Base.metadata,
    Column("empleado_id", Integer, ForeignKey("Empleados.id"), primary_key=True),
    Column(
        "tipo_de_servicio_id",
        Integer,
        ForeignKey("TipoDeServicios.id"),
        primary_key=True
    ),
)
