"""
CP1404/ Practical
UnreliableCar class - a Car that only drives based on a reliability percentage.
"""
import random
from car import Car


class UnreliableCar(Car):
    """A Car that may or may not drive depending on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar based on parent Car.

        name: string, reference name for the car
        fuel: float, one unit of fuel drives one kilometre
        reliability: float, percentage chance (0-100) that the car will drive
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number falls within reliability range.

        distance: float, the requested distance to drive
        Returns the actual distance driven (0 if car fails to drive).
        """
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0