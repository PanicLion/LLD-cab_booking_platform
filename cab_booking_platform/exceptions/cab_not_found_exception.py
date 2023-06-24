class CabNotFoundException(Exception):
    def __init__(self, message="Cab not found!") -> None:
        super().__init__(message)