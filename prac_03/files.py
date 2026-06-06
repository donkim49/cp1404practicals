"""
CP1404/CP5632 - Practical

"""

# 1. Ask user for name, write to name.txt using open/close
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2. Read name from name.txt and greet - using open/close and read()
in_file = open("name.txt", "r")
stored_name = in_file.read()
in_file.close()
print(f"Hi {stored_name}!")

# 3. Read only the first two numbers from numbers.txt and print their sum
# Uses readline() - reads one line at a time; with replaces open/close
with open("numbers.txt", "r") as in_file:
    first = int(in_file.readline())
    second = int(in_file.readline())
print(first + second)

# 4. Print total of ALL numbers in numbers.txt - works for any number of lines
# Uses 'for line in file' - the right tool when you need every line
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)