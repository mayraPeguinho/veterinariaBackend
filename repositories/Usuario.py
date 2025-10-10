from models.usuario import Usuario
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class UsuariorRepo:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def buscarPorUsuario(self, nombre_de_usuario: str) -> Usuario | None:
        query = select(Usuario).where((Usuario.nombre_de_usuario == nombre_de_usuario))
        result = await self.db.execute(query)
        return result.scalars().first()
