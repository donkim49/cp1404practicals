"""
CP1404/ Practical
Project Management Program - load, save, display, filter, add, and update projects.
Estimated time: 2 hours
Actual time: TODO
"""

import datetime
from project import Project

DEFAULT_FILENAME = 'projects.txt'
DATE_FORMAT = '%d/%m/%Y'
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """Run the project management program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    choice = get_menu_choice()
    while choice != 'q':
        if choice == 'l':
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        choice = get_menu_choice()

    offer_save(projects)
    print("Thank you for using custom-built project management software.")


def get_menu_choice():
    """Display the menu and return a valid lowercase menu choice."""
    print(MENU)
    return input(">>> ").lower()


def load_projects(filename):
    """Load and return a list of Project objects from a tab-separated file."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split('\t')
            start_date = datetime.datetime.strptime(parts[1], DATE_FORMAT).date()
            project = Project(parts[0], start_date, parts[2], parts[3], parts[4])
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save all projects to a tab-separated file."""
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(
                f"{project.name}\t{project.start_date.strftime(DATE_FORMAT)}\t"
                f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n"
            )


def display_projects(projects):
    """Display incomplete projects then completed projects, each sorted by priority."""
    incomplete = sorted(p for p in projects if not p.is_complete())
    completed = sorted(p for p in projects if p.is_complete())
    print("Incomplete projects: ")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects: ")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Display projects that start on or after a user-entered date, sorted by date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, DATE_FORMAT).date()
    filtered = sorted(
        (p for p in projects if p.start_date >= filter_date),
        key=lambda p: p.start_date
    )
    for project in filtered:
        print(project)


def add_project(projects):
    """Prompt user for project details and add a new Project to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input(f"Start date ({DATE_FORMAT[1:]}): ")
    start_date = datetime.datetime.strptime(date_string, DATE_FORMAT).date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """Display all projects, let user choose one, then update its completion and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    index = int(input("Project choice: "))
    project = projects[index]
    print(project)

    new_percentage = input("New Percentage: ")
    if new_percentage:
        project.completion_percentage = int(new_percentage)

    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)


def offer_save(projects):
    """Ask the user if they want to save to the default file before quitting."""
    response = input(f"Would you like to save to {DEFAULT_FILENAME}? ").lower()
    if response in ('yes', 'y'):
        save_projects(DEFAULT_FILENAME, projects)
        print(f"Projects saved to {DEFAULT_FILENAME}.")


main()