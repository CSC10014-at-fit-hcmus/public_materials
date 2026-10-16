def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}
    for course, day in courses:
        result.setdefault(day, []).append(course)

    for day, courses_on_day in result.items():
        courses_on_day.sort()

    return result