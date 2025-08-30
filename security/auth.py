import bcrypt
from jose import jwt
from jose.exceptions import JWTError
from datetime import datetime, timedelta, timezone
from typing import Optional
from dotenv import load_dotenv


SECRET_KEY = "p9$Xw!4zQ@bL2#vR6fT8^44441&yU4eG5hK3*]P"
ALGORITHM = "HS256"


def crear_token_acceso(datos: dict, expiracion: Optional[timedelta] = None):
    if expiracion is None:
        expiracion = timedelta(minutes=15)

    datos_a_codificar = datos.copy()
    datos_a_codificar.update(
        {"exp": datetime.now(timezone.utc) + expiracion}
    )  # si existe lo modifica sino lo crea el exp
    token_jwt = jwt.encode(datos_a_codificar, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt


def decodifica_token_acceso(token: str):
    try:
        datos = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return datos
    except JWTError:
        return None


def generar_contraseña_hash(contraseña: str) -> str:
    hashed = bcrypt.hashpw(contraseña.encode("utf8"), bcrypt.gensalt())
    return hashed.decode("utf8")


def verificar_contraseña(contraseña, contraseña_hash) -> bool:
    return bcrypt.checkpw(contraseña.encode("utf8"), contraseña_hash.encode("utf8"))
