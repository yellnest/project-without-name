import enum

from sqlalchemy import Column, Table, Integer, String, Float, Boolean, ForeignKey, Computed, Enum, UniqueConstraint, \
    DateTime, func
from sqlalchemy.orm import relationship

from app.database import Base


class EnglishAccentChoice(enum.Enum):
    american = 'american'
    british = 'british'


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


class Songs(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    slug = Column(String(60), nullable=False, unique=True)
    slang = Column(Float, nullable=False)
    ambiguity = Column(Float, nullable=False)
    flow = Column(Float, nullable=False)
    words_slurring = Column(Float, nullable=False)
    total_diff = Column(Float, Computed("(slang + ambiguity + flow + words_slurring) / 4"))
    description = Column(String, nullable=False)
    published = Column(Boolean, default=False)
    accent = Column(Enum(EnglishAccentChoice))
    artist_id = relationship('Artists', secondary=SongArtist, back_populates='song_id')
    comment = relationship('Users', secondary=SongComments, back_populates='song_comment_id')
    likes = relationship('Users', secondary=SongLikes, back_populates='song_like_id')
    genre_id = Column(Integer, ForeignKey('genre.id', ondelete='SET NULL'), nullable=False)
