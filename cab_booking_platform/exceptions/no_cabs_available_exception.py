class NoCabsAvailableException(Exception):
    def __init__(self, message="No cabs available right now!") -> None:
        super().__init__(message)