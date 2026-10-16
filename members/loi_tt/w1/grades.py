"""Calculate summary statistics for a list of grades."""

import statistics


def summary(scores: list[float]) -> dict:
    """Return the minimum, maximum, mean, and median of the grades.

    Reject an empty list first, then calculate the minimum and maximum.
    Use the statistics module for the mean and median, rounding both to two
    decimal places, and collect all four values in the returned dictionary.
    """
    if not scores:
        raise ValueError("Danh sach diem khong duoc de trong")
    
    minn = min(scores)
    maxx = max(scores)
    mean = round(statistics.mean(scores), 2)
    median = round(statistics.median(scores), 2)
    return {
        "min": minn, 
        "max": maxx,
        "mean": mean,
        "median": median
    }
