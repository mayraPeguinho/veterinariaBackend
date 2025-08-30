from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

DATABASE_URL = (
    f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
)

if not all([USER, PASSWORD, HOST, PORT, DBNAME]):
    raise ValueError(
        "❌ Faltan variables de entorno para la conexión a la base de datos. Verifica tu archivo .env"
    )

engine = create_async_engine(DATABASE_URL, echo=False)


AsyncSessionLocal = async_sessionmaker(
    engine, expire_on_commit=False, autoflush=False, autocommit=False
)
Base = declarative_base()


# Async
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
