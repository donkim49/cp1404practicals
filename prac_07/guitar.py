"""
CP1404/ Practical
Guitar class with comparison and helper methods.
"""

VINTAGE_YEAR_THRESHOLD = 1980


class Guitar:
    """Represent a guitar with a name, year, and cost."""

    def __init__(self, name, year, cost):
        """Construct a Guitar from the given values.

        name: str - name/model of the guitar
        year: int - year the guitar was made
        cost: float - cost of the guitar
        """
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __repr__(self):
        """Return developer-friendly representation of a Guitar."""
        return f"Guitar({self.name!r}, {self.year}, {self.cost})"

    def __lt__(self, other):
        """Compare guitars by year (oldest first)."""
        return self.year < other.year

    def is_vintage(self):
        """Return True if the guitar was made before 1980."""
        return self.year < VINTAGE_YEAR_THRESHOLD