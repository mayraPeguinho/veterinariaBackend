from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from security.auth import generar_contraseña_hash
from utils.enums import GeneroEnum

from models.usuario import Usuario as ModelUsuario
from models.persona import Persona as ModelPersona

from schemas.usuario import UsuarioCreate, UsuarioOut
from exceptions.auth import (
    NombreUsuarioUsadoException,
    PersonaExistenteComoUsuarioException,
    RolInvalidoException,
)
from exceptions.generalRepo import ErrorBaseDatos

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
    personaId = await _ObtenerPersona(usuario.persona, db)

    # Crear usuario (existente o recien creada)
    nuevoUsuario = ModelUsuario(
        nombre_de_usuario=usuario.nombre_de_usuario,
        contrasenia=generar_contraseña_hash(usuario.contrasenia),
        persona_id=personaId,
        rol_id=usuario.rol,
        fecha_creacion=datetime.now(),
    )

    await general_repo.OperacionesOrm(db).add_and_refresh(nuevoUsuario)

    return nuevoUsuario


async def _ObtenerPersona(persona_schema, db: AsyncSession):
    existePersona = await persona_repo.Persona(db).buscarDni(persona_schema.dni)

    # if existePersona and existePersona.usuario:
    #     raise PersonaExistenteComoUsuarioException()

    if existePersona:
        return existePersona.id
    else:
        persona_payload = persona_schema.model_dump(exclude_none=True)

        # No existe persona: crear nueva
        nueva_persona = ModelPersona(**persona_payload)
        await general_repo.OperacionesOrm(db).add_and_refresh(nueva_persona)
        return nueva_persona.id
