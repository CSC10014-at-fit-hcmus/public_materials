def word_count(text: str) -> dict[str, int]:
    for char in ".,!?;:":
        text = text.replace(char, " ")
    
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
        
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:k]

if __name__ == "__main__":
    text = "Git is fun. Git is fast!"
    print(word_count(text))
    print(top_k(text, 2))