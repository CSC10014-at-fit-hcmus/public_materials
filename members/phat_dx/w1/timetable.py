def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    grouped = {}
    for course, day in timetable:
        grouped.setdefault(day, []).append(course)
        
    for day in grouped:
        grouped[day].sort()
        
    return grouped