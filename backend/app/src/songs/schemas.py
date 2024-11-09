from pydantic import BaseModel


class SongSchema(BaseModel):
    id: int
    title: str
    slug: str
    slang: float
    ambiguity: float
    flow: float
    words_slurring: float
    total_diff: float
    description: str
    published: bool
    accent: str
    genre_id: int

class CreateSongSchema(BaseModel):
    title: str
    slug: str
    slang: float
    ambiguity: float
    flow: float
    words_slurring: float
    description: str
    published: bool
    accent: str
    genre_id: int
