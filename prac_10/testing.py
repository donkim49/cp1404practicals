"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.

    >>> repeat_string("Python", 1)
    'Python'
    >>> repeat_string("hi", 2)
    'hi hi'
    >>> repeat_string("yo", 3)
    'yo yo yo'
    """
    # TODO: 1. Fixed: join copies of s with spaces instead of plain repetition
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in.

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    # TODO: 4. Fixed: changed > to >= so words equal to length return True
    return len(word) >= length


def make_sentence(phrase):
    """Format a phrase as a sentence: capitalised and ending with a single full stop.

    >>> make_sentence("hello")
    'Hello.'
    >>> make_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> make_sentence("the quick brown fox")
    'The quick brown fox.'
    """
    phrase = phrase.strip().capitalize()
    if not phrase.endswith("."):
        phrase += "."
    return phrase


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message
    assert repeat_string("Python", 1) == "Python"
    # TODO: 1. fixed repeat_string so this now passes
    assert repeat_string("hi", 2) == "hi hi"

    # assert test for Car odometer default
    car = Car()
    assert car.odometer == 0, "Car does not set odometer correctly"

    # TODO: 2. assert statements for Car fuel
    car_default = Car()
    assert car_default.fuel == 0, "Car does not set default fuel correctly"
    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Car does not set fuel correctly when passed in"

    print("All assert tests passed.")


run_tests()

# TODO: 3. Uncomment the following line to run doctests
doctest.testmod()