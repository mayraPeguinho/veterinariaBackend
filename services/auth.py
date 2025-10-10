from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from security.auth import generarContraseñaHash, verificarContraseña
from security.token import crearTokenAcceso
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate, UsuarioOut
from exceptions.auth import *
from repositories.usuario import UsuariorRepo as usuario_repo
import general_repo.operacionesOrm as general_repo
import services.persona as service_persona
from utils.enums import RolEnum


async def registrarUsuario(
    db: AsyncSession,
    usuario: UsuarioCreate,
) -> UsuarioOut:

    model_usuario = await obtenerUsuarioPorNombreDeUsuario(
        db, usuario.nombre_de_usuario
    )
    if model_usuario is not None:
        raise NombreUsuarioUsadoException()
    personaId = await service_persona.obtenerIdPersona(
        db, usuario.persona, usuario.nombre_de_usuario
    )

    nuevoUsuario = Usuario(
        nombre_de_usuario=usuario.nombre_de_usuario,
        contrasenia=generarContraseñaHash(usuario.contrasenia),
        persona_id=personaId,
        rol_id=RolEnum.CLIENTE.value,
        fecha_creacion=datetime.now(),
        usuario_creacion=usuario.nombre_de_usuario,
    )

    await general_repo.OperacionesOrm(db).add_and_refresh(nuevoUsuario)

    return nuevoUsuario


async def login(db: AsyncSession, username, password):

    usuario_existente = await obtenerUsuarioPorNombreDeUsuario(db, username)
    if verificarContraseña(password, usuario_existente.contrasenia):
        return crearTokenAcceso({"sub": username})
    else:
        raise CredencialesInvalidasException()


async def obtenerUsuarioPorNombreDeUsuario(db, username: str):
    return await usuario_repo(db).buscarPorUsuario(username)
