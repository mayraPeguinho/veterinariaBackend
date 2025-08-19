from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey, MetaData


empleado_tipoDeServicios = Table(
    "empleados_tipo_de_servicios",
    Base.metadata,
    Column("empleado_id", Integer, ForeignKey("empleados.id"), primary_key=True),
    Column(
        "tipo_de_servicio_id",
        Integer,
        ForeignKey("tipo_de_servicios.id"),
    ),
)
