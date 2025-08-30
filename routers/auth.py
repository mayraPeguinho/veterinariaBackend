from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from config.database import get_db
from datetime import datetime

from models import usuario as model_usuario
from schemas import usuario as schema_usuario

from security.auth import (
    generar_contraseña_hash,
    verificar_contraseña,
    crear_token_acceso,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/", status_code=201, response_model=schema_usuario.UsuarioCreacion)
async def crear_usuario(
    usuario: schema_usuario.UsuarioCreacion, db: AsyncSession = Depends(get_db)
):
    # Verificar si el usuario ya existe
    result = await db.execute(
        select(model_usuario.Usuario).where(
            model_usuario.Usuario.nombre_de_usuario == usuario.nombre_de_usuario
        )
    )
    db_usuario = result.scalars().first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="Nombre de usuario ya registrado")

    # Crear usuario nuevo
    nuevo_usuario = model_usuario.Usuario(
        nombre_de_usuario=usuario.nombre_de_usuario,
        contrasenia=generar_contraseña_hash(usuario.contrasenia),
        fecha_creacion=datetime.now(),
    )

    db.add(nuevo_usuario)
    await db.refresh(nuevo_usuario)
    return nuevo_usuario


# @router.post("/iniciar_sesion")
# async def iniciar_sesion(usuario: UsuarioLogin, db: AsyncSession = Depends(get_db)):
#     # Buscar usuario en DB
#     result = await db.execute(
#         select(Usuario).where(Usuario.nombre_de_usuario == usuario.nombre_de_usuario)
#     )
#     db_usuario = result.scalars().first()

#     if not db_usuario or not verificar_contraseña(
#         usuario.contrasenia, db_usuario.contrasenia
#     ):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Credenciales inválidas",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     # Crear token JWT
#     token = crear_token_acceso({"sub": db_usuario.nombre_de_usuario})

#     return {"access_token": token, "token_type": "bearer"}
