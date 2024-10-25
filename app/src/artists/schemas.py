from pydantic import BaseModel

class ArtistSchema(BaseModel):
    id: int
    nick: str
    slug: str
    avatar: str | None


class CreateArtistSchema(BaseModel):
    nick: str
    slug: str
    avatar: str | None
