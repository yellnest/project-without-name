from app.exceptions import UserAlreadyExists
from app.src.users.dao import UserDAO


async def email_already_exist(email: str):
    answer = await UserDAO.get_one_or_none(email=email)
    if answer:
        raise UserAlreadyExists
    return email

