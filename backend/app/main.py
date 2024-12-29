from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import RedisError

from fastapi import FastAPI

from app.config import settings
from app.src.users.router import router as user_router
from app.src.songs.router import router as song_router
from app.src.genre.router import router as genre_router
from app.src.artists.router import router as artist_router
from app.src.comments.router import router as comment_router


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    try:
        redis = settings.get_redis_connection()
        redis.ping()
        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    except RedisError as e:
        raise RedisError(f"Ошибка подключения к Redis: {e}")
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
app.include_router(song_router)
app.include_router(genre_router)
app.include_router(artist_router)
app.include_router(comment_router)
