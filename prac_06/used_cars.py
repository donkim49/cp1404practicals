"""
CP1404/CP5632 Practical - Client code to use the Car class.

"""
from car import Car


def main():
    # Demo test code to show how to use car class.
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # Limo operations
    limo = Car("Limo", 100)       # Create limo with 100 units of fuel
    limo.add_fuel(20)              # Add 20 more units
    print(limo.fuel)               # Print the amount of fuel
    limo.drive(115)                # Attempt to drive 115 km
    print(limo)


main()