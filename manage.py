import typer
from config.database import Base, engine
import pkgutil
import importlib
import models  # tu carpeta de modelos

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
    """Eliminar tablas"""
    try:
        Base.metadata.drop_all(bind=engine)
        typer.echo("🗑️ Tablas eliminadas")
    except Exception as e:
        typer.echo(f"❌ Error al eliminar tablas: {e}")

if __name__ == "__main__":
    app()
