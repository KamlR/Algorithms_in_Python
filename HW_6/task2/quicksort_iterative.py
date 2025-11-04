def partition(arr, low, high):
    """Разделение массива вокруг pivot"""
    pivot = arr[high]  
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_iterative(arr):
    """Итеративная версия Quick Sort"""
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            p = partition(arr, low, high)
            stack.append((low, p - 1))
            stack.append((p + 1, high))

    return arr


