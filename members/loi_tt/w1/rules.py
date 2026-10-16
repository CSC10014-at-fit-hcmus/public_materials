"""Check thesis registration requirements and report unmet requirements."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return whether both the credit and GPA thresholds are met.

    Compare credits with 120 and GPA with 2.0, then return True only when
    both comparisons succeed.
    """
    return credits >= 120 and gpa >= 2.0


def missing(credits, gpa) -> list[str]:
    """Return a message for each unmet thesis registration requirement.

    Start with an empty list, append the credit shortfall when credits are
    below 120, append the GPA shortfall when GPA is below 2.0, and return the
    collected messages.
    """
    reasons = []
    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")

    if gpa < 2.0:
        reasons.append(f"need {2.0 - gpa} more gpa")
    return reasons