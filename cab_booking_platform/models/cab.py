import uuid
from models.location import Location
from models.trip import Trip


class Cab:
    def __init__(self, driver_name: str, location: Location) -> None:
        self.id = uuid.uuid4()
        self.driver_name = driver_name
        self.is_available: bool = True
        self.current_location = location
        self.current_trip = None


    def __str__(self) -> str:
        return f"Cab( \
                id={str(self.id)}, \
                driver={self.driver_name}, \
                is_available={self.is_available} \
                )"
    

    def get_id(self) -> str:
        return str(self.id)


    def set_is_available(self, is_available: bool):
        self.is_available = is_available
    

    def get_is_available(self) -> bool:
        return self.is_available


    def set_current_location(self, location: Location):
        self.current_location = location


    def get_current_location(self) -> Location:
        return self.current_location
    

    def get_current_trip(self) -> Trip:
        return self.current_trip


    def set_current_trip(self, new_trip: Trip) -> None:
        self.current_trip = new_trip
