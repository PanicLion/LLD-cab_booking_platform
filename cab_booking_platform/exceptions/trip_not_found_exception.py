class TripNotFoundException(Exception):
    def __init__(self, message="Trip not found!!") -> None:
        super().__init__(message)