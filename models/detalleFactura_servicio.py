from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

detalleFactura_servicio = Table(
    "DetalleFacturas_Servicios",
    Base.metadata,
    Column("detalle_factura_id", Integer, ForeignKey("DetalleFacturas.id"), primary_key=True),
    Column("servicio_id", Integer, ForeignKey("Servicios.id"), primary_key=True),
)
