from app.exceptions import NoPermissionException
from app.src.users.schemas import UserSchema


def check_permissions(current_user: UserSchema) -> None:
    """Проверка прав доступа для пользователя."""
    if not (current_user.is_admin or current_user.is_superuser):
        raise NoPermissionException
