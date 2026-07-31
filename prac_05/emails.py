"""
Emails
Estimate: 25 minutes
Actual:   22 minutes

Stores users' emails (keys) and names (values) in a dictionary.
Extracts a suggested name from the email address and confirms with the user.
"""


def extract_name(email):
    """Extract and return a title-cased name from an email address."""
    local_part = email.split("@")[0]
    parts = local_part.split(".")
    # Only use parts that look like name parts (filter out numbers-only parts)
    name_parts = [part for part in parts if not part.isdigit()]
    return " ".join(name_parts).title()


def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        suggested_name = extract_name(email)
        response = input(f"Is your name {suggested_name}? (Y/n) ")
        if response == "" or response.lower() == "y":
            name = suggested_name
        else:
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()