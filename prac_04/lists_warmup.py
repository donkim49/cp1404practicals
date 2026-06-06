"""
CP1404/CP5632 Practical
Lists warm-up exercises
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# What values do the following expressions have?
# numbers[0]      -> 3          (first element)
# numbers[-1]     -> 2          (last element)
# numbers[3]      -> 1          (element at index 3)
# numbers[:-1]    -> [3,1,4,1,5,9]  (all except last)
# numbers[3:4]    -> [1]        (slice from index 3 up to but not including 4)
# 5 in numbers    -> True       (5 is in the list)
# 7 in numbers    -> False      (7 is not in the list)
# "3" in numbers  -> False      (string "3" is not in the list, 3 int is)
# numbers + [6,5,3] -> [3,1,4,1,5,9,2,6,5,3]  (concatenation)

# Change the first element of numbers to "ten"
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all elements except the first two (slice)
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)