import sys
import os
hw5_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, hw5_path)
from task1.tracer import tracer

# Для визуализации стека вызовов используем декоратор @tracer из task1.
class Permutations:
    result = []
    def __init__(self):
      pass
    def make_permutations(self, nums):
      self.result = []
      self._backtrack([], nums)
    @tracer
    def _backtrack(self, path, remaining):
      if not remaining:
        self.result.append(path)
        return
      for i in range(len(remaining)):
        self._backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
    def get_result(self):
      return self.result

k = Permutations()
k.make_permutations([1, 2, 3])
print(k.get_result())