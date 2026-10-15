def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    reasons = []
    
    if credits < 120:
        needed_credits = 120 - credits
        reasons.append(f"need {needed_credits} more credits")
        
    if gpa < 2.0:
        needed_gpa = round(2.0 - gpa, 2)
        reasons.append(f"need {needed_gpa} more GPA")
        
    return reasons


if __name__ == "__main__":
    print(can_register_thesis(120, 2.5))
    print(missing(120, 2.5))

    print(can_register_thesis(118, 2.5))
    print(missing(118, 2.5))

    print(can_register_thesis(115, 1.85))
    print(missing(115, 1.85))

    print(can_register_thesis(120, 2.0))
    print(missing(120, 2.0))

    print(can_register_thesis(120, 1.99))
    print(missing(120, 1.99))

    print(can_register_thesis(119.9, 2.0))
    print(missing(119.9, 2.0))