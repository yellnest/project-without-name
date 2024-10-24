from fastapi import APIRouter, Depends

from app.exeptions import SuccessRequest, NoSuchItem
from app.src.users.dao import UserDAO
from app.src.users.schemas import UserSchema, UserRegistrationSchema

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/all")
async def get_all_users() -> list[UserSchema]:
    return await UserDAO.get_all()


@router.get("/{user_id}")
async def get_user_by_id(user_id: int) -> UserSchema | None:
    return await UserDAO.get_by_id(user_id)


@router.post("/create-user")
async def create_user(user_data: UserRegistrationSchema):
    await UserDAO.add_item(user_name=user_data.user_name, user_password=user_data.user_password,
                           email=user_data.email, eng_lvl=user_data.eng_lvl)
    raise SuccessRequest


@router.delete("/{user_id}")
async def delete_user(user_id: int = Depends):
    item = await UserDAO.get_one_or_none(id=user_id)
    if item is None:
        raise NoSuchItem
    await UserDAO.delete_by_id(model_id=user_id)
    raise SuccessRequest

@router.patch("/{user_id}")
async def update_user(user_id: int, user_data: UserRegistrationSchema):
    await UserDAO.update_by_id(model_id=user_id, user_name=user_data.user_name, user_password=user_data.user_password,
                               email=user_data.email, eng_lvl=user_data.eng_lvl)
    raise SuccessRequest