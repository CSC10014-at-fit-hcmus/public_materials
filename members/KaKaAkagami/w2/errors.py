
"""Custom exceptions and feasibility checks for Week 2."""

from .models import Task


class InfeasiblePlan(Exception):
    """Raised when required study hours exceed available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        return (
            f"Infeasible plan: need {self.needed_h} hours, "
            f"but only {self.available_h} hours are available."
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan if tasks require too many hours."""
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
