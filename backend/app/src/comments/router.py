from fastapi import APIRouter
from fastapi.params import Depends

from app.src.comments.dao import CommentDao
from app.src.songs.dependencies import valid_song_id

router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

@router.get("/{song_id}", dependencies=[Depends(valid_song_id)])
async def get_all_comm_by_song(song_id:int):
    return await CommentDao.get_comments_by_song_id(song_id=song_id)


# async def create_comment_by_id:
#     return await CommentDao.add_item()
