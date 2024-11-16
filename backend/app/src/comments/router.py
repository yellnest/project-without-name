from fastapi import APIRouter

from app.src.comments.dao import CommentDao

router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

@router.get("/{song_id}")
async def get_all_comm_by_song(song_id:int):
    return await CommentDao.get_comments_by_song_id(song_id=song_id)
