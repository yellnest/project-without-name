from app.dao.base_dao import BaseDao
from app.src.genre.models import Genre


class GenreDao(BaseDao):
    model = Genre

