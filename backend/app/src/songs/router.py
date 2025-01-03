from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from fastapi_filter import FilterDepends
from app.base.servieces import handle_errors
from app.exceptions import SuccessRequest
from app.src.songs.dao import SongsDao, SongLikesDao, SongArtistDao
from app.src.songs.dependencies import valid_song_id
from app.src.songs.filters import SongFilter
from app.src.songs.schemas import SongSchema, CreateSongSchema, UpdateSongSchema
from app.src.users.dependencies import get_current_user

router = APIRouter(
    prefix="/songs",
    tags=["songs"],
)


@router.get("/all")
@cache(expire=20)
async def get_all_songs(song_filter: SongFilter = FilterDepends(SongFilter), user_id: SongSchema = Depends(get_current_user)) -> list[SongSchema]:
    return await SongsDao.show_all_songs(song_filter, user_id)


@router.get("/{song_id}", dependencies=[Depends(valid_song_id)])
async def get_song_by_id(song_id: int) -> SongSchema:
    return await SongsDao.show_song_by_id(song_id)


@router.post("/create-song")
@handle_errors
async def create_song(user_data: CreateSongSchema):
    await SongsDao.add_item(title=user_data.title, slug=user_data.slug, slang=user_data.slang,
                            ambiguity=user_data.ambiguity, flow=user_data.flow, words_slurring=user_data.words_slurring,
                            description=user_data.description, published=user_data.published, accent=user_data.accent,
                            genre_id=user_data.genre_id)


@router.delete("/{song_id}", dependencies=[Depends(valid_song_id)])
async def delete_song_by_id(song_id: int):
    await SongsDao.delete_by_id(model_id=song_id)
    return SuccessRequest


@router.patch("/{song_id}", dependencies=[Depends(valid_song_id)])
@handle_errors
async def update_song_by_id(song_id: int, user_data: UpdateSongSchema):
    update_data = {key: value for key, value in user_data.model_dump(exclude_unset=True).items()}
    await SongsDao.update_by_id(song_id, **update_data)


@router.post("/artists")
@handle_errors
async def add_artist_to_song(song_id: int, artist_id: int):
    await SongArtistDao.add_item(song_id=song_id, artist_id=artist_id)


@router.delete("/artists/{song_id}", dependencies=[Depends(valid_song_id)])
@handle_errors
async def delete_artist_from_song(song_id: int, artist_id: int):
    await SongsDao.delete_artist_of_song_by_id(song_id=song_id, artist_id=artist_id)


@router.get("/like/{user_id}")
async def get_user_likes(user_id: SongSchema = Depends(get_current_user)):
    return await SongsDao.get_user_likes(user_id=user_id.id)


@router.post('/like', dependencies=[Depends(valid_song_id)])
@handle_errors
async def add_user_like(song_id: int, user_id: SongSchema = Depends(get_current_user)):
    await SongLikesDao.add_item(song_id=song_id, user_id=user_id.id)


@router.delete("/like/{song_id}", dependencies=[Depends(valid_song_id)])
@handle_errors
async def delete_artist_from_song(song_id: int, user_id: SongSchema = Depends(get_current_user)):
    await SongsDao.delete_like(song_id=song_id, user_id=user_id.id)
