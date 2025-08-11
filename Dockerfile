# Imagen base de Python
FROM python:3.11-slim

# Configuración básica de Python

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Zona horaria (opcional)
ENV TZ=America/Buenos_Aires

# Crear carpeta de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias (opcional para psycopg2-binary)
RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata && \
    rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias Python
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar el código
COPY . /app

# Exponer puerto del backend
EXPOSE 8000

# Ejecutar la app con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]