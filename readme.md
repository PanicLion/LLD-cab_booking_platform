
# LLD - Cab Booking Platform

### Problem Statement:

We want to build a cab booking platform to allow a rider to book a cab.

### Details:

- The location is represented as a (x, y) coordinate.
- Distance between two points (x1, y1) and(x2, y2) is sqrt((x1-x2)^2 + (y1-y2)^2)
- Platform has decided upon maximum distance a driver has to travel to pickup a rider.
- A cab has only 1 driver.
- Sharing of cab is not allowed between riders
- There is a single type of cab

### Please build an application that exposes following features to riders and drivers.

- Register a rider.
- Register a driver/cab
- Update a cab’s location
- A driver can switch on/off his availability
- A rider can book a cab
- Fetch history of all rides taken by a rider.
- End the Trip

## Test

```
git clone https://github.com/PanicLion/LLD-cab_booking_platform.git

<!-- run the below command only if design branch hasn't merged with master -->
git checkout design

cd cab_booking_platform

python main.py
```