def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits, gpa) -> list[str]:
    reasons = []
    if credits < 120:
        reasons.append(f"need {120 - credits} more credicts")

    if gpa < 2.0:
        reasons.append(f"need {2.0 - gpa} more gpa")
    return reasons