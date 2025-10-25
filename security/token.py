from services.exceptions.auth import *
from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError
from datetime import datetime, timedelta, timezone
from typing import Optional
import os

SECRET_KEY = os.getenv("SECRET_KEY_TOKEN")
REFRESH_SECRET_KEY = os.getenv("REFRESH_SECRET_KEY")

ALGORITHM = "HS256"


def crearTokens(datos: dict, expiracion: Optional[timedelta] = None):
    if expiracion is None:
        expiracion = timedelta(minutes=15)

    access_payload = datos.copy()
    access_payload.update(
        {
            "tipo": "access",
            "exp": datetime.now(timezone.utc) + expiracion,
            "iat": datetime.now(timezone.utc),
        }
    )
    access_token = jwt.encode(access_payload, SECRET_KEY, algorithm=ALGORITHM)

    refresh_payload = {
        "sub": datos["sub"],
        "tipo": "refresh",
        "exp": datetime.now(timezone.utc) + expiracion,
        "iat": datetime.now(timezone.utc),
    }
    refresh_token = jwt.encode(refresh_payload, REFRESH_SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


def decodificarTokenAcceso(token: str):
    try:
        datos = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return datos
    except ExpiredSignatureError:
        raise TokenExpiradoException()
    except JWTError:
        raise CredencialesInvalidasException()


def decodificarRefreshToken(token: str) -> dict:
    try:
        datos = jwt.decode(token, REFRESH_SECRET_KEY, algorithms=[ALGORITHM])

        if datos.get("tipo") != "refresh":
            raise CredencialesInvalidasException()

        return datos
    except ExpiredSignatureError:
        raise RefreshTokenExpiradoException()
    except JWTError:
        raise CredencialesInvalidasException()
