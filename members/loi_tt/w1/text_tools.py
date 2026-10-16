"""Count words and select the most frequent words in a text."""


def word_count(text: str) -> dict:
    """Return a dictionary mapping normalized words to their counts.

    Lowercase the text, remove the listed punctuation, and split it on
    whitespace. Visit each resulting word and either initialize its count
    or increment the existing count, then return the completed dictionary.
    """
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
    """Return up to k words, ordered by frequency and then alphabetically.

    Get the word counts, convert them to word-count pairs, sort by descending
    count and ascending word, and return the first k pairs.
    """
    counts = word_count(text)
    items = list(counts.items())
    items.sort(key = lambda item: (-item[1], item[0]))
    return items[:k]