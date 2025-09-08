from sqlalchemy.ext.asyncio import AsyncSession
from models.persona import Persona as ModelPersona

from typing import TypedDict, Optional
from sqlalchemy import select
from sqlalchemy.orm import selectinload


class Persona:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def buscarDni(self, dni: str) -> Optional[ModelPersona]:
        query = (
            select(ModelPersona)
            .options(selectinload(ModelPersona.usuario))
            .where((ModelPersona.dni == dni))
        )
        result = await self.db.execute(query)
        return result.scalars().first()
