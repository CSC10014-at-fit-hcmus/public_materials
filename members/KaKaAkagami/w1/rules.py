
def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check if a student is eligible to register for a thesis."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return reasons why a student is not eligible."""
    reasons = []

    if credits < 120:
        remaining = 120 - credits
        reasons.append(f"need {remaining} more credits")

    if gpa < 2.0:
        reasons.append("need GPA of at least 2.0")

    return reasons
