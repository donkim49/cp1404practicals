"""CP1404/CP5632 Practical - ProgrammingLanguage class."""


class ProgrammingLanguage:
    # Represent a programming language with its key characteristics.

    def __init__(self, name, typing, reflection, year):

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        # Return a string representation of the programming language.
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")

    def is_dynamic(self):
        # Return True if the language is dynamically typed, False otherwise.
        return self.typing == "Dynamic"