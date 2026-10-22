class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        # Store the needed and available hours
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self):
        # Define the error message to display
        return f"Need {self.needed_h} hours, but only have {self.available_h} hours."


def check_feasible(tasks: list, available_h: float):
    # Calculate the total needed hours for all tasks
    total_needed = sum(task.effort_h for task in tasks)

    # Raise an error if total needed hours exceed available hours
    if total_needed > available_h:
        raise InfeasiblePlan(total_needed, available_h)