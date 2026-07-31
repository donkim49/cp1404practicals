"""
CP1404/ Practical
Taxi simulator program using Taxi and SilverServiceTaxi classes.
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Run the taxi simulator."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0.0

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").strip().lower()

        if choice == 'q':
            print(f"Total trip cost: ${bill:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break
        elif choice == 'c':
            chosen = choose_taxi(taxis)
            if chosen is not None:
                current_taxi = chosen
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill:.2f}")


def display_taxis(taxis):
    """Display all taxis with their index numbers.

    taxis: list of Taxi/SilverServiceTaxi objects
    """
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Prompt the user to choose a taxi from the list and return it.

    taxis: list of Taxi/SilverServiceTaxi objects
    Returns the chosen Taxi object, or None if invalid choice.
    """
    print("Taxis available: ")
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if choice < 0 or choice >= len(taxis):
            print("Invalid taxi choice")
            return None
        return taxis[choice]
    except ValueError:
        print("Invalid taxi choice")
        return None


def drive_taxi(taxi):
    """Prompt the user for a distance, drive the taxi and return the trip cost.

    taxi: Taxi or SilverServiceTaxi object
    Returns the fare for the trip as a float.
    """
    try:
        distance = float(input("Drive how far? "))
        taxi.start_fare()
        taxi.drive(distance)
        fare = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${fare:.2f}")
        return fare
    except ValueError:
        print("Invalid distance")
        return 0.0


main()