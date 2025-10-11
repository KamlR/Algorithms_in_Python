from two_sum import two_sum

def test_two_sum():
  assert two_sum([2, 1], 3) == str(0) + " " + str(1)
  assert two_sum([1, 2, 3], 5) == str(1) + " " + str(2)
  assert two_sum([3, 4, 2, 10], 13) == str(0) + " " + str(3)
  assert two_sum([3, 4, 2, 10], 6) == str(1) + " " + str(2)
  assert two_sum([3, 4, 2, 10], 12) == str(2) + " " + str(3)
  assert two_sum([5, 1, 9, 10, 1], 6) == str(0) + " " + str(1)
  assert two_sum([5, 1, 9, 10, 1], 2) == str(1) + " " + str(4)
  assert two_sum([5, 1, 9, 10, 1], 19) == str(2) + " " + str(3)
  assert two_sum([5, 1, 9, 10, 1], 11) == str(1) + " " + str(3)
  assert two_sum([12, 100, 56, 23, 200], 212) == str(0) + " " + str(4)
  assert two_sum([12, 100, 56, 23, 200], 123) == str(1) + " " + str(3)
  assert two_sum([12, 100, 56, 23, 200], 79) == str(2) + " " + str(3)
  assert two_sum([12, 100, 56, 23, 200], 300) == str(1) + " " + str(4)
  assert two_sum([12, 100, 56, 23, 200], 300) == str(1) + " " + str(4)
  assert two_sum([1000, 2000, 100, 3000, 4000], 4000) == str(0) + " " + str(3)
  assert two_sum([1000, 2000, 100, 3000, 4000], 4000) == str(0) + " " + str(3)
  assert two_sum([1000, 2000, 100, 3000, 4000], 2100) == str(1) + " " + str(2)
  assert two_sum([1000, 2000, 100, 3000, 4000], 5000) == str(0) + " " + str(4)
  