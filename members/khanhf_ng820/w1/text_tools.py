from __future__ import annotations


def word_count(text: str) -> dict[str, int]:
    cleaned = text.lower().translate(str.maketrans("", "", ".,!?;:"))
    words = cleaned.split()
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []

    counts = word_count(text)
    if not counts:
        return []

    sorted_pairs = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_pairs[:k]
