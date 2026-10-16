"""Sort a list of integers using the insertion sort algorithm."""


def insertion_sort(a: list[int]) -> list[int]:
    """Sort the input list in place and return that same list.

    Starting at the second element, save the current value as the key and
    scan left through the already-sorted prefix. Shift each larger value one
    position right, place the key in the open position, and repeat for the
    remaining elements. The original list is mutated and then returned.
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a
