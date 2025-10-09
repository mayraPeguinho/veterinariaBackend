from exceptions.auth import *
from jose import jwt
from jose.exceptions import JWTError
from datetime import datetime, timedelta, timezone
from typing import Optional
import os

SECRET_KEY = os.getenv("SECRET_KEY_TOKEN")

ALGORITHM = "HS256"


def crearTokenAcceso(datos: dict, expiracion: Optional[timedelta] = None):
    if expiracion is None:
        expiracion = timedelta(minutes=15)

    datos_a_codificar = datos.copy()
    datos_a_codificar.update({"exp": datetime.now(timezone.utc) + expiracion})

    return {
        "access_token": jwt.encode(datos_a_codificar, SECRET_KEY, algorithm=ALGORITHM)
    }


def decodificarTokenAcceso(token: str):
    try:
        datos = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return datos
    except JWTError:
        raise CredencialesInvalidasException()
