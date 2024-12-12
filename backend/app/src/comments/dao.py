from sqlalchemy import select

from app.dao.base_dao import BaseDao
from app.database import async_session_marker
from app.src.relationship_tables.relation_models import SongComments


class CommentDao(BaseDao):

    model = SongComments

    @classmethod
    async def get_comments_by_song_id(cls, song_id: int):
        async with async_session_marker() as session:
            comments = (
                select(
                    SongComments
                )
                .where(SongComments.c.song_id == song_id)
            )
            result = await session.execute(comments)
            # print(result.mappings().first())
            return result.mappings().all()

    @classmethod
    async def get_comment_by_id(cls, comment_id: int):
        async with async_session_marker() as session:
            comment = (
                select(
                    SongComments
                )
                .where(SongComments.c.id == comment_id)
            )
            result = await session.execute(comment)
            return result.mappings().first()


    # @classmethod
    # async def create_comment_by_song_id(cls, song_id: int, comment: str):
    #     async with async_session_marker() as session:
    #         pass