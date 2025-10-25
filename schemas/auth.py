from pydantic import BaseModel, Field


class TokenResponse(BaseModel):
    access_token: str = Field(...)
    refresh_token: str = Field(...)
    token_type: str = Field("bearer", description="Tipo de token")
