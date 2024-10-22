import enum
from datetime import datetime

from sqlalchemy import Column, Integer, String, Enum, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class EnglishLevel(enum.Enum):
    IDK = 'I do not know'
    A1 = 'A1'
    A2 = 'A2'
    B1 = 'B1'
    B2 = 'B2'
    C1 = 'C1'


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    email = Column(String, nullable=False, unique=True)
    eng_lvl = Column(Enum(EnglishLevel), nullable=False)
    avatar = Column(String)
    is_admin = Column(Boolean, default=False, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
