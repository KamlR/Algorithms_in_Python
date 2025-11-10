from minheap import kth_largest_using_class, kth_largest_using_library
from random import randint

def test_kth_largest_using_class():
  for size in range(10, 100 + 1):
    nums = [randint(-100, 100) for _ in range(size)]
    nums_sort = nums.copy()
    nums_sort.sort()
    for k in range(0, size):
      assert nums_sort[-(k + 1)] == kth_largest_using_class(nums, k + 1)

def test_kth_largest_using_library():
  for size in range(10, 100 + 1):
    nums = [randint(-100, 100) for _ in range(size)]
    nums_sort = nums.copy()
    nums_sort.sort()
    for k in range(0, size):
      assert nums_sort[-(k + 1)] == kth_largest_using_library(nums, k + 1)