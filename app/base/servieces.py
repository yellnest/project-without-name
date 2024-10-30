import functools
import re
from datetime import datetime, UTC

from asyncpg import UniqueViolationError, ForeignKeyViolationError, InvalidTextRepresentationError
from sqlalchemy.exc import IntegrityError, DBAPIError
from app.exeptions import SuccessRequest, ItemAlreadyExists, IncorrectForeignKey, InvalidText


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
            current_error = e.orig.__dict__.get('sqlstate')
            if current_error == UniqueViolationError.sqlstate:
                raise ItemAlreadyExists
            elif current_error == ForeignKeyViolationError.sqlstate:
                raise IncorrectForeignKey
            else:
                raise e
        except DBAPIError as e:
            current_error = e.orig.__dict__.get('sqlstate')
            if current_error == InvalidTextRepresentationError.sqlstate:
                raise InvalidText
            else:
                raise e
    return wrapper
