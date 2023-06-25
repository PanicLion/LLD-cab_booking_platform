from controllers.cab_controllers import CabController
from controllers.rider_controllers import RiderController
from services.cab_services import CabService
from services.rider_services import RiderService
from services.trip_services import TripService


cab_service = CabService()
rider_service = RiderService()
trip_service = TripService(cab_service, rider_service)

cab_controller = CabController(cab_service, trip_service)
rider_controller = RiderController(rider_service, trip_service)

# Register few riders
r1 = rider_controller.register_rider("R1")
r2 = rider_controller.register_rider("R2")
r3 = rider_controller.register_rider("R3")

# Register few cabs
c1 = cab_controller.register_cab("D1", 1.0, 1.0)
c2 = cab_controller.register_cab("D2", 4.0, 4.0)
c3 = cab_controller.register_cab("D3", 100.0, 100.0)

# Book a cab
rider_controller.book_cab(r1.get_id(), 0.0, 0.0, 500.0, 500.0)
rider_controller.book_cab(r2.get_id(), 0.0, 0.0, 500.0, 500.0)

# End ride for a Cab
cab_controller.end_trip(c1.get_id())

# Update Cab's location
cab_controller.update_cab_location(c1.get_id(), 150.0, 150.0)

# Update the availability of a Cab
cab_controller.update_cab_availability(c1.get_id(), False)

# Fetch trip history for r1 and r2
print("Trip History of R1")
print([str(trip) for trip in rider_controller.bookings(r1.get_id())])

print("Trip History of R2")
print([str(trip) for trip in rider_controller.bookings(r2.get_id())])

