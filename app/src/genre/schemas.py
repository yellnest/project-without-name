from pydantic import BaseModel

class GenreSchema(BaseModel):
    id: int
    title: str
    slug: str


class CreateGenreSchema(BaseModel):
    title: str
    slug: str
