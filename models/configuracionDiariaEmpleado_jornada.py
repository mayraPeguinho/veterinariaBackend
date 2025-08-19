from config.database import Base
from sqlalchemy import Column, Integer, Table, String, Numeric, ForeignKey, Time


configuracionDiariaEmpleado_jornada = Table(
    "configuraciones_diarias_empleados_jornadas",
    Base.metadata,
    Column("jornada_id", Integer, ForeignKey("jornadas.id")),
    Column(
        "configuracion_diaria_empleado_id",
        Integer,
        ForeignKey("configuraciones_diarias_empleados.id"),
    ),
)
