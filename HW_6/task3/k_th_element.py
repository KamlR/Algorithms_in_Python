def partition(arr, start, end):
    """Разделение массива вокруг pivot"""
    pivot = arr[end]  
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def find_k_element(arr, k):
  start = 0
  end = len(arr) - 1
  n = len(arr)

  while start <= end:
    pos = partition(arr, start, end)
    right_count = n - pos 

    if right_count == k:
        return arr[pos]
    elif right_count > k:
        start = pos + 1
    else:
        end = pos - 1
