
"""CSV and JSON utilities for Week 2 tasks."""

import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from CSV and report invalid rows with line numbers."""
    tasks = []

    with Path(path).open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for line_number, row in enumerate(reader, start=2):
            try:
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
                tasks.append(task)

            except (ValueError, KeyError, TypeError) as exc:
                raise ValueError(
                    f"Invalid task on line {line_number}: {exc}"
                ) from exc

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save tasks as JSON with ISO-formatted deadlines."""
    data = []

    for task in tasks:
        item = asdict(task)
        item["deadline"] = task.deadline.isoformat()
        data.append(item)

    Path(path).write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
