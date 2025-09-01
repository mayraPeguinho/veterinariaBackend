from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db
from schemas import usuario as schema_usuario
from services import auth as service_auth


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/", status_code=201, response_model=schema_usuario.UsuarioOut)
async def crear_usuario(
    usuario: schema_usuario.UsuarioCreate,
    db: AsyncSession = Depends(get_db),
):
    # Validaciones
    return await service_auth.usuario_creado(usuario, db)
