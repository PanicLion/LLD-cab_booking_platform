import math


class Location:
    def __init__(self, x: float, y: float) -> None:
        self.longitude = x
        self.latitude = y

    
    def __str__(self) -> str:
        return f"Location(longitude={self.longitude}, latitude={self.latitude})"
    

    def calculate_distance(self, destination) -> float:
        return math.sqrt(
            (self.longitude - destination.longitude) ** 2 
            + (self.latitude - destination.latitude) ** 2
        )
    