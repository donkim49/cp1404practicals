"""
CP1404/CP5632 - Practical
Score menu program with multiple options
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    # Score menu program.
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell!")


def get_valid_score():
    # Get a valid score between 0 and 100 inclusive.
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score


def determine_score_result(score):
    # Determine the result based on score value.
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    # Print stars equal to the score value.
    print("*" * int(score))


main()