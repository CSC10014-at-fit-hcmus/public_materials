from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self):
        # Check if importance is between 1 and 5
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        # Calculate the remaining days
        delta = self.deadline - today
        # Return days left, or 0 if it is overdue
        return max(0, delta.days)