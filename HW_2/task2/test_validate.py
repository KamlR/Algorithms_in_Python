from validate import check_pushed_popped
def test_empty_pushed_or_popped():
  # немного спорный случай, если два списка пустые, но пусть будет False.
  assert check_pushed_popped([], []) == False
  assert check_pushed_popped([1], []) == False
  assert check_pushed_popped([], [1]) == False

def test_pushed_or_popped_true():
  assert check_pushed_popped([2, 3], [3, 2]) == True
  assert check_pushed_popped([1, 2, 3, 4], [4, 3, 2, 1]) == True
  assert check_pushed_popped([4, 3, 2, 1], [3, 4, 1, 2]) == True
  assert check_pushed_popped([1, 2, 3, 4], [1, 2, 3, 4]) == True
  assert check_pushed_popped([3, 4, 2, 1, 5, 6], [1, 2, 6, 5, 4, 3]) == True
  assert check_pushed_popped([1, 2, 5, 6, 7, 8 ], [2, 1, 8, 7, 6, 5]) == True

def test_pushed_or_popped_false():
  assert check_pushed_popped([1, 2, 3], [3, 1, 2]) == False
  assert check_pushed_popped([1, 2, 3, 4], [3, 4, 1, 2]) == False
  assert check_pushed_popped([1, 2, 3, 4, 5, 6 ], [6, 1, 2, 3, 4, 5]) == False
  assert check_pushed_popped([1, 2, 3, 4, 5, 6], [1, 2, 3, 6, 4, 5]) == False
  


