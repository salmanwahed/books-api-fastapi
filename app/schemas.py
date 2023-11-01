from typing import List, Union

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    preface: Union[str, None] = None


class BookCreate(BookBase):
    author_id: int


class AuthorBase(BaseModel):
    name: str


class Book(BookBase):
    id: int
    author: Union[AuthorBase, None] = None

    class Config:
        orm_mode = True


class Author(AuthorBase):
    id: int
    books: List[BookBase] = []

    class Config:
        orm_mode = True
