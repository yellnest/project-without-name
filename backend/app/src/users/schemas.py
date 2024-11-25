from datetime import datetime
from typing import Any

from pydantic import EmailStr, BaseModel, model_validator

from app.exceptions import PasswordsDoNotMatchException


class UserSchema(BaseModel):
    id: int
    user_name: str
    user_password: str
    email: EmailStr
    user_password: str
    eng_lvl: str
    avatar: str | None
    is_admin: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime


class UserLoginSchema(BaseModel):
    email: EmailStr
    user_password: str


class UserRegistrationSchema(UserLoginSchema):
    repeat_password: str
    user_name: str

    # eng_lvl: str

    @model_validator(mode='before')
    def check_passwords_match(cls, values: dict[str, Any]) -> dict[str, Any]:
        # Comparing two passwords before returning
        password = values.get('user_password')
        password_repeat = values.get('repeat_password')
        if password != password_repeat:
            raise PasswordsDoNotMatchException
        return values


class UserUpdateSchema(BaseModel):
    user_name: str
    email: EmailStr
    eng_lvl: str
