import statistics

def summary(scores: list[float]) -> dict:
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
