"""
CP1404/CP5632 - Practical
Program to determine the number of lines in a file.
Asks the user for filenames repeatedly until they press Enter.
Uses a function (SRP) and exception handling for missing files.
"""


def main():
    """Get filenames from user and print line counts until empty input."""
    filename = input("Enter filename: ")
    while filename != "":
        try:
            line_count = count_lines(filename)
            print(f"{filename} has {line_count} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        filename = input("Enter filename: ")


def count_lines(filename):
    """Count and return the number of lines in the given file."""
    with open(filename) as in_file:
        return len(in_file.readlines())


main()
