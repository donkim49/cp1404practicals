"""
CP1404/ Practical
Band class - a Band has a list of Musician objects (association).
"""


class Band:
    """Represent a Band that contains a collection of Musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and an empty list of musicians.

        name: string, the name of the band
        """
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band and its musicians."""
        return f"{self.name} ({', '.join(str(m) for m in self.musicians)})"

    def add(self, musician):
        """Add a Musician to the band.

        musician: Musician object to add
        """
        self.musicians.append(musician)

    def play(self):
        """Return a string of each musician playing their instrument."""
        return '\n'.join(musician.play() for musician in self.musicians)