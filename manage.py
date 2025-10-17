import typer
import asyncio
import pkgutil
import importlib
from sqlalchemy import text
from config.database import Base, engine, AsyncSessionLocal
from seeds.dataInicial import crear_tablas_iniciales
import models

# Importar automáticamente todos los modelos
for _, module_name, _ in pkgutil.iter_modules(models.__path__):
    importlib.import_module(f"models.{module_name}")

app = typer.Typer()


# ----------------------
# Funciones async internas
# ----------------------
async def _init_db():
    """Crear todas las tablas."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def _drop_db():
    """Eliminar todas las tablas y recrear el schema."""
    async with engine.begin() as conn:
        await conn.run_sync(
            lambda sync_conn: sync_conn.execute(text("DROP SCHEMA public CASCADE"))
        )
        await conn.run_sync(
            lambda sync_conn: sync_conn.execute(text("CREATE SCHEMA public"))
        )


async def _seed_db():
    """Aplicar seeds iniciales (idempotente)."""
    async with AsyncSessionLocal() as db:
        await crear_tablas_iniciales(db)


# ----------------------
# Comandos Typer
# ----------------------
@app.command()
def init_db():
    """Crear tablas de la base de datos."""
    typer.echo("🔄 Creando tablas...")
    try:
        asyncio.run(_init_db())
        typer.echo("✅ Tablas creadas correctamente.")
    except Exception as e:
        typer.echo(f"❌ Error creando tablas: {e}")


@app.command()
def reset_db():
    """Reiniciar la base de datos y aplicar seeds."""
    typer.echo("♻️ Reseteando base de datos...")

    async def _reset():
        await _drop_db()
        await _init_db()
        await _seed_db()

    try:
        asyncio.run(_reset())
        typer.echo("✅ Base de datos reiniciada y seeds aplicadas.")
    except Exception as e:
        typer.echo(f"❌ Error reseteando base de datos: {e}")


@app.command()
def seed():
    """Aplicar seeds a la base de datos."""
    typer.echo("🌱 Aplicando seeds...")
    try:
        asyncio.run(_seed_db())
        typer.echo("✅ Seeds aplicadas correctamente.")
    except Exception as e:
        typer.echo(f"❌ Error aplicando seeds: {e}")


# ----------------------
if __name__ == "__main__":
    app()
