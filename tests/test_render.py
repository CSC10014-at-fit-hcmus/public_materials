"""Tests for the shared study planner render module."""

from datetime import date

from shared.contract import Block, Task
from shared.study_planner.render import render


def test_render_single_block():
    task = Task("Python Basics", 5, 3.0, date(2026, 10, 30))
    blocks = [Block(task, 2.5)]

    result = render(blocks)

    assert "Study Plan (2.5 h):" in result
    assert "1. Python Basics ... 2.5 h" in result
    assert "importance: 5" in result
    assert "deadline: 2026-10-30" in result
    assert "Summary:" not in result


def test_render_multiple_blocks():
    task1 = Task("Assignment 1", 4, 2.0, date(2026, 10, 25))
    task2 = Task("DS Exam", 5, 4.0, date(2026, 10, 28))
    blocks = [Block(task1, 2.0), Block(task2, 1.5)]

    result = render(blocks)

    assert "Study Plan (3.5 h):" in result
    assert "1. Assignment 1 ... 2.0 h" in result
    assert "2. DS Exam ... 1.5 h" in result


def test_render_empty_blocks():
    result = render([])

    assert result == "No study blocks scheduled."


def test_render_with_full_summary():
    task = Task("Read Tutorial", 3, 2.0, date(2026, 10, 29))
    blocks = [Block(task, 2.0)]
    summary = {
        "total_tasks": 1,
        "total_effort_h": 2.0,
        "allocated_hours": 2.0,
        "remaining_hours": 0.0,
        "completion_rate": 100.0,
        "overdue_tasks": [],
    }

    result = render(blocks, summary)

    assert "Study Plan (2.0 h):" in result
    assert "1. Read Tutorial ... 2.0 h" in result
    assert "Summary:" in result
    assert "Total Tasks: 1" in result
    assert "Total Effort: 2.0 h" in result
    assert "Allocated Hours: 2.0 h" in result
    assert "Remaining Hours: 0.0 h" in result
    assert "Completion Rate: 100.0%" in result
    assert "Overdue Tasks:" not in result


def test_render_with_overdue_tasks():
    task = Task("Late Project", 5, 4.0, date(2026, 10, 10))
    blocks = [Block(task, 1.0)]
    summary = {
        "total_tasks": 2,
        "total_effort_h": 6.0,
        "allocated_hours": 1.0,
        "remaining_hours": 5.0,
        "completion_rate": 16.67,
        "overdue_tasks": ["Late Project"],
    }

    result = render(blocks, summary)

    assert "Overdue Tasks: Late Project" in result
    assert "Remaining Hours: 5.0 h" in result


def test_render_empty_blocks_with_summary():
    summary = {
        "total_tasks": 1,
        "total_effort_h": 3.0,
        "allocated_hours": 0.0,
        "remaining_hours": 3.0,
        "completion_rate": 0.0,
        "overdue_tasks": ["Assignment 2"],
    }

    result = render([], summary)

    assert "No study blocks scheduled." in result
    assert "Summary:" in result
    assert "Total Tasks: 1" in result
    assert "Overdue Tasks: Assignment 2" in result
