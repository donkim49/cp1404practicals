"""
CP1404/ Practical
Test/client code for the Taxi class.
"""
from taxi import Taxi


def main():
    """Demonstrate Taxi functionality."""
    # Create a new taxi with name "Prius 1" and 100 units of fuel
    my_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40 km
    my_taxi.drive(40)

    # Print taxi details and current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Restart the meter and drive 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # Print details and current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


main()