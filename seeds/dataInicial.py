import typer
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import AsyncSessionLocal
from sqlalchemy.future import select
from models.rol import Rol
from models.tipoEstadoTurno import TipoEstadoTurno


app = typer.Typer()


async def creacion_roles(db: AsyncSession):
    result = await db.execute(select(Rol))
    roles_existentes = result.scalars().all()

    if not roles_existentes:
        db.add_all(
            [
                Rol(nombre="Admin"),
                Rol(nombre="Empleado"),
                Rol(nombre="Cliente"),
            ]
        )
        await db.commit()


async def creacion_estados(db: AsyncSession):
    result = await db.execute(select(TipoEstadoTurno))
    estados_existentes = result.scalars().all()

    if not estados_existentes:
        db.add_all(
            [
                TipoEstadoTurno(nombre="Creado"),
                TipoEstadoTurno(nombre="Agendado"),
                TipoEstadoTurno(nombre="Incompleto"),
                TipoEstadoTurno(nombre="Completado"),
                TipoEstadoTurno(nombre="Cancelado"),
                TipoEstadoTurno(nombre="Expirado"),
            ]
        )
        await db.commit()


async def crear_tablas_iniciales(db: AsyncSession):
    await creacion_roles(db)
    await creacion_estados(db)


if __name__ == "__main__":
    app()
