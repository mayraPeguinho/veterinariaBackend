from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise ValueError(
        "❌ Faltan variables de entorno para la conexión a la base de datos. Verifica tu archivo .env"
    )

engine = create_async_engine(DATABASE_URL, echo=False)


AsyncSessionLocal = async_sessionmaker(
    engine, expire_on_commit=False, autoflush=False, autocommit=False
)
Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as session:  # ← Auto-maneja sesión
        async with session.begin():  # ← Auto-maneja transacción
            yield session  # ← Entrega sesión con transacción activa
        # ← Auto-commit si todo sale bien, auto-rollback si hay error
    # ← Auto-close de sesión
