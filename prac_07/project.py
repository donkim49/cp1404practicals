"""
CP1404/ Practical
Project class for project management.
"""


class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project from the given values.

        name: str - project name
        start_date: datetime.date - project start date
        priority: int - priority number (lower = higher priority)
        cost_estimate: float - estimated cost in dollars
        completion_percentage: int - percentage complete (0-100)
        """
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return human-readable string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __repr__(self):
        """Return developer-friendly representation of a Project."""
        return f"{vars(self)}"

    def __lt__(self, other):
        """Compare projects by priority (lower number = higher priority, sorts first)."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is 100% complete."""
        return self.completion_percentage == 100