from config.database import Base
from sqlalchemy import Column, Integer, Table, String, Numeric, ForeignKey, Time
from sqlalchemy.orm import relationship


configuracionDiariaEmpleado_jornada = Table(
    "configuraciones_diarias_empleados_jornadas",
    Base.metadata,
    Column("jornada_id", Integer, ForeignKey("jornada.id")),
    Column(
        "configuracion_diaria_empleado_id",
        Integer,
        ForeignKey("configuracion_diaria_empleado.id"),
    ),
)
