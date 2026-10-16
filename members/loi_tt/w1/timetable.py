"""Group course names by their scheduled day."""


def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Return each day with its course names sorted alphabetically.

    Start with an empty mapping, add each course to the list for its day,
    sort every day's list, and return the mapping.
    """
    result = {}
    for course, day in courses:
        result.setdefault(day, []).append(course)

    for day, courses_on_day in result.items():
        courses_on_day.sort()

    return result 