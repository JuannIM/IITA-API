"""
This module contains the API routes for managing books in the application.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, services, database
from .services import get_db

router = APIRouter()

# Ruta para obtener todos los libros
@router.get("/books", response_model=list[models.BookResponse])
def read_books(db: Session = Depends(services.get_db)):
    return services.get_books(db)

# Ruta para obtener un libro por ID
@router.get("/books/{book_id}", response_model=models.BookResponse)
def read_book(book_id: int, db: Session = Depends(services.get_db)):
    book = services.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Ruta para crear un libro
@router.post("/books", response_model=models.BookResponse)
def create_book(book: models.BookCreate, db: Session = Depends(services.get_db)):
    return services.create_book(db, book)

# Ruta para eliminar un libro
@router.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(services.get_db)):
    book = services.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}
