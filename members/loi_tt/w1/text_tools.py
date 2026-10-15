def word_count(text: str) -> dict:
    text = text.lower()
    text = text.translate(text.maketrans("", "", ".,!;:"))
    words = text.split()
    counts = {}
    for word in words:
        if word not in counts :
            counts[word] = 1
        else: counts[word] += 1
    return counts

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    items = list(counts.items())
    items.sort(key = lambda item: (-item[1], item[0]))
    return items[:k]

print(word_count("Git is fun. Git is fast!"))
print(top_k("Git is fun. Git is fast!", 2))