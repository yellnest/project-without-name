import enum

from sqlalchemy import Column, Table, Integer, String, Float, Boolean, ForeignKey, Computed, Enum
from sqlalchemy.orm import relationship

from app.database import Base


class EnglishAccentChoice(enum.Enum):
    american = 'american'
    british = 'british'


SongArtist = Table('song_artist', Base.metadata,
                   Column('id', Integer, primary_key=True),
                   Column('song_id', Integer, ForeignKey('songs.id')),
                   Column('artist_id', Integer, ForeignKey('artists.id'))
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
    artist_id = relationship('artists', secondary=SongArtist, backref='songs')
    # artist_id = Column(Integer, ForeignKey('artists.id'), nullable=False)
    genre_id = Column(Integer, ForeignKey('genre.id'), nullable=False)
