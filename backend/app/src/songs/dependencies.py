from app.exceptions import NoSuchItemException
from app.src.songs.dao import SongsDao


async def valid_song_id(song_id: int):
    answer = await SongsDao.get_one_or_none(id=song_id)
    if answer:
        return answer
    raise NoSuchItemException
