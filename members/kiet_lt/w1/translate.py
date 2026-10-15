def transpose(matrix: list[list[int | float]]) -> list[list[int | float]]:
    """
    Transposes a 2D matrix (list of lists).

    Difference from C++:
    In C++, transposing a std::vector<std::vector<T>> typically requires pre-allocating
    the result matrix with reversed dimensions and using nested index loops (i, j).
    In Python, we can achieve this idiomatically using `zip(*matrix)` combined with
    a list comprehension, eliminating the need for manual indexing or memory pre-allocation.
    """
    if not matrix or not matrix[0]:
        return []
    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    print(transpose([[1,2,3],[4,5,6],[7,8,9]]))

    print(transpose([[]]))