from sqlalchemy.orm import Session
from . import models, database

# Obtener sesión de base de datos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear un nuevo libro
def create_book(db: Session, book: models.BookCreate):
    db_book = database.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Obtener todos los libros
def get_books(db: Session):
    return db.query(database.Book).all()

# Obtener un libro por ID
def get_book_by_id(db: Session, book_id: int):
    return db.query(database.Book).filter(database.Book.id == book_id).first()

# Eliminar un libro
def delete_book(db: Session, book_id: int):
    book = get_book_by_id(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book
