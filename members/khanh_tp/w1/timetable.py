def by_day(vec : list[tuple[str, str]]):
    grouped = {}

    for course in vec:
        grouped.setdefault(course[1], []).append(course[0])

    for list in grouped.values():
        list.sort()

    return grouped