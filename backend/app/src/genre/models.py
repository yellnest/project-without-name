from sqlalchemy import Column, Integer, String
from app.database import Base


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False, unique=True)
    slug = Column(String(35), unique=True)
