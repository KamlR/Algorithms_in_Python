import heapq
class MinHeap:
  def __init__(self):
    self.heap = []
  
  def _parent(self, i): return (i - 1) // 2
  def _left(self, i): return 2 * i + 1
  def _right(self, i): return 2 * i + 2

  def _swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def pop(self):
    if len(self.heap) == 0:
      raise IndexError("pop from empty heap")
    self._swap(0, len(self.heap) - 1)
    min_val = self.heap.pop()
    self._heapify_down(0)
    return min_val

  def push(self, value):
    self.heap.append(value)
    self._heapify_up(len(self.heap) - 1)

  def _heapify_up(self, i):
    while i > 0 and self.heap[i] < self.heap[self._parent(i)]:
      self._swap(i, self._parent(i))
      i = self._parent(i)
  
  def _heapify_down(self, i):
    smallest = i
    left, right = self._left(i), self._right(i)
    if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
        smallest = left
    if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
        smallest = right
    if smallest != i:
        self._swap(i, smallest)
        self._heapify_down(smallest)
  def peek(self):
    if len(self.heap) == 0:
      raise IndexError("trying to get the element from empty heap")
    return self.heap[0]

  def __len__(self):
    return len(self.heap)


def kth_largest_using_class(nums, k):
  minheap = MinHeap()

  for num in nums:
    if len(minheap) < k:
      minheap.push(num)
    elif num > minheap.peek():
      minheap.pop()
      minheap.push(num)
  return minheap.peek()

# попробуем сделать как можно более выгодное по времени решение, опираясь на офиц. доку.
# комменты по времени работы буду брать из доки.
def kth_largest_using_library(nums, k):
  heap = nums[:k]
  # transform list x into a min-heap, in-place, in linear time.
  heapq.heapify(heap)

  for num in nums[k:]:
    if num > heap[0]:
      # This one step operation is more efficient than a heappop() followed by heappush() and can be more appropriate when using a fixed-size heap.
      heapq.heapreplace(heap, num) 
  return heap[0]