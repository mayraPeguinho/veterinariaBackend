from sqlalchemy.ext.asyncio import AsyncSession
from security.auth import generarContraseñaHash
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate, UsuarioClienteCreate, UsuarioOut
from services.exceptions.auth import *
from services.exceptions.usuarios import *
from repositories.usuario import UsuariorRepo
import general_repo.operacionesOrm as general_repo
import services.persona as service_persona
import services.responsable as service_responsable
import services.empleados as service_empleado
from utils.enums import RolEnum
from typing import Optional


async def registrarUsuario(
    db: AsyncSession,
    usuario: UsuarioCreate | UsuarioClienteCreate,
    current_user: Optional[Usuario] = None,
):

    await validarNombreUsuarioUnico(db, usuario.nombre_de_usuario)
    await validarDniUnico(db, usuario.persona.dni)

    nombre_de_usuario_creacion = usuario.nombre_de_usuario
    if current_user:
        validarPermisoCrearUsuarioAdmin(usuario, current_user)
        nombre_de_usuario_creacion = current_user.nombre_de_usuario

    persona_model = await service_persona.obtenerPersona(
        db, usuario.persona, usuario.nombre_de_usuario
    )
    await db.flush()
    if persona_model.id is None:
        raise Exception()

    rol = getattr(usuario, "rol_id", None)
    rol_id = rol.value if rol else RolEnum.CLIENTE.value
    nuevoUsuario = Usuario(
        nombre_de_usuario=usuario.nombre_de_usuario,
        contrasenia=generarContraseñaHash(usuario.contrasenia),
        persona=persona_model,
        rol_id=rol_id,
        usuario_creacion=nombre_de_usuario_creacion,
    )

    await general_repo.OperacionesOrm(db).add_and_refresh(nuevoUsuario)

    if rol_id == RolEnum.ADMIN.value or rol_id == RolEnum.EMPLEADO.value:
        empleado_model = await service_empleado.crear(
            db, usuario.persona.empleado, persona_model.id, nombre_de_usuario_creacion
        )
        persona_model.empleado = empleado_model

    elif rol_id == RolEnum.CLIENTE.value:
        responsable_model = await service_responsable.crear(
            db,
            usuario.persona.responsable,
            persona_model.id,
            nombre_de_usuario_creacion,
        )
        persona_model.responsable = responsable_model
    await db.refresh(persona_model, ["responsable", "empleado"])
    await db.refresh(nuevoUsuario, ["persona"])
    # return UsuarioOut.model_validate(nuevoUsuario, from_attributes=True)
    return nuevoUsuario


async def obtenerPorNombreUsuario(db, username: str):
    return await UsuariorRepo(db).buscarPorNombreUsuario(username)


async def obtenerPorId(db, id_usuario: int):
    return await UsuariorRepo(db).buscarPorId(id_usuario)


async def obtenerTodos(db):
    return await UsuariorRepo(db).obtenerTodos()


async def validarNombreUsuarioUnico(db: AsyncSession, nombre_usuario: str):
    if await obtenerPorNombreUsuario(db, nombre_usuario):
        raise NombreUsuarioUsadoException()


async def validarDniUnico(db: AsyncSession, dni: str):
    if await UsuariorRepo(db).buscarPorDni(dni):
        raise NumeroDocumentoAsignadoException()


def validarPermisoCrearUsuarioAdmin(usuario: UsuarioCreate, current_user: Usuario):
    if (
        usuario.rol_id == RolEnum.ADMIN.value
        and current_user.rol_id != RolEnum.ADMIN.value
    ):
        raise PermisosInsuficientesException()
