from mergesort_iterative import merge_sort_iterative
from random import randint

def test_merge_sort():
  max_size = 1000
  for size in range(0, max_size + 1):
    nums1 = [randint(-200, 200) for _ in range(size)]
    nums2 = nums1.copy()
    nums1.sort()
    assert nums1 == merge_sort_iterative(nums2)

def test_merge_sort_ascending():
  max_size = 1000
  for size in range(0, max_size + 1):
    nums1 = list(range(size))
    nums2 = nums1.copy()
    nums1.sort()
    assert nums1 == merge_sort_iterative(nums2)

def test_merge_sort_descending():
  max_size = 1000
  for size in range(0, max_size + 1):
    nums1 = list(range(size))
    nums1 = nums1[::-1]
    nums2 = nums1.copy()
    nums1.sort()
    assert nums1 == merge_sort_iterative(nums2)

def test_merge_sort_duplicates():
  max_size = 1000
  for size in range(0, max_size + 1):
    nums1 = [5] * size
    nums2 = nums1.copy()
    nums1.sort()
    assert nums1 == merge_sort_iterative(nums2)