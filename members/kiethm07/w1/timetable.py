def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}
    for course, day in schedule:
        result.setdefault(day, []).append(course)
    
    for courses in result.values():
        courses.sort()
        
    return result


if __name__ == "__main__":
    sample_data = [("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]
    print(by_day(sample_data))