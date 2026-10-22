def binary_search(a: list[int], key: int) -> int:
    "Binary search: Python arbitrary-precision ints prevent (lo + hi) // 2 overflow."
    # In C++, computing the midpoint typically requires lo + (hi - lo) / 2
    # to prevent 32-bit signed integer overflow when lo + hi > INT_MAX.
    # In Python, integers have arbitrary precision (unbounded), so (lo + hi) // 2
    # is inherently safe from arithmetic overflow.
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == key:
            return mid
        if a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
