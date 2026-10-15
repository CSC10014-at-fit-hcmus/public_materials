def by_day(vec : list[tuple[str, str]]):
    grouped = {}

    for course in vec:
        grouped.setdefault(course[1], []).append(course[0])

    return grouped

print(by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]))