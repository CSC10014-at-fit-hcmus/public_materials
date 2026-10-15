# Merge 2 sorted vectors into a single sorted vector

def merge_sort(a, b):
    """Merge sorted lists without C++ vector type declarations."""
    i = 0
    j = 0

    ans = []
    while (i < len(a)) and (j < len(b)):
        if a[i] < b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1

    while (i < len(a)):
        ans.append(a[i])
        i += 1

    while (j < len(b)):
        ans.append(b[j])
        j += 1

    return ans
