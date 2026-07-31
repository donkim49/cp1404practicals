"""CP1404/CP5632 Practical - Tests for Guitar class."""
from guitar import Guitar
import datetime

CURRENT_YEAR = datetime.datetime.now().year


def main():
    # Test Guitar class methods.
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 500.00)
    guitar3 = Guitar("50-year old guitar", CURRENT_YEAR - 50, 1000.00)

    # Test get_age()
    expected_age1 = CURRENT_YEAR - 1922
    print(f"Gibson L-5 CES get_age() - Expected {expected_age1}. Got {guitar1.get_age()}")

    expected_age2 = CURRENT_YEAR - 2013
    print(f"Another Guitar get_age() - Expected {expected_age2}. Got {guitar2.get_age()}")

    # Test is_vintage()
    print(f"Gibson L-5 CES is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"Another Guitar is_vintage() - Expected False. Got {guitar2.is_vintage()}")
    print(f"50-year old guitar is_vintage() - Expected True. Got {guitar3.is_vintage()}")


main()