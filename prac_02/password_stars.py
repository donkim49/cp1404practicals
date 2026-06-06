"""
CP1404/CP5632 - Practical
Password stars program with error checking
"""

MINIMUM_LENGTH = 8


def main():
    # Get valid password and print asterisks.
    password = get_password()
    print_asterisks(password)


def get_password():
    # Get password with minimum length validation.
    password = input(f"Enter password (minimum {MINIMUM_LENGTH} characters): ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password too short! Must be at least {MINIMUM_LENGTH} characters.")
        password = input(f"Enter password (minimum {MINIMUM_LENGTH} characters): ")
    return password


def print_asterisks(password):
    # Print asterisks equal to the length of the password.
    print("*" * len(password))


main()