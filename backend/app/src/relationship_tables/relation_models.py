from sqlalchemy import Column, Table, Integer, String, ForeignKey, UniqueConstraint, DateTime, func

from app.database import Base


SongArtist = Table('song_artist', Base.metadata,
                   Column('id', Integer, primary_key=True),
                   Column('song_id', Integer, ForeignKey('songs.id', ondelete='CASCADE')),
                   Column('artist_id', Integer, ForeignKey('artists.id', ondelete='SET NULL')),
                   UniqueConstraint('song_id', 'artist_id', name='uix_1')
                   )

SongComments = Table('song_comments', Base.metadata,
                     Column('id', Integer, primary_key=True),
                     Column('song_id', Integer, ForeignKey('songs.id', ondelete='CASCADE')),
                     Column('user_id', Integer, ForeignKey('users.id', ondelete='CASCADE')),
                     Column('comm_text', String, nullable=False),
                     Column('created_at', DateTime, server_default=func.now()),
                     Column('updated_at', DateTime, server_default=func.now(), onupdate=func.now()),
                     )

SongLikes = Table('song_likes', Base.metadata,
                   Column('id', Integer, primary_key=True),
                   Column('song_id', Integer, ForeignKey('songs.id', ondelete='CASCADE')),
                   Column('user_id', Integer, ForeignKey('users.id', ondelete='CASCADE')),
                   UniqueConstraint('song_id', 'user_id', name='uix_2')
                   )