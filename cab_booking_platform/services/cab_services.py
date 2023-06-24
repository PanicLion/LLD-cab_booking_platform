from models.cab import Cab
from models.location import Location
from exceptions.cab_already_exists_exception import CabAlreadyExistsException
from exceptions.cab_not_found_exception import CabNotFoundException


class CabService:
    cabs: dict[str, Cab] = {}

    def create_cab(self, new_cab: Cab) -> None:
        if str(new_cab.id) in self.cabs:
            raise CabAlreadyExistsException
        self.cabs[str(new_cab.id)] = new_cab

    
    def get_cab(self, id: str) -> Cab:
        if id not in self.cabs:
            raise CabNotFoundException
        return self.cabs.get(id)
    

    def update_cab_location(self, id: str, new_location: Location) -> None:
        if id not in self.cabs:
            raise CabNotFoundException
        self.cabs.get(id).set_current_location(new_location)

    
    def update_cab_availability(self, id: str, is_available: bool) -> None:
        if id not in self.cabs:
            raise CabNotFoundException
        self.cabs.get(id).set_is_available(is_available)
    

    def get_cabs(self, source: Location, max_pickup_distance: float) -> list[Cab]:
        result: list[Cab] = []
        for cab in self.cabs.values:
            if (cab.get_is_available() 
                    and cab.get_current_location().calculate_distance(source) 
                    <= max_pickup_distance):
                result.append(cab)
        return result
    