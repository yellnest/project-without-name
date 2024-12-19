import functools
import re
from datetime import datetime, UTC

from asyncpg import UniqueViolationError, ForeignKeyViolationError, InvalidTextRepresentationError
from sqlalchemy.exc import IntegrityError, DBAPIError
from app.exceptions import SuccessRequest, ItemAlreadyExistsException, IncorrectForeignKeyException, InvalidEnumException


def naive_utcnow():
    """Return (date time utc) without microseconds
    """
    return datetime.now(UTC).replace(tzinfo=None).strftime("%Y-%m-%d %H:%M:%S")


def generate_slug(title):
    """Return slug based on title, work only with latin letters
    """
    slug = re.sub(r'\W+', '-', title.lower())
    return slug


def handle_errors(func):
    """ Takes a func and checking for errors
    """

    @functools.wraps(func)
    async def wrapper(**kwargs):
        try:
            await func(**kwargs)
            raise SuccessRequest
        except IntegrityError as e:
            # match = re.search(r"Key \(email\)=\((.*?)\) already exists", str(e.orig))
            # conflicting_slug = match.group(1)
            current_error = e.orig.__dict__.get('sqlstate')
            if current_error == UniqueViolationError.sqlstate:
                """Если указано unique, и происходит попытка добавить существующие, то вызывается эта ошибка"""
                raise ItemAlreadyExistsException
            elif current_error == ForeignKeyViolationError.sqlstate:
                """Если указан несуществующий foreignKey"""
                raise IncorrectForeignKeyException
            else:
                raise e
        except DBAPIError as e:
            current_error = e.orig.__dict__.get('sqlstate')
            if current_error == InvalidTextRepresentationError.sqlstate:
                """Если указано несуществующие поле в enum"""
                raise InvalidEnumException
            else:
                raise e


    return wrapper
