from sqlalchemy.ext.asyncio import AsyncSession
from security.auth import verificarContraseña
from security.token import crearTokens, decodificarRefreshToken
from services.exceptions.auth import *
import services.usuarios as service_usuarios


async def login(db: AsyncSession, username, password):

    usuario_existente = await service_usuarios.obtenerPorNombreUsuario(db, username)
    if verificarContraseña(password, usuario_existente.contrasenia):
        return crearTokens(
            {
                "sub": f"{usuario_existente.id}",
                "usuario": username,
                "rol": usuario_existente.rol.nombre,
                "permisos": [p.nombre for p in usuario_existente.rol.permisos],
            }
        )
    else:
        raise CredencialesInvalidasException()


async def refrescarToken(db: AsyncSession, refresh_token):

    payload = decodificarRefreshToken(refresh_token)
    usuario_id = int(payload.get("sub"))

    usuario = await service_usuarios.obtenerPorId(db, usuario_id)

    if not usuario:
        raise CredencialesInvalidasException()

    tokens = crearTokens(
        {
            "sub": str(usuario.id),
            "usuario": usuario.nombre_de_usuario,
            "rol": usuario.rol.nombre,
            "permisos": [p.nombre for p in usuario.rol.permisos],
        }
    )

    return tokens
