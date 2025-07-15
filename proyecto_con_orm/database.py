from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./reservas.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) #ver que es esto
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bing=engine)
Base = declarative_base()