from fastapi import APIRouter, Depends

from app.base.servieces import handle_errors
from app.exceptions import SuccessRequest
from app.src.songs.dao import SongsDao
from app.src.songs.dependencies import item_exists_or_not
from app.src.songs.schemas import SongSchema, CreateSongSchema

router = APIRouter(
    prefix="/songs",
    tags=["songs"],
)


@router.get("/all")
async def get_all_songs() -> list[SongSchema]:
    return await SongsDao.show_all_songs()
    # return await SongsDao.get_all()


@router.get("/{song_id}")
async def get_song_by_id(song_id: int) -> SongSchema:
    return await SongsDao.show_song_by_id(song_id)


@router.post("/create-song")
@handle_errors
async def create_song(user_data: CreateSongSchema):
    await SongsDao.add_item(title=user_data.title, slug=user_data.slug, slang=user_data.slang,
                            ambiguity=user_data.ambiguity, flow=user_data.flow, words_slurring=user_data.words_slurring,
                            description=user_data.description, published=user_data.published, accent=user_data.accent,
                            genre_id=user_data.genre_id)


@router.delete("/{song_id}", dependencies=[Depends(item_exists_or_not)])
async def delete_song_by_id(song_id: int):
    await SongsDao.delete_by_id(model_id=song_id)
    return SuccessRequest


@router.patch("/{song_id}", dependencies=[Depends(item_exists_or_not)])
async def update_song_by_id(song_id: int, user_data: CreateSongSchema):
    await SongsDao.update_by_id(model_id=song_id, title=user_data.title, slug=user_data.slug, slang=user_data.slang,
                                ambiguity=user_data.ambiguity, flow=user_data.flow,
                                words_slurring=user_data.words_slurring,
                                description=user_data.description, published=user_data.published,
                                accent=user_data.accent,
                                genre_id=user_data.genre_id)
    return f'{SuccessRequest} + '


@router.post("/artists/{song_id}")
@handle_errors
async def add_artist_to_song(song_id: int, artist_id: int):
    await SongsDao.add_artist_of_song_by_id(song_id=song_id, artist_id=artist_id)


@router.delete("/artists/{song_id}", dependencies=[Depends(item_exists_or_not)])
async def delete_artist_from_song(song_id: int, artist_id: int):
    await SongsDao.delete_artist_of_song_by_id(song_id=song_id, artist_id=artist_id)
    return SuccessRequest
