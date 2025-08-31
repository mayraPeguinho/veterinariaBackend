from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class TipoEstadoAtencion(Base):
    __tablename__ = "TiposEstadoAtencion"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)

    estados_atenciones = relationship(
        "EstadoAtencion", back_populates="tipo_estado_atencion"
    )
