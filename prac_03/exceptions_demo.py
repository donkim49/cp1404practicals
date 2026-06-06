"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   A ValueError will occur when the user enters something that cannot be
   converted to an integer by int(), e.g. typing "World" or "7.5"

2. When will a ZeroDivisionError occur?
   A ZeroDivisionError will occur when the user enters 0 for the denominator,
   since dividing any number by zero is undefined.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   Yes by adding a check so that if the denominator is 0, we do not attempt
   the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # Fix for Q3: check for zero before dividing to avoid ZeroDivisionError
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")