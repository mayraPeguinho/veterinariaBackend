from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db
from schemas.usuario import *
from services import usuarios as services_usuarios
from security.auth import requierePermiso, puedeRealizarAccionUsuario
from typing import List, Optional
from starlette import status
from utils.enums import UsuariosOrderBy

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=UsuariosPaginado,
    dependencies=[Depends(requierePermiso("ver_usuarios"))],
)
async def obtenerUsuarios(
    db: AsyncSession = Depends(get_db),
    limit: int = Query(50, ge=1),
    offset: int = Query(0, ge=0),
    order_by: UsuariosOrderBy = Query(UsuariosOrderBy.nombre_de_usuario),
    order_direction: Optional[str] = Query("asc"),
):
    return await services_usuarios.obtenerPaginado(
        db, limit, offset, order_by, order_direction
    )


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
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
    status_code=status.HTTP_200_OK,
    response_model=UsuarioOut,
)
async def modificarUsuario(
    usuario: UsuarioActualEdit,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(requierePermiso("editar_usuario")),
):
    return await services_usuarios.modificarActual(db, usuario, current_user)


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=UsuarioOut,
)
async def modificarUsuarioPorId(
    id: int,
    usuario: UsuarioEdit,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(requierePermiso("editar_usuarios")),
):
    return await services_usuarios.modificar(db, id, usuario, current_user)


@router.post("/internos", status_code=status.HTTP_200_OK, response_model=UsuarioOut)
async def registrarUsuario(
    usuario: UsuarioInternoCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(requierePermiso("crear_usuario")),
):
    return await services_usuarios.registrarUsuarioInterno(
        db, usuario, current_user=current_user
    )


@router.post("/externos", status_code=status.HTTP_200_OK, response_model=UsuarioOut)
async def registrarUsuarioCliente(
    usuario: UsuarioExternoCreate,
    db: AsyncSession = Depends(get_db),
):
    return await services_usuarios.registrarUsuarioExterno(db, usuario)
