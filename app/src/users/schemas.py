from datetime import datetime

from pydantic import EmailStr, BaseModel


class UserSchema(BaseModel):
    id: int
    user_name: str
    email: EmailStr
    user_password: str
    eng_lvl: str
    avatar: str | None
    is_admin: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime


class UserRegistrationSchema(BaseModel):
    user_name: str
    email: EmailStr
    user_password: str
    eng_lvl: str



