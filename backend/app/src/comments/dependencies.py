from fastapi import Depends
from app.exceptions import NoSuchItemException
from app.src.comments.dao import CommentDao
from app.src.comments.schema import CommentSchema
from app.src.users.dependencies import get_current_user
from app.src.users.permissions import check_admin_permission
from app.src.users.schemas import UserSchema


async def get_comment_by_id(comment_id: int):
    comm = await CommentDao.get_comment_by_id(comment_id)
    if comm is None:
        raise NoSuchItemException
    return comm


def admin_or_owner(comment: CommentSchema = Depends(get_comment_by_id), current_user: UserSchema = Depends(get_current_user)):
    if comment.user_id == current_user.id:
        return current_user
    check_admin_permission(current_user)
    return current_user

