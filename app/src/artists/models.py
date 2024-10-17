from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Artists(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    nick = Column(String(50), nullable=False, unique=True)
    slug = Column(String(50), unique=True)
    avatar = Column(String)
    song_id = relationship('songs', secondary=SongArtist, backref='artists')


