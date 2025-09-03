from sqlalchemy.ext.asyncio import AsyncSession
from models.rol import Rol as ModelRol
from sqlalchemy import select


class Rol:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def buscarPorId(self, id: int):
        query = select(ModelRol).where((ModelRol.id == id))
        result = await self.db.execute(query)
        return result.scalars().first()
