import typer
from config.database import Base, engine, SessionLocal
from seeds.data_inicial import crear_tablas_iniciales
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
        with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
            conn.execute(text("DROP SCHEMA public CASCADE"))
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


@app.command()
def reset_db():
    """Reiniciar la base de datos."""
    drop_db()
    init_db()
    seed()


if __name__ == "__main__":
    app()
