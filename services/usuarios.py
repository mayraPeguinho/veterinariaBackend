from sqlalchemy.ext.asyncio import AsyncSession
from security.auth import generarContraseñaHash, verificarContraseña
from models.usuario import Usuario
from schemas.usuario import (
    UsuarioInternoCreate,
    UsuarioExternoCreate,
    UsuarioActualEdit,
)
from services.exceptions.auth import *
from services.exceptions.usuarios import *
from repositories.usuario import UsuariorRepo
import general_repo.operacionesOrm as general_repo
import services.persona as service_persona
import services.responsable as service_responsable
import services.empleados as service_empleado
from utils.enums import RolEnum


async def registrarUsuarioExterno(
    db: AsyncSession,
    usuario: UsuarioExternoCreate,
):
    await _validarDatosBasicos(db, usuario)

    persona_model = await service_persona.obtenerPersona(
        db, usuario.persona, usuario.nombre_de_usuario
    )
    await db.refresh(persona_model, ["responsable"])

    nuevoUsuario = await _crearUsuarioBase(
        db=db,
        usuario=usuario,
        persona_model=persona_model,
        rol_id=RolEnum.CLIENTE.value,
        usuario_creacion=usuario.nombre_de_usuario,
    )

    if persona_model.responsable is None:
        responsable_model = await service_responsable.crear(
            db,
            usuario.persona.responsable,
            persona_model.id,
            usuario.nombre_de_usuario,
        )
        persona_model.responsable = responsable_model
        await db.refresh(persona_model, ["responsable"])
        await db.refresh(nuevoUsuario, ["persona"])
    return nuevoUsuario


async def registrarUsuarioInterno(
    db: AsyncSession,
    usuario: UsuarioInternoCreate,
    current_user: Usuario = None,
):
    if usuario.rol_id.value == RolEnum.CLIENTE.value:
        raise RolInvalidoException()
    await _validarDatosBasicos(db, usuario)

    validarPermisoCrearUsuarioAdmin(usuario, current_user)

    persona_model = await service_persona.obtenerPersona(
        db, usuario.persona, usuario.nombre_de_usuario
    )

    nuevoUsuario = await _crearUsuarioBase(
        db=db,
        usuario=usuario,
        persona_model=persona_model,
        rol_id=usuario.rol_id.value,
        usuario_creacion=current_user.nombre_de_usuario,
    )
    await db.refresh(persona_model, ["empleado"])

    if persona_model.empleado is None:

        empleado_model = await service_empleado.crear(
            db,
            usuario.persona.empleado,
            persona_model.id,
            current_user.nombre_de_usuario,
        )
        persona_model.empleado = empleado_model
        await db.refresh(persona_model, ["empleado"])
        await db.refresh(nuevoUsuario, ["persona"])

    return nuevoUsuario


async def _validarDatosBasicos(db: AsyncSession, usuario):
    await validarNombreUsuarioUnico(db, usuario.nombre_de_usuario)
    await validarDniUnico(db, usuario.persona.dni)
    await validarEmailUnico(db, usuario.email)


async def _crearUsuarioBase(
    db: AsyncSession,
    usuario,
    persona_model,
    rol_id: int,
    usuario_creacion: str,
) -> Usuario:
    nuevo_usuario = Usuario(
        nombre_de_usuario=usuario.nombre_de_usuario,
        email=usuario.email,
        contrasenia=generarContraseñaHash(usuario.contrasenia),
        persona=persona_model,
        rol_id=rol_id,
        usuario_creacion=usuario_creacion,
    )
    await general_repo.OperacionesOrm(db).add_and_refresh(nuevo_usuario)
    return nuevo_usuario


async def obtenerPorNombreUsuario(db, username: str):
    usuario = await UsuariorRepo(db).obtenerPorNombreUsuario(username)
    if usuario:
        return usuario
    raise UsuarioNoEncontradoException()


async def obtenerPorId(db, id_usuario: int):
    usuario = await UsuariorRepo(db).obtenerPorId(id_usuario)
    if usuario:
        return usuario
    raise UsuarioNoEncontradoException()


async def obtenerTodos(db):
    return await UsuariorRepo(db).obtenerTodos()


async def validarNombreUsuarioUnico(db: AsyncSession, nombre_usuario: str):
    if await UsuariorRepo(db).obtenerPorNombreUsuario(nombre_usuario):
        raise NombreUsuarioUsadoException()


async def validarDniUnico(db: AsyncSession, dni: str):
    if await UsuariorRepo(db).obtenerPorDni(dni):
        raise NumeroDocumentoAsignadoException()


async def validarEmailUnico(db: AsyncSession, email: str):
    if await UsuariorRepo(db).obtenerPorEmail(email):
        raise EmailUsadoException()


def validarPermisoCrearUsuarioAdmin(
    usuario: UsuarioInternoCreate, current_user: Usuario
):
    if (
        usuario.rol_id == RolEnum.ADMIN.value
        and current_user.rol_id != RolEnum.ADMIN.value
    ):
        raise PermisosInsuficientesException()


async def modificarUsuarioActual(
    db, usuario: UsuarioActualEdit, current_user: Usuario
) -> Usuario:
    requiere_autenticacion = (
        usuario.nombre_de_usuario != current_user.nombre_de_usuario
        or usuario.email != current_user.email
        or usuario.contrasenia_nueva
    )

    if requiere_autenticacion:
        await _actualizarDatosSensibles(db, usuario, current_user)

    _actualizarDatosPersonales(usuario, current_user)

    return current_user


async def _actualizarDatosSensibles(
    db, usuario: UsuarioActualEdit, current_user: Usuario
) -> None:
    if not usuario.contrasenia_actual or not verificarContraseña(
        usuario.contrasenia_actual, current_user.contrasenia
    ):
        raise CredencialesInvalidasException()

    if usuario.nombre_de_usuario != current_user.nombre_de_usuario:
        await validarNombreUsuarioUnico(db, usuario.nombre_de_usuario)
        current_user.nombre_de_usuario = usuario.nombre_de_usuario

    if usuario.email != current_user.email:
        await validarEmailUnico(db, usuario.email)
        current_user.email = usuario.email

    if usuario.contrasenia_nueva:
        current_user.contrasenia = generarContraseñaHash(usuario.contrasenia_nueva)


def _actualizarDatosPersonales(
    usuario: UsuarioActualEdit, current_user: Usuario
) -> None:
    persona_nueva = usuario.persona
    persona_actual = current_user.persona

    persona_actual.nombre = persona_nueva.nombre
    persona_actual.apellido = persona_nueva.apellido
    persona_actual.telefono = persona_nueva.telefono
    persona_actual.genero = persona_nueva.genero.value
    persona_actual.direccion = persona_nueva.direccion
    persona_actual.email = persona_nueva.email

    if persona_nueva.responsable and persona_actual.responsable:
        persona_actual.responsable.acepta_recordatorios = (
            persona_nueva.responsable.acepta_recordatorios
        )
