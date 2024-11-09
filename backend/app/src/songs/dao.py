from sqlalchemy import select, func, alias

from app.dao.base_dao import BaseDao
from app.database import async_session_marker

from app.src.artists.models import Artists
from app.src.genre.models import Genre
from app.src.songs.models import Songs

from app.src.relationship_tables.relation_models import SongArtist, SongLikes
from app.src.users.models import Users


class SongsDao(BaseDao):
    model = Songs


    @classmethod
    async def show_all_songs(cls):
        async with async_session_marker() as session:

            # Define the subquery
            subquery = select(SongLikes.c.song_id, func.count(SongLikes.c.user_id).label('like_count')) \
                .group_by(SongLikes.c.song_id) \
                .subquery('sl')

            # Alias the subquery for easier reference
            sl = alias(subquery, name='sl')

            all_song_foreign_keys = (
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
                    func.coalesce(sl.c.like_count, 0).label('like_count')
                    # func.json_agg(func.json_build_object('name', Artists.nick)).label('artists')
            )
                .select_from(Songs)
                .join(Genre, Songs.genre_id == Genre.id)

                # list of related artists of the song
                .join(SongArtist, SongArtist.c.song_id == Songs.id, isouter=True)
                .join(Artists, SongArtist.c.artist_id == Artists.id, isouter=True)

                # likes amount of the song
                .join(sl, sl.c.song_id == Songs.id, isouter=True)

                .group_by(
                    Songs.id,
                    Genre.title,
                    sl.c.like_count
                )
            )
            result = await session.execute(all_song_foreign_keys)
            return result.mappings().all()

