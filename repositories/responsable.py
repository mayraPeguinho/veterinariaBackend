# from models.usuario import Usuario
# from models.permiso import Permiso
# from models.rol_permiso import rol_permiso
# from models.responsable import Responsable
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select
# from typing import List
# from repositories.persona import PersonaRepo


# class ResponsableRepo:
#     def __init__(self, db: AsyncSession) -> None:
#         self.db = db

#     async def buscarPorId(self, id_usuario: int) -> Usuario | None:
#         query = select(Usuario).where((Usuario.id == id_usuario))
#         result = await self.db.execute(query)
#         return result.scalars().first()
