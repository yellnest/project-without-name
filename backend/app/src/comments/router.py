from fastapi import APIRouter
from fastapi.params import Depends

from app.src.comments.dao import CommentDao
from app.src.comments.schema import CommentSchema, CommentCreateSchema
from app.src.songs.dependencies import valid_song_id
from app.src.users.dependencies import get_current_user

router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

@router.get("/{song_id}", dependencies=[Depends(valid_song_id)])
async def get_all_comm_by_song(song_id:int) -> list[CommentSchema]:
    return await CommentDao.get_comments_by_song_id(song_id=song_id)



@router.post("/{song_id}", dependencies=[Depends(valid_song_id)])
async def create_comment_by_id(song_id: int, comm_text=str, user_id: CommentCreateSchema = Depends(get_current_user)):
    return await CommentDao.add_item(song_id=song_id, user_id=user_id.id, comm_text=comm_text)
