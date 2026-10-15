def summary(scores : list[float]):
    if len(scores) == 0:
        return ValueError("Can't enter an empty list")

    max_val = scores[0]
    min_val = scores[0]
    sum = 0
    for val in scores:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        sum += val

    sorted_list = sorted(scores)

    mean = sum / len(scores)
    median = 0
    if len(scores) % 2 == 0:
        median = (scores[len(scores)//2] + scores[len(scores)//2-1]) / 2  
    else:
        median = scores[len(scores)//2]

    return {"min" :  min_val, "max" : max_val, "mean" : round(mean,2), "median" : round(median,2)}

print(summary([7.5, 9, 6, 8]))