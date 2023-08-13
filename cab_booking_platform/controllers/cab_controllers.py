from services.cab_services import CabService
from services.trip_services import TripService
from models.location import Location
from models.cab import Cab


class CabController:
    def __init__(self, cab_service: CabService, trip_service: TripService) -> None:
        self.cab_service = cab_service
        self.trip_service = trip_service

    
    def register_cab(self, driver_name: str, x: float, y: float):
        current_location: Location = Location(x, y)
        new_cab: Cab = Cab(driver_name, current_location)
        self.cab_service.create_cab(new_cab)
        return new_cab


    def update_cab_location(self, cab_id: str, new_x: float, new_y: float):
        new_location: Location = Location(new_x, new_y)
        self.cab_service.update_cab_location(cab_id, new_location)

    
    def update_cab_availability(self, cab_id: str, is_available: bool):
        self.cab_service.update_cab_availability(cab_id, is_available)

    
    def end_trip(self, cab_id: str):
        cab: Cab = self.cab_service.get_cab(cab_id)
        self.trip_service.end_trip(cab)
