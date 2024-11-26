from jose import jwt, JWTError, ExpiredSignatureError

from app.config import settings
from app.exceptions import UserAlreadyExistsException, TokenIsNotExistException, WrongTokenFormatException, \
    TokenExpiredException
from app.src.users.dao import UserDAO

from fastapi import Request, Depends


async def email_already_exist(email: str):
    answer = await UserDAO.get_one_or_none(email=email)
    if answer:
        raise UserAlreadyExistsException
    return email


def get_token(request: Request):
    token = request.cookies.get('access_token')
    if not token:
        raise TokenIsNotExistException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except ExpiredSignatureError as e:
        raise TokenExpiredException
    user_id = payload.get('sub')
    user = await UserDAO.get_by_id(int(user_id))
    return user
