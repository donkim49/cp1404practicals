"""
CP1404/CP5632 - Practical
Python's random module.
"""
import random

print(random.randint(5, 20))   # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))   # line 3

# Q: What did you see on line 1?
# A: 8,10,13
# Q: What was the smallest number you could have seen, what was the largest?
# A: Smallest: 5, Largest: 20

# Q: What did you see on line 2?
# A: 3,5,9
# Q: What was the smallest number you could have seen, what was the largest?
# A: Smallest: 3, Largest: 9
# Q: Could line 2 have produced a 4?
# A: No - randrange(3, 10, 2) produces values from {3, 5, 7, 9} (step of 2 starting at 3, all odd)

# Q: What did you see on line 3?
# A: 3.2924712713923716, 3.142243061225579, 4.435359633580119
# Q: What was the smallest number you could have seen, what was the largest?
# A: Smallest: 2.5, Largest: 5.5  (uniform includes both endpoints)

# Code to produce a random number between 1 and 100 inclusive
print(random.randint(1, 100))