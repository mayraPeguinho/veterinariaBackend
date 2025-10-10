import bcrypt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from exceptions.auth import *
from security.token import decodificarTokenAcceso
from repositories.usuario import UsuariorRepo
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def generarContraseñaHash(contraseña: str) -> str:
    hashed = bcrypt.hashpw(contraseña.encode("utf8"), bcrypt.gensalt())
    return hashed.decode("utf8")


def verificarContraseña(contraseña, contraseña_hash) -> bool:
    return bcrypt.checkpw(contraseña.encode("utf8"), contraseña_hash.encode("utf8"))


async def getCurrentUser(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
):
    payload = decodificarTokenAcceso(token)
    username = payload.get("sub")
    if username is None:
        raise CredencialesInvalidasException()
    await UsuariorRepo(db).buscarPorUsuario(username)
    return username
