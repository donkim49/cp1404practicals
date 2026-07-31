"""
CP1404 Practical
State names in a dictionary
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                "WA": "Western Australia", "ACT": "Australian Capital Territory",
                "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

# Print all states and names neatly lined up
for code, name in CODE_TO_NAME.items():
    print(f"{code:<3} is {name}")

print()

state_code = input("Enter short state: ")
while state_code != "":
    try:
        print(state_code.upper(), "is", CODE_TO_NAME[state_code.upper()])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")