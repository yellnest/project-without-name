from jose import jwt, ExpiredSignatureError, JWTError

from app.config import settings
from app.exceptions import UserAlreadyExistsException, TokenIsNotExistException, \
    TokenExpiredException, InvalidTokenException, InvalidTokenInformationException
from app.src.users.dao import UserDAO

from fastapi import Request, Depends

from app.src.users.permissions import check_permissions
from app.src.users.schemas import UserSchema


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
        user_id = payload.get('sub')
    except ExpiredSignatureError:
        raise TokenExpiredException
    except KeyError:
        raise InvalidTokenInformationException
    except JWTError:
        raise InvalidTokenException
    user = await UserDAO.get_by_id(int(user_id))
    return user


def permission_dependency(current_user: UserSchema = Depends(get_current_user)):
    check_permissions(current_user)
    return current_user

