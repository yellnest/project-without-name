from symtable import Class

from fastapi import HTTPException, status


class BaseProjectException(HTTPException):
    status_code = 500
    detail = "Internal Server Error"

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class SuccessRequest(BaseProjectException):
    status_code = status.HTTP_200_OK
    detail = "Success request"


class NoSuchItemException(BaseProjectException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Item not found"


class ItemAlreadyExistsException(BaseProjectException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Item already exists"


class IncorrectForeignKeyException(BaseProjectException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Incorrect Foreign Key"


class InvalidEnumException(BaseProjectException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Invalid enum choices"


class UserAlreadyExistsException(BaseProjectException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User with email already exists"


class PasswordsDoNotMatchException(BaseProjectException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Passwords do not match"


class IncorrectEmailException(BaseProjectException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверная почта"


class IncorrectPasswordException(BaseProjectException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный пароль"


class TokenIsNotExistException(BaseProjectException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"


class WrongTokenFormatException(BaseProjectException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"


class TokenExpiredException(BaseProjectException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Время жизни токена кончилось"


class InvalidTokenException(BaseProjectException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Невалидный токен"


class InvalidTokenInformationException(BaseProjectException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token does not contain user id or sub"


class NoPermissionException(BaseProjectException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "У вас нет доступа"
