from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base, CreatedAndUpdatedFields


class Comments(Base, CreatedAndUpdatedFields):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    song_id = Column(Integer, ForeignKey('songs.id'), nullable=False)
    comm_text = Column(String, nullable=False)

