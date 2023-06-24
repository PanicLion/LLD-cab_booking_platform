import uuid
from enum import Enum
from rider import Rider
from location import Location
from cab import Cab


class TripStatus(Enum):
    IN_PROGRESS = 1
    FINISHED = 2


class Trip:
    def __init__(self, rider: Rider, cab: Cab, price: float, 
                 source: Location, destination: Location) -> None:
        self.id = uuid.uuid4()
        self.rider = rider
        self.cab = cab
        self.status: TripStatus = TripStatus.IN_PROGRESS
        self.price = price
        self.source = source
        self.destination = destination
    

    def end_trip(self):
        self.status = TripStatus.FINISHED
