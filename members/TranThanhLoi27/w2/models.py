import math
from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A single task with the data needed to plan it."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        # Title must be a non-empty string
        if not isinstance(self.title, str):
            raise TypeError("title must be a string")
        if not self.title.strip():
            raise ValueError("title must be a non-empty string")

        # Importance must be a whole number between 1 and 5
        if isinstance(self.importance, bool) or not isinstance(self.importance, int):
            raise TypeError("importance must be an integer")
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

        # Effort must be a finite, non-negative number of hours
        if isinstance(self.effort_h, bool) or not isinstance(
            self.effort_h, (int, float)
        ):
            raise TypeError("effort_h must be a number")
        if not math.isfinite(self.effort_h) or self.effort_h < 0:
            raise ValueError("effort_h must be a finite, non-negative number")

        # Deadline must be a date
        if not isinstance(self.deadline, date):
            raise TypeError("deadline must be a date")

    def days_left(self, today: date) -> int:
        # Calculate the remaining days
        delta = self.deadline - today
        # Return days left, or 0 if it is overdue
        return max(0, delta.days)
