from k_th_element import find_k_element
from random import randint

def test_find_k_element():
  for size in range(10, 300 + 1):
    nums = [randint(-100, 100) for _ in range(size)]
    nums_sort = nums.copy()
    nums_sort.sort()
    for k in range(0, size):
      assert nums_sort[-(k + 1)] == find_k_element(nums, k + 1)


