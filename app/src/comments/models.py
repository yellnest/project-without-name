from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    song_id = Column(Integer, ForeignKey('songs.id'), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    comm_text = Column(String, nullable=False)
