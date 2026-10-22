def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("List cannot be empty")
        
    n = len(scores)
    sorted_scores = sorted(scores)
    
    mean_val = sum(scores) / n
    
    mid = n // 2
    if n % 2 == 0:
        median_val = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2.0
    else:
        median_val = sorted_scores[mid]
        
    return {
        "min": sorted_scores[0],
        "max": sorted_scores[-1],
        "mean": round(mean_val, 2),
        "median": round(median_val, 2)
    }