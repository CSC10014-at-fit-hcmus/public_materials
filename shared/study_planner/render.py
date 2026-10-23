"""Text rendering for the shared study planner."""

from shared.contract import Block


def render(blocks: list[Block], summary: dict | None = None) -> str:
    """Render study blocks and optional summary statistics into a readable plan.

    Args:
        blocks: List of allocated study blocks.
        summary: Optional summary statistics dictionary.

    Returns:
        A formatted multi-line text plan.
    """
    lines: list[str] = []

    if not blocks:
        lines.append("No study blocks scheduled.")
    else:
        total_hours = sum(block.hours for block in blocks)
        lines.append(f"Study Plan ({total_hours:.1f} h):")
        for idx, block in enumerate(blocks, start=1):
            title = block.task.title
            hours = block.hours
            deadline = block.task.deadline.isoformat()
            importance = block.task.importance
            lines.append(
                f"  {idx}. {title} ... {hours:.1f} h "
                f"(importance: {importance}, deadline: {deadline})"
            )

    if summary:
        lines.append("")
        lines.append("Summary:")
        if "total_tasks" in summary:
            lines.append(f"  - Total Tasks: {summary['total_tasks']}")
        if "total_effort_h" in summary:
            lines.append(f"  - Total Effort: {summary['total_effort_h']:.1f} h")
        if "allocated_hours" in summary:
            lines.append(f"  - Allocated Hours: {summary['allocated_hours']:.1f} h")
        if "remaining_hours" in summary:
            lines.append(f"  - Remaining Hours: {summary['remaining_hours']:.1f} h")
        if "completion_rate" in summary:
            lines.append(f"  - Completion Rate: {summary['completion_rate']:.1f}%")
        if summary.get("overdue_tasks"):
            overdue_str = ", ".join(summary["overdue_tasks"])
            lines.append(f"  - Overdue Tasks: {overdue_str}")

    return "\n".join(lines)
