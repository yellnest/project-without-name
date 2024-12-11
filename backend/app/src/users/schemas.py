from datetime import datetime
from typing import Optional

from pydantic import EmailStr, BaseModel

from app.src.users.models import EnglishLevel


class BaseUserSchema(BaseModel):
    user_name: Optional[str]
    email: Optional[EmailStr]
    eng_lvl: Optional[EnglishLevel]
    avatar: Optional[str]


class UserSchema(BaseUserSchema):
    id: int
    is_admin: Optional[bool] = False
    is_superuser: Optional[bool] = False
    user_password: str
    created_at: datetime
    updated_at: datetime


class UserLoginSchema(BaseModel):
    email: EmailStr
    user_password: str


class UserRegistrationSchema(UserLoginSchema, BaseUserSchema):
    repeat_password: str


class UserUpdateSchema(BaseUserSchema):
    pass

class UserUpdatePasswordSchema(BaseModel):
    current_password: str
    user_password: str
    repeat_password: str


# class UserUpdateSchema(BaseModel):
#     # __annotations__ = {k: Optional[v] for k, v in UserCreate.__annotations__.items()}
#
#     user_name: Optional[str] = None
#     email: Optional[EmailStr] = None
#     eng_lvl: Optional[EnglishLevel] = None
#     user_password: Optional[str] = None
#     repeat_password: Optional[str] = None
