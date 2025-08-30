from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Table


empleado_categoria = Table(
    "Empleados_Categorias",
    Base.metadata,
    Column("empleado_id", Integer, ForeignKey("Empleados.id"), primary_key=True),
    Column("categoria_id", Integer, ForeignKey("Categorias.id"), primary_key=True),
)
