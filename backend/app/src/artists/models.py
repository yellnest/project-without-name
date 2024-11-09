from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.src.relationship_tables.relation_models import SongArtist


class Artists(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    nick = Column(String(50), nullable=False)
    slug = Column(String(50), unique=True)
    avatar = Column(String)
    song_id = relationship('Songs', secondary=SongArtist, back_populates='artist_id')


