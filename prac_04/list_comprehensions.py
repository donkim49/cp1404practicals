"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# join string method to create a single sorted string of names
print(" ".join(sorted(names)))

# TODO: list comprehension to create a list of all the full_names in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']

# TODO: list comprehension to create a list of integers from the above list of strings
numbers = [int(x) for x in almost_numbers]
print(numbers)

# TODO: list comprehension to create a list of only the numbers greater than 9
big_numbers = [x for x in numbers if x > 9]
print(big_numbers)

# TODO: (more advanced) string of last names for full names longer than 11 characters
# Result should be: 'Harlem, Hendrix, Lovelace'
long_name_lastnames = ", ".join([name.split()[1] for name in full_names if len(name) > 11])
print(long_name_lastnames)