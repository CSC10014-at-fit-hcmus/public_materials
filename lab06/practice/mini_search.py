"""Lab 6 warm-up: build a tiny search engine with the data structures you already know.

No AI here — just dictionaries, sets and sorting (DSA!). Run the tests:  pytest -q test_mini_search.py
"""
import re

DOCS = {
    "D1": "Students may register a thesis with at least 120 credits and a GPA of 2.0.",
    "D2": "Retake credits are charged at 1.5 times the normal credit rate.",
    "D3": "A lost student card can be replaced at Student Affairs in room I.102.",
    "D4": "Students may borrow up to 5 books from the library for 14 days.",
}
STOP = {"a", "an", "the", "at", "of", "for", "to", "in", "can", "be", "is", "my", "i", "may", "with", "and", "up", "from"}


def tokenize(text: str) -> list[str]:
    """'Lost my card!' -> ['lost', 'card']  (lower-case words, stop words removed) — given."""
    return [w for w in re.findall(r"\w+", text.lower()) if w not in STOP]


def build_index(docs: dict[str, str]) -> dict[str, set[str]]:
    """Inverted index: word -> set of document ids that contain it.

    Example: {"thesis": {"D1"}, "credits": {"D1", "D2"}, ...}
    """
    index: dict[str, set[str]] = {}
    # TODO S1: for each (doc_id, text) in docs.items(), for each word in tokenize(text):
    #          index.setdefault(word, set()).add(doc_id)
    return index


def search(index: dict[str, set[str]], query: str, k: int = 2) -> list[tuple[str, int]]:
    """Score = number of query words found in the document. Return the top k (doc_id, score),
    highest score first; ties broken by doc_id. Documents with score 0 are not returned."""
    scores: dict[str, int] = {}
    # TODO S2: for each word in tokenize(query): for each doc_id in index.get(word, set()): scores[doc_id] += 1
    # TODO S3: sort by (-score, doc_id) and return the first k
    return []
