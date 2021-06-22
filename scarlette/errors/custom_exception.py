class CustomException(Exception):
    def __init__(self, message: str) -> None:
        self.__message: str = message

        super().__init__(self.__message)

    @property
    def message(self) -> str:
        return self.message