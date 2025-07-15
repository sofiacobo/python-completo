from pydantic import BaseModel

class ReservaCreate(BaseModel):
    cliente: str
    fecha: str
    cantidad: int

class ReservaOut(BaseModel):
    id: int
    cliente: str
    fecha: str
    cantidad: int

    class Config: #esto es para decirle que trabaje como orm
        orm_mode = True