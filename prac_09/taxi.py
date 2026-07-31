"""
CP1404/ Practical
Taxi class - specialised version of Car with fare tracking.
"""
from car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    price_per_km = 1.23

    def __init__(self, name, fuel):
        """Initialise a Taxi instance based on parent class Car.

        name: string, reference name for taxi
        fuel: float, one unit of fuel drives one kilometre
        """
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance and price."""
        return (f"{super().__str__()}, {self.current_fare_distance}km on current fare, "
                f"${self.price_per_km:.2f}/km")

    def get_fare(self):
        """Return the fare for the current trip, rounded to nearest 10c."""
        return round(self.price_per_km * self.current_fare_distance, 1)

    def start_fare(self):
        """Begin a new fare by resetting current fare distance."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but also accumulate fare distance.

        distance: float, the requested distance to drive
        Returns the actual distance driven.
        """
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven