from sqlalchemy.ext.asyncio import AsyncSession
from models.responsable import Responsable
import general_repo.operacionesOrm as general_repo


async def crear(db: AsyncSession, responsable, persona_id, usuario_creacion: str):

    responsable_model = Responsable(
        acepta_recordatorios=responsable.acepta_recordatorios,
        persona_id=persona_id,
        usuario_creacion=usuario_creacion,
    )
    await general_repo.OperacionesOrm(db).add_and_refresh(responsable_model)
