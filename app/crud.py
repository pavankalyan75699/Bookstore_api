from sqlalchemy.orm import Session
from app.models import Book

def create_book(db: Session, book: Book):
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_books(db: Session):
    return db.query(Book).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, updates: dict):
    book = get_book(db, book_id)
    if book:
        for key, value in updates.items():
            setattr(book, key, value)
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book
def search_books(
    db:Session,
    title:str=None,
    author:str=None,
    genre:str=None,
    min_price:float=None,
    max_price:float=None      
):
    db.query(Book)
    if title:
        query=query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query=query.filter(Book.author.ilike(f"%{author}%"))
    if genre:
        query=query.filter(Book.genre.ilike(f"%{genre}%"))
    if min_price is not None:
        query=query.filter(Book.price >= min_price)
    if max_price is not None:
        query = query.filter(Book.price <= max_price)
    return query.all()