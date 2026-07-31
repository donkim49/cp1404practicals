"""
Wimbledon Champions
Estimate: 20 minutes
Actual:   20 minutes

Reads wimbledon.csv and displays:
- Champions and how many times they have won
- Countries of the champions in alphabetical order
"""

FILENAME = "wimbledon.csv"


def read_data(filename):
    """Read the CSV file and return a list of lists (rows of data)."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header line
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
    return data


def get_champion_wins(data):
    """Return a dictionary mapping champion name to win count."""
    champion_to_wins = {}
    for row in data:
        champion = row[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def get_champion_countries(data):
    """Return a set of countries that have produced a Wimbledon champion."""
    countries = set()
    for row in data:
        countries.add(row[1])
    return countries


def main():
    data = read_data(FILENAME)

    champion_to_wins = get_champion_wins(data)
    print("Wimbledon Champions: ")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")

    countries = get_champion_countries(data)
    sorted_countries = sorted(countries)
    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon: ")
    print(", ".join(sorted_countries))


main()