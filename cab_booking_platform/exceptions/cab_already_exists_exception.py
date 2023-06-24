class CabAlreadyExistsException(Exception):
    def __init__(self, message="Cab already exists!") -> None:
        super().__init__(message)