from .custom_exception import CustomException


class ConfigFigleNotFound(CustomException):
    def __init__(self, message: str) -> None:
        super().__init__(message)