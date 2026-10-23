
"""Task model for Week 2 exercises."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate task importance."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be between 1 and 5")

    def days_left(self, today: date) -> int:
        """Return remaining days until the deadline, minimum zero."""
        return max(0, (self.deadline - today).days)
