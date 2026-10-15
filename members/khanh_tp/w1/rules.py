def can_register_thesis(credits: int, gpa: float):
    return credits >= 120 and gpa >= 2.0

def missing(credits, gpa):
    if can_register_thesis(credits, gpa):
        return []
    else:
        miss = []
        if credits < 120:
            miss.append(f"Need {120-credits} more credits")
        if gpa < 2.0:
            miss.append(f"GPA is missing {2.0-gpa}")

    return miss