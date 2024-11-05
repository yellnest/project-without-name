from fastapi import APIRouter, Depends

from app.base.servieces import handle_errors
from app.exceptions import NoSuchItem, SuccessRequest
from app.src.artists.dao import ArtistDao
from app.src.artists.schemas import ArtistSchema, CreateArtistSchema

router = APIRouter(
    prefix="/artists",
    tags=["artists"],
)


@router.get("/all")
async def get_all_artists() -> list[ArtistSchema]:
    return await ArtistDao.get_all()


@router.get("/{artist_id}")
async def get_artist_by_id(artist_id: int) -> ArtistSchema:
    artist = await ArtistDao.get_by_id(artist_id)
    if artist is None:
        raise NoSuchItem
    return artist


@router.post("/create-artist")
@handle_errors
async def create_artist(artist: CreateArtistSchema):
    await ArtistDao.add_item(nick=artist.nick, slug=artist.slug, avatar=artist.avatar)


@router.delete("/{artist_id}", dependencies=[Depends(get_artist_by_id)])
async def delete_artist(artist_id: int):
    await ArtistDao.delete_by_id(model_id=artist_id)
    return SuccessRequest

# @router.get("/{artist_id}/edit") НА зметочку

@router.patch("/{artist_id}", dependencies=[Depends(get_artist_by_id)])
async def update_artist(artist_id: int, artist: CreateArtistSchema):
    await ArtistDao.update_by_id(model_id=artist_id, nick=artist.nick, slug=artist.slug, avatar=artist.avatar)
    return SuccessRequest
