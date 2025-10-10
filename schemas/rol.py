from pydantic import BaseModel, ConfigDict


class RolOut(BaseModel):
    id: int
    nombre: str

    model_config = ConfigDict(from_attributes=True)
