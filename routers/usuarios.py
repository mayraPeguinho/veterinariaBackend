from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db
from schemas.usuario import (
    UsuarioCreate,
    UsuarioClienteCreate,
    UsuarioOut,
    UsuarioOutBase,
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
)
async def obtenerUsuario(
    id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(puedeRealizarAccionUsuario),
):
    return await services_usuarios.obtenerPorId(db, id)


# @router.put(
#     "/{id}",
#     status_code=200,
#     response_model=UsuarioOut,
#     current_user=Depends(puedeRealizarAccionUsuario),
# )
# async def modificarUsuario(
#     id: int,
#     usuario: UsuarioCreate,
#     db: AsyncSession = Depends(get_db),
#     current_user=Depends(puedeRealizarAccionUsuario),
# ):
#     return await services_usuarios.modificar(db, id)


@router.post("", status_code=200, response_model=UsuarioOut)
async def registrarUsuario(
    usuario: UsuarioCreate,
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(requierePermiso("crear_usuario")),
):
    return await services_usuarios.registrarUsuario(
        db, usuario, current_user=current_user
    )


@router.post("/clientes", status_code=200, response_model=UsuarioOut)
async def registrarUsuarioCliente(
    usuario: UsuarioClienteCreate,
    db: AsyncSession = Depends(get_db),
):
    return await services_usuarios.registrarUsuario(db, usuario)
