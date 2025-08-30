from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

rol_permiso = Table(
    "Roles_Permisos",
    Base.metadata,
    Column("rol_id", Integer, ForeignKey("Roles.id"), primary_key=True),
    Column("permiso_id", Integer, ForeignKey("Permisos.id"), primary_key=True),
)
