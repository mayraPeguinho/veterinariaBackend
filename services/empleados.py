from sqlalchemy.ext.asyncio import AsyncSession
from models.empleado import Empleado
import general_repo.operacionesOrm as general_repo


async def crear(db: AsyncSession, empleado, id_persona: int, usuario_creacion: str):
    empleado_model = Empleado(
        **empleado.model_dump(),
        persona_id=id_persona,
        usuario_creacion=usuario_creacion
    )

    await general_repo.OperacionesOrm(db).add_and_refresh(empleado_model)
