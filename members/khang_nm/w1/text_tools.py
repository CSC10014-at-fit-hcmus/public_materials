
def word_count(text: str) -> dict[str, int]:
    """Count words ignoring case and basic punctuation."""
    counts = {}

    text = text.lower()

    for char in ".,!?;:":
        text = text.replace(char, " ")

    words = text.split()

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the k most frequent words, sorted by count and name."""
    if k <= 0:
        return []

    counts = word_count(text)

    sorted_words = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    return sorted_words[:k]
