# Binary search


def b_search(ar1, value):
    lo, hi = 0, len(ar1)
    while lo <= hi:
        mid = (lo + hi) / 2
        if value > ar1[mid]:
            lo = mid + 1
        elif value < ar1[mid]:
            hi = mid - 1
        else:
            return mid
    return None


ar1 = [1, 2, 3, 4, 5, 6, 7]
print b_search(ar1, 5)
