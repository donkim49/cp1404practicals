"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    # Get user score and random score, then determine and print results.
    # User score
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(f"User score {score} is {result}")
    if result == "Excellent":
        print("You get a prize!")

    # Random score
    random_score = random.randint(0, 100)
    random_result = determine_score_result(random_score)
    print(f"Random: {random_score} = {random_result}")


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


main()