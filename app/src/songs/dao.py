from app.dao.base_dao import BaseDao
from app.src.songs.models import Songs


class SongsDao(BaseDao):
    model = Songs
