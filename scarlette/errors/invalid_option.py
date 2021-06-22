from .custom_exception import CustomException


class InvalidOption(CustomException):
    def __init__(self, message: str) -> None:
        super().__init__(message)