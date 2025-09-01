from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime
from security.auth import generar_contraseña_hash

from models.usuario import Usuario as ModelUsuario
from models.persona import Persona as ModelPersona
from models.rol import Rol as ModelRol
from schemas.usuario import UsuarioCreate, UsuarioOut


async def usuario_creado(usuario: UsuarioCreate, db: AsyncSession) -> UsuarioOut:

    usuarioExistente = select(ModelUsuario).where(
        ModelUsuario.nombre_de_usuario == usuario.nombre_de_usuario
    )
    respuestaUsuarioExistente = await db.execute(usuarioExistente)
    if respuestaUsuarioExistente.scalars().first():
        raise HTTPException(
            status_code=409, detail="El nombre de usuario ya está en uso."
        )

    # Validación DNI/email en Persona
    existePersona = select(ModelPersona).where(
        (ModelPersona.dni == usuario.persona.dni)
        | (ModelPersona.email == usuario.persona.email)
    )
    respuestaExistePersona = await db.execute(existePersona)
    if respuestaExistePersona.scalars().first():
        raise HTTPException(status_code=409, detail="DNI o email ya existen.")

    # Resolver rol
    userRol = select(ModelRol).where(
        ModelRol.nombre == usuario.rol
    )  # adapta según tu schema
    respuestauserRol = await db.execute(userRol)
    rol = respuestauserRol.scalars().first()
    if not rol:
        raise HTTPException(status_code=400, detail="Rol inválido.")

    # Crear persona y flush para obtener id
    nueva_persona = ModelPersona(**usuario.persona.model_dump(exclude_none=True))
    db.add(nueva_persona)
    await db.flush()  # nueva_persona.id estará disponible pero no committed

    # Crear usuario
    nuevo_usuario = ModelUsuario(
        nombre_de_usuario=usuario.nombre_de_usuario,
        contrasenia=generar_contraseña_hash(usuario.contrasenia),
        persona_id=nueva_persona.id,
        rol_id=rol.id,
        fecha_creacion=datetime.now(),
    )
    db.add(nuevo_usuario)

    await db.refresh(nuevo_usuario)
    return nuevo_usuario
