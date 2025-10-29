# для тестирования воспользуюсь уже реализованной функцией
from itertools import permutations
import random
from permutations import Permutations

def test_permutations():
  perms  = Permutations()
  for n in range(0, 10):
    for _ in range(3):
      nums = [random.randint(1, 100) for _ in range(n)]
      perms.make_permutations(nums)
      excepted_result = [list(p) for p in permutations(nums)]
      assert perms.get_result() == excepted_result
