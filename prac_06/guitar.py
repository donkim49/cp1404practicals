"""CP1404/CP5632 Practical - Guitar class."""
import datetime


class Guitar:
    # Represent a guitar with name, year and cost.

    def __init__(self, name="", year=0, cost=0):

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        # Return a string representation of the guitar.
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        # Return the age of the guitar in years.
        return datetime.datetime.now().year - self.year

    def is_vintage(self):
        # Return True if the guitar is 50 or more years old, False otherwise.
        return self.get_age() >= 50