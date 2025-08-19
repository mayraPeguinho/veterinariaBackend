from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Table


empleado_categoria = Table(
    "empleados_categorias",
    Base.metadata,
    Column("empleado_id", Integer, ForeignKey("empleados.id")),
    Column("categoria_id", Integer, ForeignKey("categorias.id")),
)
