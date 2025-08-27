from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

atencion_producto = Table(
    "Atenciones_Productos",
    Base.metadata,
    Column("atencion_id", Integer, ForeignKey("Atenciones.id"), primary_key=True),
    Column("producto_id", Integer, ForeignKey("Productos.id"), primary_key=True),
)
