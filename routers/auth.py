from fastapi import APIRouter, Depends, HTTPException, status
from models.usuario import Usuario
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from config.database import get_db

from utils.auth import (
    generar_contraseña_hash,
    verificar_contraseña,
    crear_token_acceso,
    decodifica_token_acceso,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/", status_code=201)
async def crear_usuario(usuario: Usuario, db: AsyncSession = Depends(get_db)):
    # Verificamos si el nombre de usuario ya existe
    result = await db.execute(
        select(Usuario).where(Usuario.nombre_de_usuario == usuario.nombre_de_usuario)
    )
    db_usuario = result.scalars().first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="Nombre de usuario ya registrado")
    db.add(usuario)
    await db.refresh(usuario)
    return usuario


@router.post("/iniciar_sesion", status_code=200)
async def iniciar_sesion(usuario: Usuario, db: AsyncSession = Depends(get_db)):
    from sqlalchemy import select

    result = await db.execute(
        select(Usuario).where(Usuario.nombre_de_usuario == usuario.nombre_de_usuario)
    )
    db_usuario = result.scalars().first()
    if not db_usuario or not db_usuario.verificar_password(usuario.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"mensaje": "Inicio de sesión exitoso"}
