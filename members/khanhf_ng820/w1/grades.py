from __future__ import annotations


def summary(scores: list[float]) -> dict[str, float]:
    if not scores:
        raise ValueError("scores list cannot be empty")

    sorted_scores = sorted(scores)
    n = len(sorted_scores)

    min_val = min(sorted_scores)
    max_val = max(sorted_scores)
    mean_val = round(sum(sorted_scores) / n, 2)

    if n % 2 == 1:
        med_val = sorted_scores[n // 2]
    else:
        med_val = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

    return {
        "min": min_val,
        "max": max_val,
        "mean": mean_val,
        "median": round(med_val, 2),
    }
