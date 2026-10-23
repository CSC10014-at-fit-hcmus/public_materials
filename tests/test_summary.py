
"""Tests for the shared study planner summary module."""

from datetime import date, timedelta

import pytest

from shared.contract import Block, Task
from shared.study_planner.summary import summarise


def test_normal_summary():
    deadline = date.today() + timedelta(days=7)

    python = Task("Study Python", 5, 4.0, deadline)
    git = Task("Review Git", 3, 2.0, deadline)

    blocks = [
        Block(python, 3.0),
        Block(git, 2.0),
    ]

    result = summarise([python, git], blocks)

    assert result["total_tasks"] == 2
    assert result["total_effort_h"] == 6.0
    assert result["allocated_hours"] == 5.0
    assert result["remaining_hours"] == 1.0
    assert result["completion_rate"] == 83.33
    assert result["overdue_tasks"] == []


def test_empty_summary():
    result = summarise([], [])

    assert result["total_tasks"] == 0
    assert result["total_effort_h"] == 0.0
    assert result["allocated_hours"] == 0.0
    assert result["remaining_hours"] == 0.0
    assert result["completion_rate"] == 0.0
    assert result["overdue_tasks"] == []


def test_overdue_tasks():
    yesterday = date.today() - timedelta(days=1)
    tomorrow = date.today() + timedelta(days=1)

    late = Task("Late Assignment", 5, 3.0, yesterday)
    upcoming = Task("Upcoming Exam", 4, 2.0, tomorrow)

    result = summarise([late, upcoming], [])

    assert result["overdue_tasks"] == ["Late Assignment"]


def test_overallocation_is_capped():
    task = Task("Study Math", 4, 2.0, date.today())

    blocks = [
        Block(task, 3.0),
        Block(task, 1.0),
    ]

    result = summarise([task], blocks)

    assert result["allocated_hours"] == 4.0
    assert result["remaining_hours"] == 0.0
    assert result["completion_rate"] == 100.0


def test_zero_effort():
    task = Task("Quick Review", 2, 0.0, date.today())

    result = summarise([task], [])

    assert result["completion_rate"] == 0.0
    assert result["remaining_hours"] == 0.0


def test_negative_effort():
    task = Task("Invalid Task", 3, -2.0, date.today())

    with pytest.raises(ValueError):
        summarise([task], [])


def test_negative_block_hours():
    task = Task("Study Physics", 4, 3.0, date.today())

    with pytest.raises(ValueError):
        summarise([task], [Block(task, -1.0)])
