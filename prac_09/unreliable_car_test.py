"""
CP1404/ Practical
Tests for the UnreliableCar class.
"""
from unreliable_car import UnreliableCar

NUM_ATTEMPTS = 1000
TOLERANCE = 0.15


def main():
    """Test UnreliableCar drive behaviour over many iterations."""

    # Test a 0% reliable car - should never drive
    never_car = UnreliableCar("Lemon", 999999, 0)
    for _ in range(NUM_ATTEMPTS):
        distance = never_car.drive(10)
        assert distance == 0, "0% reliable car should never drive"
    print("0% reliable car: PASSED - never drove")

    # Test a 100% reliable car - should always drive
    always_car = UnreliableCar("Trusty", 999999, 100)
    for _ in range(NUM_ATTEMPTS):
        distance = always_car.drive(10)
        assert distance == 10, "100% reliable car should always drive"
    print("100% reliable car: PASSED - always drove")

    # Test a 50% reliable car - should drive roughly half the time
    sometimes_car = UnreliableCar("Maybe", 999999, 50)
    drives = sum(1 for _ in range(NUM_ATTEMPTS) if sometimes_car.drive(10) > 0)
    ratio = drives / NUM_ATTEMPTS
    assert abs(ratio - 0.5) < TOLERANCE, f"50% car drove {ratio:.0%} of the time - outside tolerance"
    print(f"50% reliable car: PASSED - drove {ratio:.0%} of the time")


main()