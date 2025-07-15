from sqlalchemy import Column, Integer, String

from database import Base


class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente = Column(String, index=True)
    fecha = Column(String)
    cantidad = Column(Integer)
    