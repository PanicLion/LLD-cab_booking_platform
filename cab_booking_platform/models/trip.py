import uuid
from enum import Enum
from models.rider import Rider
from models.location import Location
# import models.cab  // Error because of circular import


class TripStatus(Enum):
    IN_PROGRESS = 1
    FINISHED = 2


class Trip:
    def __init__(self, rider: Rider, cab, price: float, 
                 source: Location, destination: Location) -> None:
        self.id = uuid.uuid4()
        self.rider = rider
        self.cab = cab
        self.status: TripStatus = TripStatus.IN_PROGRESS
        self.price = price
        self.source = source
        self.destination = destination
    

    def __str__(self) -> str:
        return f"Trip(id={self.id}, rider={self.rider}, cab={self.cab}, \
                status={self.status}, price={self.price}, \
                source={self.source}, destination={self.destination} \
                )"


    def end_trip(self):
        self.status = TripStatus.FINISHED
