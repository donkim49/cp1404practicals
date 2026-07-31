"""
CP1404/ Practical
Programming Language class with pointer_arithmetic field added.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values.

        name: str - name of the language
        typing: str - 'Dynamic' or 'Static'
        reflection: bool - whether the language supports reflection
        year: int - year the language first appeared
        pointer_arithmetic: bool - whether the language supports pointer arithmetic
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        """Provide string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"First appeared in {self.year}, Pointer Arithmetic={self.pointer_arithmetic}")

    def __repr__(self):
        """Provide developer-friendly representation of a ProgrammingLanguage."""
        return f"{vars(self)}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)
    cpp = ProgrammingLanguage("C++", "Static", False, 1983, True)

    print(python)
    print(repr(python))
    assert python.reflection is True
    assert python.is_dynamic() is True
    assert python.year == 1991
    assert python.pointer_arithmetic is False
    assert ruby.reflection is True
    assert visual_basic.is_dynamic() is False
    assert cpp.pointer_arithmetic is True
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()