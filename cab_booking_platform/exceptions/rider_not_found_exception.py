class RiderNotFoundException(Exception):
    def __init__(self, message="Rider not found!") -> None:
        super().__init__(message)