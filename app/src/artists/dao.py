from app.dao.base_dao import BaseDao
from app.src.artists.models import Artists


class ArtistDao(BaseDao):
    model = Artists

