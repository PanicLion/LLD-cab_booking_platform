class RiderAlreadyExistsException(Exception):
    def __init__(self, message="Rider already exists!") -> None:
        super().__init__(message)