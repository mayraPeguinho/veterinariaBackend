from config.database import Base
from sqlalchemy import Column, Integer, Table, String, Numeric, ForeignKey, Time


configuracionDiariaEmpleado_jornada = Table(
    "ConfiguracionesDiariasEmpleados_Jornadas",
    Base.metadata,
    Column("jornada_id", Integer, ForeignKey("Jornadas.id")),
    Column(
        "configuracion_diaria_empleado_id",
        Integer,
        ForeignKey("ConfiguracionesDiariasEmpleados.id"),
    ),
)
