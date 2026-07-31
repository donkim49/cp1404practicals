"""CP1404/CP5632 Practical - Client code using ProgrammingLanguage class."""
from programming_language import ProgrammingLanguage


def main():
    # Demonstrate use of ProgrammingLanguage class.
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()