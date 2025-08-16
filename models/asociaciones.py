from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

roles_permisos = Table(
    "roles_permisos",
    Base.metadata,
    Column("rol_id", Integer, ForeignKey("roles.id"), primary_key=True),
    Column("permiso_id", Integer, ForeignKey("permisos.id"), primary_key=True),
)

atenciones_productos = Table(
    "atenciones_productos",
    Base.metadata,
    Column("atencion_id", Integer, ForeignKey("atenciones.id"), primary_key=True),
    Column("producto_id", Integer, ForeignKey("productos.id"), primary_key=True),
)
