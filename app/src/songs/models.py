import enum

from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Computed, Enum
from sqlalchemy.orm import relationship

from app.database import Base
from app.src.relationship_tables.relation_models import SongArtist, SongComments, SongLikes


class EnglishAccentChoice(enum.Enum):
    american = 'american'
    british = 'british'



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
