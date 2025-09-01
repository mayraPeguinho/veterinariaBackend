import typer
from config.database import Base, engine, AsyncSessionLocal
from seeds.data_inicial import crear_tablas_iniciales
import pkgutil
import importlib
import models
from sqlalchemy import text
import asyncio


# Importar automáticamente todos los módulos dentro de models
for _, module_name, _ in pkgutil.iter_modules(models.__path__):
    importlib.import_module(f"models.{module_name}")

app = typer.Typer()


@app.command()
async def init_db():
    """Crear tablas"""
    typer.echo("Actualizando base de datos...")
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        typer.echo("✅ Tablas creadas")
    except Exception as e:
        typer.echo(f"❌ Error al crear tablas: {e}")


@app.command()
async def drop_db():
    """Eliminar todas las tablas y objetos en cascada"""
    try:
        async with engine.begin() as conn:
            await conn.execute(text("DROP SCHEMA public CASCADE"))
            await conn.execute(text("CREATE SCHEMA public"))
            typer.echo("🗑️ Base de datos reseteada (DROP SCHEMA CASCADE)")
    except Exception as e:
        typer.echo(f"❌ Error al eliminar tablas: {e}")


@app.command()
async def seed():
    """Inserta datos iniciales (idempotente)."""
    async with AsyncSessionLocal() as db:
        try:
            await crear_tablas_iniciales(db)
            await db.commit()
            typer.echo("✅ Seeds aplicadas correctamente.")
        except Exception as e:
            await db.rollback()
            typer.echo(f"❌ Error aplicando seeds: {e}")
            raise


@app.command()
def run_seed():
    asyncio.run(seed())


@app.command()
async def reset_db():
    """Reiniciar la base de datos."""
    await drop_db()
    await init_db()
    await seed()


@app.command()
def crear_tablas():  # Crea las tablas y permite ejecutar comandos async en consola
    typer.echo("Actualizando base de datos...")
    asyncio.run(init_db())


if __name__ == "__main__":

    asyncio.run(app())
