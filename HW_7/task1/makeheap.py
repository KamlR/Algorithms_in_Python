def sift_down(a, i, n):
  while True:
      left = 2 * i + 1
      right = 2 * i + 2
      smallest = i

      if left < n and a[left] < a[smallest]:
          smallest = left
      if right < n and a[right] < a[smallest]:
          smallest = right

      if smallest == i:
          break

      a[i], a[smallest] = a[smallest], a[i]
      i = smallest

def makeheap(arr):
    n = len(arr)
    # начинаем с последнего родителя и идём вверх
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)
    return arr
