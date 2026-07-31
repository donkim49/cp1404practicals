"""
CP1404/ Practical
Tests for the SilverServiceTaxi class.
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi fare calculations."""

    # For an 18 km trip with fanciness of 2, fare should be $48.80 (rounded to 10c)
    taxi = SilverServiceTaxi("TestCab", 100, 2)
    taxi.drive(18)
    fare = taxi.get_fare()
    assert fare == 48.80, f"Expected $48.80, got ${fare:.2f}"
    print(f"18km trip with fanciness 2: ${fare:.2f} - PASSED")

    # Test that flagfall is applied on zero distance
    taxi2 = SilverServiceTaxi("EmptyRide", 100, 1)
    fare2 = taxi2.get_fare()
    assert fare2 == SilverServiceTaxi.flagfall, f"Expected flagfall only, got ${fare2:.2f}"
    print(f"Zero distance fare (flagfall only): ${fare2:.2f} - PASSED")

    # Test fanciness of 4 (Hummer-style)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    hummer.drive(61)
    fare3 = hummer.get_fare()
    print(f"61km trip with fanciness 4: ${fare3:.2f}")

    print(hummer)


main()