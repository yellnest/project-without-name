from fastapi import APIRouter, Depends, Response

from app.base.servieces import handle_errors
from app.exceptions import SuccessRequest, NoSuchItemException
from app.src.users.auth import get_password_hash, authenticate_user, create_access_token
from app.src.users.dao import UserDAO
from app.src.users.dependencies import get_current_user
from app.src.users.schemas import UserSchema, UserRegistrationSchema, UserUpdateSchema, UserLoginSchema

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"],
)


@router.post("/register")
@handle_errors
async def register_user(user: UserRegistrationSchema):
    hashed_password = get_password_hash(user.user_password)
    await UserDAO.add_item(user_name=user.user_name, user_password=hashed_password, email=user.email)
    raise SuccessRequest

    # await email_already_exist(user.email)
    # print(user.email)
    # if user.user_password == user.repeat_password:
    #     print(user.user_password)
    # else:
    #     print('fadsfads')
    # await UserDAO.add_item(user_name=user.username, email=user.email, user_password=user.user_password,
    #                        eng_lvl=user.eng_lvl,)


@router.post("/login")
async def login_user(response: Response, user_data: UserLoginSchema):
    user = await authenticate_user(user_data.email, user_data.user_password)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)
    return access_token


@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('access_token')
    raise SuccessRequest


@router.get('/me')
async def read_users_me(current_user: UserSchema = Depends(get_current_user)) -> UserSchema:
    return current_user


@router.get("/all")
async def get_all_users() -> list[UserSchema]:
    return await UserDAO.get_all()


@router.get("/{user_id}")
async def get_user_by_id(user_id: int) -> UserSchema:
    user = await UserDAO.get_by_id(user_id)
    if user is None:
        raise NoSuchItemException
    return user


@router.post("/create-user")
@handle_errors
async def create_user(user_data: UserRegistrationSchema):
    await UserDAO.add_item(user_name=user_data.user_name, user_password=user_data.user_password, email=user_data.email)
    raise SuccessRequest


@router.delete("/{user_id}", dependencies=[Depends(get_user_by_id)])
async def delete_user(user_id: int):
    await UserDAO.delete_by_id(model_id=user_id)
    raise SuccessRequest


@router.patch("/{user_id}", dependencies=[Depends(get_user_by_id)])
@handle_errors
async def update_user(user_id: int, user_data: UserUpdateSchema):
    await UserDAO.update_by_id(model_id=user_id, user_name=user_data.user_name, email=user_data.email,
                               eng_lvl=user_data.eng_lvl)
    raise SuccessRequest
