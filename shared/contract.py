"""Shared contract for Team T-W2 / T-W3."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int  # 1-5
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        return max(0, (self.deadline - today).days)


@dataclass
class Block:
    task: Task
    hours: float
