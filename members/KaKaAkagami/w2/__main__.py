
"""Run the Week 2 task package from the command line."""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load sample tasks and display their information."""
    sample_path = (
        Path(__file__).resolve().parents[3]
        / "samples"
        / "tasks.csv"
    )

    tasks = load_tasks(sample_path)

    print("Study Planner - Sample Tasks")
    print("----------------------------")

    for task in tasks:
        print(
            f"Title: {task.title} | "
            f"Importance: {task.importance} | "
            f"Effort: {task.effort_h}h | "
            f"Deadline: {task.deadline.isoformat()}"
        )


if __name__ == "__main__":
    main()
