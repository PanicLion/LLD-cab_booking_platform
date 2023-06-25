from services.rider_services import RiderService
from services.trip_services import TripService
from models.rider import Rider
from models.location import Location
from models.trip import Trip


class RiderController:
    def __init__(self, rider_service: RiderService, trip_service: TripService) -> None:
        self.rider_service = rider_service
        self.trip_service = trip_service

    
    def register_rider(self, rider_name: str):
        new_rider: Rider = Rider(rider_name)
        self.rider_service.create_rider(new_rider)
        return new_rider

    
    def book_cab(self, rider_id: str, source_x: float, 
                 source_y: float, dest_x: float, dest_y: float):
        self.trip_service.create_trip(
            self.rider_service.get_rider(rider_id),
            Location(source_x, source_y),
            Location(dest_x, dest_y)
        )
    

    def bookings(self, rider_id: str) -> list[Trip]:
        bookings: list[Trip] = self.trip_service.get_trip_history(
            self.rider_service.get_rider(rider_id)
        )
        return bookings
