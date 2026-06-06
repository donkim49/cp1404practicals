"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    # Program to load and display subject data from file.
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename=FILENAME):
    """Read subject data from file and return as a list of lists.

    Each inner list contains: [subject_code (str), lecturer (str), num_students (int)]
    """
    subjects = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        subject = [parts[0], parts[1], int(parts[2])]
        subjects.append(subject)
    input_file.close()
    return subjects


def display_subjects(subjects):
    # Display all subject details in a formatted layout.
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:<15} and has {subject[2]:>3} students")


main()