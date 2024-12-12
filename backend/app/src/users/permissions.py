from fastapi import Depends

from app.exceptions import NoPermissionException
from app.src.users.dependencies import get_current_user
from app.src.users.schemas import UserSchema


def check_admin_permission(current_user: UserSchema = Depends(get_current_user)) -> None:
    """Проверка прав доступа для пользователя."""
    if not (current_user.is_admin or current_user.is_superuser):
        raise NoPermissionException


def check_admin_or_owner_permission(resource_user_id: int = None, current_user: UserSchema = Depends(get_current_user)):
    if not (current_user.is_admin or current_user.is_superuser or current_user.id == resource_user_id):
        raise NoPermissionException
    return current_user
