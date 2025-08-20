from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# URL de conexión a PostgreSQL desde variable de entorno
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError(
        "❌ Variable de entorno DATABASE_URL no encontrada. Verifica tu archivo .env"
    )

# Motor de conexión
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()
