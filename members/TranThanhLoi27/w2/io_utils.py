import csv
import json
from datetime import date
from pathlib import Path

from .models import Task

# Columns every CSV row must provide
REQUIRED_FIELDS = ("title", "importance", "effort_h", "deadline")


def load_tasks(path: str | Path) -> list[Task]:
    """
    Load and parse tasks from a CSV file.

    Args:
        path: File path to the CSV file.

    Returns:
        A list of Task objects instantiated from the CSV data.

    Raises:
        ValueError: If a row has invalid data types or missing expected fields.
    """
    tasks: list[Task] = []
    with open(path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        # Start at line 2 to account for the header row in CSV error reporting
        for line_num, row in enumerate(reader, start=2):
            try:
                # A row shorter than the header yields None for missing columns
                missing = [f for f in REQUIRED_FIELDS if row.get(f) is None]
                if missing:
                    raise ValueError(f"missing required field(s): {', '.join(missing)}")

                # Parse and cast fields to their expected data types
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
            except (ValueError, KeyError, TypeError) as e:
                # Include line number for easier debugging
                raise ValueError(f"Error at line {line_num}: {e}") from e
            tasks.append(task)
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """
    Serialize a list of Task objects into a formatted JSON file.

    Args:
        tasks: The list of Task objects to serialize.
        path: Destination file path for the JSON output.
    """
    data = []
    for task in tasks:
        # Convert each Task instance into a JSON-serializable dictionary
        data.append(
            {
                "title": task.title,
                "importance": task.importance,
                "effort_h": task.effort_h,
                "deadline": task.deadline.isoformat(),
            }
        )

    # Write the serialized data with 2-space indentation for readability
    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
