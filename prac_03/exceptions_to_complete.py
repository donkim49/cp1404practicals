"""
CP1404/CP5632 - Practical
Gets a valid integer from the user - does not crash on invalid input.
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True   # only reached if int() succeeded (no exception)
    except ValueError:
        print("Please enter a valid integer.")

print("Valid result is:", result)