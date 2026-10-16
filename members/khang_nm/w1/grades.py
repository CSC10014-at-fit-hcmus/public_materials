
def summary(scores: list[float]) -> dict:
    """Return the min, max, mean, and median of a list of scores."""

    if not scores:
        raise ValueError("Scores list cannot be empty")

    n = len(scores)
    sorted_scores = sorted(scores)

    minimum = min(scores)
    maximum = max(scores)
    mean = round(sum(scores) / n, 2)

    mid = n // 2

    if n % 2 == 0:
        median = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
    else:
        median = sorted_scores[mid]

    return {
        "min": minimum,
        "max": maximum,
        "mean": mean,
        "median": round(median, 2)
    }
