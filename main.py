from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from exceptions.handlerExcep import register_exception_handlers

# Importar models para registrar todos los modelos de SQLAlchemy
from config.database import engine, Base

from routers import auth, usuarios

import pkgutil
import importlib
import models


# Importar automáticamente todos los módulos dentro de models
for _, module_name, _ in pkgutil.iter_modules(models.__path__):
    importlib.import_module(f"models.{module_name}")


app = FastAPI()
app.include_router(usuarios.router)
app.include_router(auth.router)
register_exception_handlers(app)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    # Crear las tablas en modo asincrónico
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
