from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

roles_permisos = Table(
    "roles_permisos",
    Base.metadata,
    Column("rol_id", Integer, ForeignKey("roles.id"), primary_key=True),
    Column("permiso_id", Integer, ForeignKey("permisos.id"), primary_key=True)
)