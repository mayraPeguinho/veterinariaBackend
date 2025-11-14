from sqlalchemy.ext.asyncio import AsyncSession
from models.empleado import Empleado
from typing import Optional
from sqlalchemy import select


class EmpleadoRepo:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def buscarPorNumeroDeLegajo(self, numero_legajo: str) -> Optional[Empleado]:
        query = select(Empleado).where((Empleado.numero_legajo == numero_legajo))
        result = await self.db.execute(query)
        return result.scalars().first()
