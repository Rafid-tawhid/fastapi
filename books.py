from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import  UUID

app = FastAPI()

class Book(BaseModel):
    id:UUID
    title: str =Field(min_length=1, max_length=100)
    author: str =Field(min_length=1, max_length=100)
    discription: str =Field(min_length=1, max_length=100)
    rating: int =Field(gt=-1,lt=101)


BOOKS=[]

@app.get("/")
def read_root():
    return BOOKS

@app.post("/")
def create_book(book: Book):
    BOOKS.append(book)
    return book