from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db
from schemas.usuario import (
    UsuarioInternoCreate,
    UsuarioExternoCreate,
    UsuarioOut,
    UsuarioOutBase,
    UsuarioActualEdit,
)
from services import usuarios as services_usuarios
from security.auth import requierePermiso, puedeRealizarAccionUsuario
from typing import List

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.get(
    "",
    status_code=200,
    response_model=List[UsuarioOutBase],
    dependencies=[Depends(requierePermiso("ver_usuarios"))],
)
async def obtenerUsuarios(db: AsyncSession = Depends(get_db)):
    return await services_usuarios.obtenerTodos(db)


@router.get(
    "/{id}",
    status_code=200,
    response_model=UsuarioOut,
    dependencies=[Depends(puedeRealizarAccionUsuario)],
)
async def obtenerUsuario(
    id: int,
    db: AsyncSession = Depends(get_db),
):
    return await services_usuarios.obtenerPorId(db, id)


@router.put(
    "/me",
    status_code=200,
    response_model=UsuarioOut,
)
async def modificarUsuario(
    usuario: UsuarioActualEdit,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(requierePermiso("editar_usuario")),
):
    return await services_usuarios.modificarUsuarioActual(db, usuario, current_user)


@router.post("/internos", status_code=200, response_model=UsuarioOut)
async def registrarUsuario(
    usuario: UsuarioInternoCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(requierePermiso("crear_usuario")),
):
    return await services_usuarios.registrarUsuarioInterno(
        db, usuario, current_user=current_user
    )


@router.post("/externos", status_code=200, response_model=UsuarioOut)
async def registrarUsuarioCliente(
    usuario: UsuarioExternoCreate,
    db: AsyncSession = Depends(get_db),
):
    return await services_usuarios.registrarUsuarioExterno(db, usuario)
