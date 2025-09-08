from pydantic import BaseModel


class RolOut(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True
