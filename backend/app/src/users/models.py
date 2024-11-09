import enum

from sqlalchemy import Column, Integer, String, Enum, Boolean
from sqlalchemy.orm import relationship

from app.database import Base, CreatedAndUpdatedFields
from app.src.relationship_tables.relation_models import SongComments, SongLikes


class EnglishLevel(enum.Enum):
    IDK = 'I do not know'
    A1 = 'A1'
    A2 = 'A2'
    B1 = 'B1'
    B2 = 'B2'
    C1 = 'C1'


class Users(Base, CreatedAndUpdatedFields):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    user_password = Column(String(50), nullable=False)
    email = Column(String, nullable=False, unique=True)
    eng_lvl = Column(Enum(EnglishLevel), nullable=False)
    avatar = Column(String)
    is_admin = Column(Boolean, default=False, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    song_comment_id = relationship('Songs', secondary=SongComments, back_populates='comment')
    song_like_id = relationship('Songs', secondary=SongLikes, back_populates='likes')
