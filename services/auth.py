from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from security.auth import generar_contraseña_hash

from models.usuario import Usuario as ModelUsuario
from models.persona import Persona as ModelPersona

from schemas.usuario import UsuarioCreate, UsuarioOut
from exceptions.auth import (
    NombreUsuarioUsadoException,
    PersonaExistenteComoUsuarioException,
    RolInvalidoException,
)

import repositories.Persona as persona_repo
import repositories.Usuario as usuario_repo
import general_repo.operacionesOrm as general_repo


async def registrarUsuario(usuario: UsuarioCreate, db: AsyncSession) -> UsuarioOut:

    usuarioExistente = await usuario_repo.Usuario(db).buscarPorUsuario(
        usuario.nombre_de_usuario
    )
    if usuarioExistente:
        raise NombreUsuarioUsadoException()
    # Obtener o crear persona y devolver su id (desacoplado en método privado)
    persona_id = await _obtener_o_crear_persona(usuario.persona, db)

    # Crear usuario (existente o recien creada)
    nuevo_usuario = ModelUsuario(
        nombre_de_usuario=usuario.nombre_de_usuario,
        contrasenia=generar_contraseña_hash(usuario.contrasenia),
        persona_id=persona_id,
        rol_id=usuario.rol,
        fecha_creacion=datetime.now(),
    )
    await general_repo.OperacionesOrm(db).add_and_refresh(nuevo_usuario)
    return nuevo_usuario


async def _obtener_o_crear_persona(persona_schema, db: AsyncSession):
    """Busca una persona por dni/email; si existe y no tiene usuario la actualiza,
    si no existe la crea. Devuelve el id de la persona.

    Lanza auth_exceptions.PersonaExistente si la persona ya tiene usuario.
    """
    existePersona = await persona_repo.Persona(db).buscarDni(persona_schema.dni)

    # Si existe persona y ya tiene usuario
    if existePersona and existePersona.usuario:
        raise PersonaExistenteComoUsuarioException()

    if existePersona:
        return existePersona.id
    else:
        persona_payload = persona_schema.model_dump(exclude_none=True)

        # No existe persona: crear nueva
        nueva_persona = ModelPersona(**persona_payload)
        await general_repo.OperacionesOrm(db).add_and_refresh(nueva_persona)
        return nueva_persona.id
