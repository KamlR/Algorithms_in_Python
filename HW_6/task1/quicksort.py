from time_decorator import timeit
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

@timeit
def quick_sort_time(arr):
    return quick_sort(arr)



max_len = 1000
for n in range(0, max_len + 1):
  nums1 = [random.randint(-200, 200) for _ in range(n)]
  nums1.sort(reverse=True)
  quick_sort_time(nums1)