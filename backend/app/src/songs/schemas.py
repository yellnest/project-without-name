from pydantic import BaseModel, Field


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
    genre_name: str
    artists: list[str | None]

class CreateSongSchema(BaseModel):
    title: str
    slug: str
    slang: float = Field(ge=1, le=10)
    ambiguity: float = Field(ge=1, le=10)
    flow: float = Field(ge=1, le=10)
    words_slurring: float = Field(ge=1, le=10)
    description: str
    published: bool
    accent: str
    genre_id: int
