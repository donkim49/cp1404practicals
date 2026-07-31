"""
CP1404 Practical
Hex colour code lookup using a dictionary
"""

COLOUR_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "black": "#000000",
    "blue": "#0000ff",
    "crimson": "#dc143c",
    "gold": "#ffd700",
    "green": "#008000",
    "hotpink": "#ff69b4",
    "orange": "#ffa500",
    "red": "#ff0000",
    "white": "#ffffff",
}

colour_name = input("Enter colour name (blank to stop): ")
while colour_name != "":
    try:
        print(f"{colour_name} has hex code {COLOUR_TO_HEX[colour_name.lower()]}")
    except KeyError:
        print(f"'{colour_name}' is not a known colour name")
    colour_name = input("Enter colour name (blank to stop): ")