from sqlalchemy.ext.asyncio import AsyncSession
from models.empleado import Empleado
import general_repo.operacionesOrm as general_repo
from repositories.empleado import EmpleadoRepo
from services.exceptions.empleados import *


async def crear(db: AsyncSession, empleado, id_persona: int, usuario_creacion: str):
    await validarNumeroLegajoUnico(db, empleado.numero_legajo)
    empleado_model = Empleado(
        **empleado.model_dump(),
        persona_id=id_persona,
        usuario_creacion=usuario_creacion
    )

    await general_repo.OperacionesOrm(db).add_and_refresh(empleado_model)


async def obtenerPorNumeroDeLegajo(db: AsyncSession, numero_legajo: str):
    return await EmpleadoRepo(db).buscarPorNumeroDeLegajo(numero_legajo)


async def validarNumeroLegajoUnico(db: AsyncSession, numero_legajo: str):
    if await obtenerPorNumeroDeLegajo(db, numero_legajo):
        raise NumeroDeLegajoAsignadoException()
