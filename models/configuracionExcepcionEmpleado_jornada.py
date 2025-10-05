from config.database import Base
from sqlalchemy import Column, Integer, Table, String, Numeric, ForeignKey, Time


configuracionExcepcionEmpleado_jornada = Table(
    "ConfiguracionesExcepcionesEmpleados_Jornadas",
    Base.metadata,
    Column("jornada_id", Integer, ForeignKey("Jornadas.id")),
    Column(
        "configuracion_excecpion_empleado_id",
        Integer,
        ForeignKey("ConfiguracionesExcepcionesEmpleados.id"),
    ),
)
