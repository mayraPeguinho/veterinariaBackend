from sqlalchemy.ext.asyncio import AsyncSession
from models.persona import Persona
import general_repo.operacionesOrm as general_repo
from repositories.persona import PersonaRepo


async def obtenerIdPersona(db: AsyncSession, persona_schema, usuario_creacion: str):
    existePersona = await PersonaRepo(db).buscarPorDni(persona_schema.dni)

    if existePersona:
        return existePersona.id
    else:
        persona_payload = persona_schema.model_dump(exclude_none=True)
        persona_payload["usuario_creacion"] = usuario_creacion

        nueva_persona = Persona(**persona_payload)
        await general_repo.OperacionesOrm(db).add_and_refresh(nueva_persona)
        return nueva_persona.id
