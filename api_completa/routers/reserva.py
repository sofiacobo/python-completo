from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.jwt import get_current_user, get_db
from schemas.reserva import ReservaCreate, ReservaOut
from models.reserva import Reserva


router = APIRouter(prefix="/reservas", tags=["reservas"])

#CREACION DE ENDPOINTS
@router.post("/reservas", response_model= ReservaOut)
def crear_reserva(reserva : ReservaCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)): #le paso la reserva, la bd 
    r = Reserva(**reserva.model_dump()) #se transforma con model dump en una instancia de reserva
    db.add(r) #esto es como un insert into en codigo sql
    db.commit()
    db.refresh(r)
    return r

@router.get("/", response_model = List[ReservaOut]) #la respuesta es una lista de reservas
def listar_reservas(db: Session = Depends(get_db), user=Depends(get_current_user)): #get current es proteccion para el endpoint
    return db.query(Reserva).all()