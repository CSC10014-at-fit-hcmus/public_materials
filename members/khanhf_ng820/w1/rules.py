from __future__ import annotations


def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    reasons: list[str] = []
    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        diff_gpa = round(2.0 - gpa, 2)
        diff_str = int(diff_gpa) if diff_gpa.is_integer() else diff_gpa
        reasons.append(f"need {diff_str} higher GPA")
    return reasons
