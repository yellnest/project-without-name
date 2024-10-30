from fastapi import HTTPException, status


class BaseProjectException(HTTPException):
    status_code = 500
    detail = "Internal Server Error"

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class SuccessRequest(BaseProjectException):
    status_code = status.HTTP_200_OK
    detail = "Success request"


class NoSuchItem(BaseProjectException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Item not found"


class ItemAlreadyExists(BaseProjectException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Item already exists"


class IncorrectForeignKey(BaseProjectException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Incorrect Foreign Key"


class InvalidText(BaseProjectException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Invalid text"
