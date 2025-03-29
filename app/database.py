from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base de datos SQLite
DATABASE_URL = "sqlite:///./library.db"

# Crear motor de base de datos
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()

# Modelo de libro en la base de datos
class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    category = Column(String, index=True)
    available = Column(Boolean, default=True)

# Crear tablas en la base de datos
def init_db():
    Base.metadata.create_all(bind=engine)
