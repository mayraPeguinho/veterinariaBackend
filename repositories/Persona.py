from sqlalchemy.ext.asyncio import AsyncSession
from models.persona import Persona
from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import selectinload


class PersonaRepo:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def buscarPorDni(self, dni: str) -> Optional[Persona]:
        query = (
            select(Persona)
            .options(
                selectinload(Persona.usuario),
                selectinload(Persona.responsable),
                selectinload(Persona.empleado),
            )
            .where((Persona.dni == dni))
        )
        result = await self.db.execute(query)
        return result.scalars().first()
