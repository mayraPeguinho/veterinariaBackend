from pydantic import BaseModel


class ResponsableCreate(BaseModel):
    acepta_recordatorios: bool = None


class ResponsableOut(ResponsableCreate):
    id: int
