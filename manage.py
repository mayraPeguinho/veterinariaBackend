import typer
from config.database import Base, engine, SessionLocal
from .seed.data_inicial import (
    crear_tablas_iniciales,
)
import pkgutil
import importlib
import models
from sqlalchemy import text


# Importar automáticamente todos los módulos dentro de models
for _, module_name, _ in pkgutil.iter_modules(models.__path__):
    importlib.import_module(f"models.{module_name}")

app = typer.Typer()


@app.command()
def init_db():
    """Crear tablas"""
    typer.echo("Actuu")
    try:
        Base.metadata.create_all(bind=engine)
        typer.echo("✅ Tablas creadas")
    except Exception as e:
        typer.echo(f"❌ Error al crear tablas: {e}")


@app.command()
def drop_db():
    """Eliminar todas las tablas y objetos en cascada"""
    try:
        with engine.connect() as conn:
            # Borra todo el schema public con CASCADE
            conn.execute(text("DROP SCHEMA public CASCADE"))
            # Lo vuelve a crear vacío
            conn.execute(text("CREATE SCHEMA public"))
        typer.echo("🗑️ Base de datos reseteada (DROP SCHEMA CASCADE)")
    except Exception as e:
        typer.echo(f"❌ Error al eliminar tablas: {e}")


@app.command()
def seed():
    """Inserta datos iniciales (idempotente)."""
    db = SessionLocal()
    try:
        crear_tablas_iniciales(db)
        db.commit()
        typer.echo("✅ Seeds aplicadas correctamente.")
    except Exception as e:
        db.rollback()
        typer.echo(f"❌ Error aplicando seeds: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    app()
