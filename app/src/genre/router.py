from fastapi import APIRouter, Depends

from app.base.servieces import handle_errors
from app.exeptions import NoSuchItem, SuccessRequest
from app.src.genre.dao import GenreDao
from app.src.genre.schemas import GenreSchema, CreateGenreSchema


router = APIRouter(
    prefix="/genres",
    tags=["genre"],
)


@router.get("/all")
async def all_genres() -> list[GenreSchema]:
    return await GenreDao.get_all()


@router.get("/{genre_id}")
async def get_genre_by_id(genre_id: int) -> GenreSchema:
    genre = await GenreDao.get_by_id(genre_id)
    if genre is None:
        raise NoSuchItem
    return genre


@router.post("/create-genre")
@handle_errors
async def create_genre(genre: CreateGenreSchema):
    await GenreDao.add_item(title=genre.title, slug=genre.slug)


@router.delete("/{genre_id}", dependencies=[Depends(get_genre_by_id)])
async def delete_genre_by_id(genre_id: int):
    await GenreDao.delete_by_id(model_id=genre_id)
    return SuccessRequest


@router.patch("/{genre_id}", dependencies=[Depends(get_genre_by_id)])
async def update_genre_by_id(genre_id: int, genre: CreateGenreSchema):
    await GenreDao.update_by_id(model_id=genre_id, title=genre.title, slug=genre.slug)
    raise SuccessRequest
