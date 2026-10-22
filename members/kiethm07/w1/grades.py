def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError
    
    s = sorted(scores)
    n = len(s)
    
    mean = sum(s) / n
    if n % 2 == 1:
        median = s[n // 2]
    else:
        median = (s[n // 2 - 1] + s[n // 2]) / 2
        
    return {
        "min": s[0],
        "max": s[-1],
        "mean": round(mean, 2),
        "median": round(median, 2)
    }

print(summary([7.5, 9, 6, 8]))