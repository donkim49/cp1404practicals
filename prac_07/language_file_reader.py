"""
CP1404/ Practical
File and class example - opens/reads a file, stores in objects of custom class.
"""

import csv
from collections import namedtuple

from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = load_languages('languages.csv')
    for language in languages:
        print(language)


def load_languages(filename):
    """Load programming languages from a CSV file and return a list of ProgrammingLanguage objects."""
    languages = []
    in_file = open(filename, 'r')
    in_file.readline()  # skip header line
    for line in in_file:
        parts = line.strip().split(',')
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[4] == "Yes"
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
        languages.append(language)
    in_file.close()
    return languages


main()