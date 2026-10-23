from .models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float) -> None:
        # Keep the arguments on the exception for logging/debugging
        super().__init__(needed_h, available_h)
        # Store the needed and available hours
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self) -> str:
        # Define the error message to display
        return f"Need {self.needed_h} hours, but only have {self.available_h} hours."


def check_feasible(tasks: list[Task], available_h: float) -> None:
    # Calculate the total needed hours for all tasks
    total_needed = sum(task.effort_h for task in tasks)

    # Raise an error if total needed hours exceed available hours
    if total_needed > available_h:
        raise InfeasiblePlan(total_needed, available_h)
