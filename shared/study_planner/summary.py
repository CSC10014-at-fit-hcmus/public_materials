
"""Summary statistics for the shared study planner."""

from datetime import date

from shared.contract import Block, Task


def summarise(tasks: list[Task], blocks: list[Block]) -> dict:
    """Summarise task effort, allocated hours, and overdue deadlines.

    completion_rate measures scheduled coverage, not actual work done.
    """
    if any(task.effort_h < 0 for task in tasks):
        raise ValueError("Task effort cannot be negative")

    if any(block.hours < 0 for block in blocks):
        raise ValueError("Allocated hours cannot be negative")

    total_effort = sum(task.effort_h for task in tasks)
    allocated_hours = sum(block.hours for block in blocks)

    covered_hours = 0.0

    for task in tasks:
        task_hours = sum(
            block.hours
            for block in blocks
            if block.task is task
        )
        covered_hours += min(task_hours, task.effort_h)

    remaining_hours = max(0.0, total_effort - covered_hours)

    completion_rate = (
        round(covered_hours / total_effort * 100, 2)
        if total_effort > 0
        else 0.0
    )

    today = date.today()
    overdue_tasks = [
        task.title
        for task in tasks
        if task.deadline < today
    ]

    return {
        "total_tasks": len(tasks),
        "total_effort_h": round(total_effort, 2),
        "allocated_hours": round(allocated_hours, 2),
        "remaining_hours": round(remaining_hours, 2),
        "completion_rate": completion_rate,
        "overdue_tasks": overdue_tasks,
    }
