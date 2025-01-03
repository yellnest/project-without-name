from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import Field

from app.src.songs.models import EnglishAccentChoice, Songs


class SongFilter(Filter):
    accent: Optional[EnglishAccentChoice] = None
    total_diff__gte: Optional[int] = None
    genre_id: Optional[int] = None
    published: Optional[bool] = None

    class Constants(Filter.Constants):
        model = Songs
