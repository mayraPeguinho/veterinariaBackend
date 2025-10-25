import bcrypt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, Path
from services.exceptions.auth import *
from security.token import decodificarTokenAcceso
from repositories.usuario import UsuariorRepo
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db
from models.usuario import Usuario
from repositories.rol import RolRepo
from utils.enums import RolEnum

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def generarContraseñaHash(contraseña: str) -> str:
    hashed = bcrypt.hashpw(contraseña.encode("utf8"), bcrypt.gensalt())
    return hashed.decode("utf8")


def verificarContraseña(contraseña, contraseña_hash) -> bool:
    return bcrypt.checkpw(contraseña.encode("utf8"), contraseña_hash.encode("utf8"))


async def getCurrentUser(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
) -> Usuario | None:
    payload = decodificarTokenAcceso(token)
    id_usuario = payload.get("sub")
    if id_usuario is None:
        raise CredencialesInvalidasException()
    return await UsuariorRepo(db).obtenerPorId(int(id_usuario))


def requierePermiso(nombre_permiso: str):
    async def verificar(
        usuario=Depends(getCurrentUser),
        db: AsyncSession = Depends(get_db),
    ):

        rol = await RolRepo(db).buscarPorId(usuario.rol_id)

        if not rol:
            raise PermisosInsuficientesException(
                detail="El usuario no tiene rol asignado"
            )

        permisos_del_rol = [p.nombre for p in rol.permisos]

        if nombre_permiso not in permisos_del_rol:
            raise PermisosInsuficientesException()

        return usuario

    return verificar


def puedeRealizarAccionUsuario(
    id: int = Path(...),
):
    async def verificar(current_user=Depends(getCurrentUser)):
        if current_user.rol_id == RolEnum.CLIENTE.value and current_user.id != id:
            print(current_user)
            print(id)
            raise PermisosInsuficientesException()
        return current_user

    return verificar
