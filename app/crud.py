from sqlalchemy.orm import Session
from . import models, schemas


def create_author(db: Session, author: schemas.AuthorBase):
    db_author = models.Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def create_book(db: Session, book: schemas.BookBase):
    db_book = models.Book(title=book.title, author_id=book.author_id, preface=book.preface)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session):
    return db.query(models.Book).all()


def get_authors(db: Session):
    return db.query(models.Author).all()
