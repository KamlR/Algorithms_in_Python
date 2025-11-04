def merge_list(a, b):
    c = []
    n = len(a)
    m = len(b)

    i = 0
    j = 0
    while i < n and j < m:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c


def merge_sort_iterative(arr):
    """Итеративная версия merge sort (bottom-up)"""
    width = 1
    n = len(arr)
    result = arr[:]

    while width < n:
        for i in range(0, n, 2 * width):
            left = result[i:i + width]
            right = result[i + width:i + 2 * width]
            merged = merge_list(left, right)
            result[i:i + 2 * width] = merged
        width *= 2

    return result


a = [9, 5, -3, 4, 7, 8, -8]
print(merge_sort_iterative(a))
