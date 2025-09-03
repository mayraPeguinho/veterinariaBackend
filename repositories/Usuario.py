from models.usuario import Usuario as ModelUsuario
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class Usuario:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def buscarPorUsuario(self, nombre_de_usuario: str):
        query = select(ModelUsuario).where(
            (ModelUsuario.nombre_de_usuario == nombre_de_usuario)
        )
        result = await self.db.execute(query)
        return result.scalars().first()
