from datetime import UTC, datetime, timedelta
from typing import Annotated
from jose import jwt, JWTError
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from models.user import User
from database import SessionLocal

SECRET_KEY = "dsdAM_-vpRGw6b4G7E7xltoYpDZz2M0dsunTAmm0pjE" #en el env, en cmd se ejecuta python -c "import secrets; print(secrets.token_urlsafe(32))"
ALGORITHM = "HS256"
EXPIRE_MINUTES = 30 #minutos de expiracion del token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def create_token(data: dict): #recibe la data como diccionario
    to_encode = data.copy() #se guarda una copia de lo que trae data
    expire = datetime.now(UTC) + timedelta(minutes=30) 
    to_encode.update({"exp": expire}) #al diccionario se le agrega el tiempo de expiracion, es decir los 30 min
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) #esto es el token
    return encoded_jwt
    
    
def get_db(): #crea la conexion
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = HTTPException( #esto es el error
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) #decodifica el token con la secret key y el tipo de algoritmo
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first() #no se que se hace aqui
    if user is None:
        raise credentials_exception #muestra el error
    return user