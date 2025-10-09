from sqlalchemy.ext.asyncio import AsyncSession
from models.rol import Rol
from sqlalchemy import select


class RolRepo:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def buscarPorId(self, id: int):
        query = select(Rol).where((Rol.id == id))
        result = await self.db.execute(query)
        return result.scalars().first()
