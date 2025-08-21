from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey


servicio_producto = Table(
    "servicios_productos",
    Base.metadata,
    Column("servicio_id", Integer, ForeignKey("servicios.id"), primary_key=True),
    Column("producto_id", Integer, ForeignKey("productos.id"), primary_key=True),
)
