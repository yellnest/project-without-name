from fastapi import APIRouter, Depends

from app.base.servieces import handle_errors
from app.exeptions import NoSuchItem, SuccessRequest
from app.src.songs.dao import SongsDao
from app.src.songs.schemas import SongSchema, CreateSongSchema

router = APIRouter(
    prefix="/songs",
    tags=["songs"],
)


@router.get("/all")
async def get_all_songs() -> list[SongSchema]:
    return await SongsDao.get_all()


@router.get("/{song_id}")
async def get_song_by_id(song_id: int) -> SongSchema:
    song = await SongsDao.get_by_id(song_id)
    if song is None:
        raise NoSuchItem
    return song


@router.post("/create-song")
@handle_errors
async def create_song(user_data: CreateSongSchema):
    await SongsDao.add_item(title=user_data.title, slug=user_data.slug, slang=user_data.slang,
                            ambiguity=user_data.ambiguity, flow=user_data.flow, words_slurring=user_data.words_slurring,
                            description=user_data.description, published=user_data.published, accent=user_data.accent,
                            genre_id=user_data.genre_id)


@router.delete("/{song_id}", dependencies=[Depends(get_song_by_id)])
async def delete_song_by_id(song_id: int):
    await SongsDao.delete_by_id(model_id=song_id)
    return SuccessRequest


@router.patch("/{song_id}", dependencies=[Depends(get_song_by_id)])
async def update_song_by_id(song_id: int, user_data: CreateSongSchema):
    await SongsDao.update_by_id(model_id=song_id, title=user_data.title, slug=user_data.slug, slang=user_data.slang,
                            ambiguity=user_data.ambiguity, flow=user_data.flow, words_slurring=user_data.words_slurring,
                            description=user_data.description, published=user_data.published, accent=user_data.accent,
                            genre_id=user_data.genre_id)
    return SuccessRequest

