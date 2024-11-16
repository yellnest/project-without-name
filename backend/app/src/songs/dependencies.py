from sqlalchemy import select

from app.database import async_session_marker
from app.exceptions import NoSuchItem
from app.src.songs.models import Songs


async def item_exists_or_not(song_id: int):
    async with async_session_marker() as session:
        item = (
            select(
                Songs.id
            )
            .where(Songs.id == song_id)
        )
        result = await session.execute(item)
        answer = result.mappings().all()
        if answer:
            return
        raise NoSuchItem