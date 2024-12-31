from pydantic import BaseModel


class Article(BaseModel):
    id: int
    title: str
    link: str
