from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from exceptions.handleExcep import appHandleException

# Importar models para registrar todos los modelos de SQLAlchemy
import models
from config.database import engine, Base

from routers import auth

app = FastAPI()
app.include_router(auth.router)
app.add_exception_handler(Exception, appHandleException)

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
