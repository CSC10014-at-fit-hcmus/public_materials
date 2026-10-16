
def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and sort them alphabetically."""
    timetable = {}

    for course, day in entries:
        timetable.setdefault(day, []).append(course)

    for day in timetable:
        timetable[day].sort()

    return timetable
