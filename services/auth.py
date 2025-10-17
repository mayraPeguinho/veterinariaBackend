from sqlalchemy.ext.asyncio import AsyncSession
from security.auth import verificarContraseña
from security.token import crearTokenAcceso
from services.exceptions.auth import *
import services.usuarios as service_usuarios


async def login(db: AsyncSession, username, password):

    usuario_existente = await service_usuarios.obtenerPorNombreUsuario(db, username)
    if verificarContraseña(password, usuario_existente.contrasenia):
        return crearTokenAcceso({"sub": username})
    else:
        raise CredencialesInvalidasException()
