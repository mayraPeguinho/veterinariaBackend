from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db
from schemas.usuario import UsuarioCreate, UsuarioOut
from schemas.auth import TokenResponse
from services import auth as service_auth
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated
from security.auth import getCurrentUser

router = APIRouter(prefix="/auth", tags=["auth"])


# SOLO USUARIOS DE TIPO CLIENTE, LIMITA ROL, FALTA IMPLEMENTAR
# Agregar un endpoint protegido para que crear usuarios con cualquier tipo de rol
@router.post("/registrar", status_code=201, response_model=UsuarioOut)
async def registrarUsuario(
    usuario: UsuarioCreate,
    db: AsyncSession = Depends(get_db),
):
    return await service_auth.registrarUsuario(db, usuario)


@router.post("/login", status_code=200, response_model=TokenResponse)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncSession = Depends(get_db),
):
    return await service_auth.login(db, form_data.username, form_data.password)


@router.get("/perfil", status_code=200, response_model=UsuarioOut)
async def obtenerPerfil(
    username: str = Depends(getCurrentUser), db: AsyncSession = Depends(get_db)
):
    return await service_auth.obtenerUsuarioPorNombreDeUsuario(db, username)
