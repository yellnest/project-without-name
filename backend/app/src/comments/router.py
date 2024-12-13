from fastapi import APIRouter
from fastapi.params import Depends

from app.base.servieces import handle_errors
from app.exceptions import SuccessRequest
from app.src.comments.dao import CommentDao
from app.src.comments.dependencies import admin_or_owner
from app.src.comments.schema import CommentSchema, CommentCreateSchema
from app.src.songs.dependencies import valid_song_id
from app.src.users.dependencies import get_current_user

router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)


@router.get("/{song_id}", dependencies=[Depends(valid_song_id)])
async def get_all_comm_by_song(song_id: int) -> list[CommentSchema]:
    return await CommentDao.get_comments_by_song_id(song_id=song_id)


@router.post("/{song_id}", dependencies=[Depends(valid_song_id)])
@handle_errors
async def create_comment_by_id(song_id: int, comm_text: str, user_id: CommentCreateSchema = Depends(get_current_user)):
    await CommentDao.add_item(song_id=song_id, user_id=user_id.id, comm_text=comm_text)


@router.delete("/{comment_id}", dependencies=[Depends(admin_or_owner)])
async def delete_comment_by_id(comment_id: int):
    await CommentDao.delete_by_id(model_id=comment_id)
    raise SuccessRequest

@router.patch("/{comment_id}", dependencies=[Depends(admin_or_owner)])
@handle_errors
async def update_comment_by_id(comment_id: int, comm_text: str):
    await CommentDao.update_by_id(model_id=comment_id, comm_text=comm_text)
