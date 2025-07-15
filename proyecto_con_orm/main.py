from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from modelo import Reserva

Base.metadata.create_all(bind = engine) #esto crea las tablas que heredan de base en modelo.py por ej reserva

app = FastAPI()

#Dependencia para obtener la sesion de bd
def get_db(): #me conecto a la bd 
    db = SessionLocal() #abre una nueva sesión (conexión) con la BD
    try:
        yield db #trae la sesion para usar en los endpoints como get, post, etc.
    finally:
        db.close() #cuando termina cierra la conexion

#Esquema Pydantic
class ReservaSchema(BaseModel):
    cliente: str
    fecha : str
    cantidad: int 

class ReservaOut(ReservaSchema):
    id : int
    class Config:
        orm_mode = True

@app.post("/reservas", response_model= ReservaOut)
def crear_reserva(reserva : ReservaSchema, db: Session = Depends(get_db)): #le paso la reserva, la bd 
    r = Reserva(**reserva.model_dump())
    db.add(r)
    db.commit()
    db.refresh(r)
    return r

@app.get("/reservas")
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(Reserva).all()