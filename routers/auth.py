from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db
from schemas.auth import TokenResponse
from services import auth as service_auth
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", status_code=200, response_model=TokenResponse)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncSession = Depends(get_db),
):
    return await service_auth.login(db, form_data.username, form_data.password)
