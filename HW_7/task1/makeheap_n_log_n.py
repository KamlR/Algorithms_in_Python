def sift_up(a, i):
  while i > 0:
      p = (i - 1) // 2  # индекс родителя
      if a[p] <= a[i]:
          break
      a[p], a[i] = a[i], a[p]
      i = p
def makeheap_n_log_n(arr):
  for i in range(1, len(arr)):
    sift_up(arr, i)
  return arr

k = [3, 2, 1]
print(makeheap_n_log_n(k))
