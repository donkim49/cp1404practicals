"""
CP1404/ Practical
My Guitars program - loads guitars from file, displays them sorted, accepts new guitars, saves.
"""

from guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Load guitars, display sorted, get new guitars from user, save all."""
    guitars = load_guitars(FILENAME)

    print("Guitars (unsorted):")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars (sorted by year):")
    display_guitars(guitars)

    add_new_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print(f"\n{len(guitars)} guitars saved to {FILENAME}.")


def load_guitars(filename):
    """Load and return a list of Guitar objects from a CSV file."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Print each guitar in the list."""
    for guitar in guitars:
        print(f"  {'(Vintage) ' if guitar.is_vintage() else ''}{guitar}")


def add_new_guitars(guitars):
    """Prompt user to enter new guitars and add them to the list."""
    print("\nEnter new guitars (leave name blank to stop):")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")


def save_guitars(filename, guitars):
    """Save all guitars to a CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


main()