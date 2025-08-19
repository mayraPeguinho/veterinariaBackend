from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

atencion_producto = Table(
    "atenciones_productos",
    Base.metadata,
    Column("atencion_id", Integer, ForeignKey("atenciones.id"), primary_key=True),
    Column("producto_id", Integer, ForeignKey("productos.id"), primary_key=True),
)
