"""
CP1404/ Practical
SilverServiceTaxi class - a fancy Taxi with flagfall and scaled price per km.
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A fancier Taxi with a flagfall charge and fanciness-scaled price per km."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi based on parent Taxi.

        name: string, reference name for taxi
        fuel: float, one unit of fuel drives one kilometre
        fanciness: float, multiplier applied to the base price per km
        """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the fare including flagfall, rounded to nearest 10c."""
        return round(super().get_fare() + self.flagfall, 1)

    def __str__(self):
        """Return a string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"