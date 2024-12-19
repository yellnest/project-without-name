from sqlalchemy import select, func, delete, and_
from sqlalchemy.dialects.mysql import insert

from app.dao.base_dao import BaseDao
from app.database import async_session_marker

from app.src.artists.models import Artists
from app.src.genre.models import Genre
from app.src.songs.models import Songs

from app.src.relationship_tables.relation_models import SongArtist, SongLikes


class SongsDao(BaseDao):
    model = Songs

    @classmethod
    def _construct_song_query(cls, song_id=None, user_id=None):
        query = (
            select(
                Songs.id,
                Songs.title,
                Songs.slug,
                Songs.slang,
                Songs.ambiguity,
                Songs.flow,
                Songs.words_slurring,
                Songs.total_diff,
                Songs.description,
                Songs.published,
                Songs.accent,
                Genre.title.label('genre_name'),
                func.json_agg(Artists.nick).label('artists'),
            )
            .select_from(Songs)
            .join(Genre, Songs.genre_id == Genre.id)
            .join(SongArtist, SongArtist.c.song_id == Songs.id, isouter=True)
            .join(Artists, SongArtist.c.artist_id == Artists.id, isouter=True)
            .group_by(
                Songs.id,
                Genre.title
            )
        )
        if song_id:
            query = query.where(Songs.id == song_id)
        elif user_id:
            query = (
                query.join(SongLikes, SongLikes.c.song_id == Songs.id, isouter=True)
                .where(SongLikes.c.user_id == user_id)
            )
        return query

    @classmethod
    async def show_all_songs(cls):
        async with async_session_marker() as session:
            query = cls._construct_song_query()
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def show_song_by_id(cls, song_id):
        async with async_session_marker() as session:
            query = cls._construct_song_query(song_id=song_id)
            song_by_result = await session.execute(query)
            return song_by_result.mappings().first()

    """Удаление и просмотр лайков"""
    @classmethod
    async def get_user_likes(cls, user_id):
        async with async_session_marker() as session:
            query = cls._construct_song_query(user_id=user_id)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def delete_like(cls, user_id, song_id):
        async with (async_session_marker() as session):
            delete_artist = (
                delete(SongLikes)
                .where(
                    and_(
                        SongLikes.c.song_id == song_id, SongLikes.c.user_id == user_id
                    )
                )
            )
            await session.execute(delete_artist)
            await session.commit()

    """Удаление исполнителей у песни"""
    @classmethod
    async def delete_artist_of_song_by_id(cls, song_id, artist_id):
        async with (async_session_marker() as session):
            delete_artist = (
                delete(SongArtist)
                .where(
                    and_(
                        SongArtist.c.song_id == song_id, SongArtist.c.artist_id == artist_id
                    )
                )
            )
            await session.execute(delete_artist)
            await session.commit()


class SongLikesDao(BaseDao):
    model = SongLikes


class SongArtistDao(BaseDao):
    model = SongArtist
