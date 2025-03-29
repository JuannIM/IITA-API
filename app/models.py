from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    category: str
    available: bool = True

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True
