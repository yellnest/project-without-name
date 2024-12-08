from datetime import datetime

from pydantic import BaseModel


class CommentSchema(BaseModel):
    id: int
    song_id: int
    user_id: int
    comm_text: str
    created_at: datetime
    updated_at: datetime


class CommentCreateSchema(BaseModel):
    song_id: int
    user_id: int
    comm_text: str

