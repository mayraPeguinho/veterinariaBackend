import typer
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import AsyncSessionLocal
from sqlalchemy.future import select
from models.rol import Rol
from models.estadoTurno import EstadoTurno


app = typer.Typer()


async def creacion_roles(db: AsyncSession):
    result = await db.execute(select(Rol))
    roles_existentes = result.scalars().all()

    if not roles_existentes:
        db.add_all(
            [
                Rol(nombre="admin"),
                Rol(nombre="empleado"),
                Rol(nombre="cliente"),
            ]
        )
        await db.commit()


async def creacion_estados(db: AsyncSession):
    result = await db.execute(select(EstadoTurno))
    estados_existentes = result.scalars().all()

    if not estados_existentes:
        db.add_all(
            [
                EstadoTurno(nombre="Creado"),
                EstadoTurno(nombre="Agendado"),
                EstadoTurno(nombre="Incompleto"),
                EstadoTurno(nombre="Completado"),
                EstadoTurno(nombre="Cancelado"),
                EstadoTurno(nombre="Expirado"),
            ]
        )
        await db.commit()


async def crear_tablas_iniciales(db: AsyncSession):
    await creacion_roles(db)
    await creacion_estados(db)


if __name__ == "__main__":
    app()
