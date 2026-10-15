
def insertion_sort(a: list[int]) -> list[int]:
    """Sort the list in place using insertion sort and return it.

    Unlike C++, Python lists can be modified directly without declaring
    a reference type explicitly.
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a
