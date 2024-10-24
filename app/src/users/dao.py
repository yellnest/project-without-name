from app.dao.base_dao import BaseDao
from app.src.users.models import Users


class UserDAO(BaseDao):
    model = Users
