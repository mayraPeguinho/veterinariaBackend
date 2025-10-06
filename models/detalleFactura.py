from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class DetalleFactura(Base):
    __tablename__ = "DetallesFacturas"

    id = Column(Integer, primary_key=True)

    nombre_item = Column(String(50), nullable=False)
    descripcion_item = Column(String(50), nullable=False)  # ver
    # 1 en caso de venderse fraccionado o tratarse de un servicio
    cantidad = Column(Integer, nullable=False)
    factura_id = Column(Integer, ForeignKey("Facturas.id"), nullable=False)

    factura = relationship("Factura", back_populates="detalles_facturas")
