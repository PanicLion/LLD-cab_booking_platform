import random
from cab_services import CabService
from rider_services import RiderService
from models.rider import Rider
from models.location import Location
from models.cab import Cab
from models.trip import Trip
from exceptions.no_cabs_available_exception import NoCabsAvailableException
from exceptions.trip_not_found_exception import TripNotFoundException


class TripService:
    MAX_PICKUP_DISTANCE = 10.0
    trips: dict[str, list[Trip]] = {}

    def __init__(self, cab_service: CabService, rider_service: RiderService) -> None:
        self.cab_service = cab_service
        self.rider_service = rider_service

    
    def create_trip(self, rider: Rider, source: Location, destination: Location) -> None:
        nearest_cabs: list[Cab] = self.cab_service.get_cabs(source, self.MAX_PICKUP_DISTANCE)

        nearest_available_cabs: list[Cab] = list(
            filter(
                lambda cab: cab.get_current_trip() == None, 
                nearest_cabs
            )
        )

        # TODO: Create a Cab Matching Strategy
        selected_cab: Cab = random.choice(nearest_available_cabs)

        if not selected_cab:
            raise NoCabsAvailableException

        # TODO: Create a Pricing Strategy
        price: float = source.calculate_distance(destination) * 10

        new_trip: Trip = Trip(rider, selected_cab, price, source, destination)
        
        if rider.get_id() not in self.trips:
            self.trips[rider.get_id()] = []
        self.trips.get(rider.get_id()).append(new_trip)
        selected_cab.set_current_trip(new_trip)


    def get_trip_history(self, rider: Rider) -> list[Trip]:
        return self.trips.get(rider.get_id())
    

    def end_trip(self, cab: Cab) -> None:
        if not cab.get_current_trip():
            raise TripNotFoundException
        cab.get_current_trip().end_trip()
        cab.set_current_trip(None)
    