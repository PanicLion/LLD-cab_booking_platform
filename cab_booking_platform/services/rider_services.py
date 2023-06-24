from models.rider import Rider
from exceptions.rider_already_exists_exception import RiderAlreadyExistsException
from exceptions.rider_not_found_exception import RiderNotFoundException


class RiderService:
    riders: dict[str, Rider] = {}

    def create_rider(self, new_rider: Rider):
        if str(new_rider.id) in self.riders:
            raise RiderAlreadyExistsException
        self.riders[str(new_rider.id)] = new_rider

    
    def get_rider(self, id: str):
        if id not in self.riders:
            raise RiderNotFoundException
        return self.riders.get(id)
    