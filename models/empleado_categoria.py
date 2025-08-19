from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Time, Table


empleados_categorias = Table(
    "empleados_categorias",
    Base.metadata,
    Column("empleado_id", Integer, ForeignKey("empleados.id")),
    Column("categoria_id", Integer, ForeignKey("categorias.id")),
)
