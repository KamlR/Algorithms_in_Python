from merge_lists import *
import random

# Тестируем случаи с пустыми списками.
def test_merge_lists_empty():
  head = merge_lists(create_list_from_array([]), create_list_from_array([]))
  assert get_array_from_list(head) == []

  head = merge_lists(create_list_from_array([1]), create_list_from_array([]))
  assert get_array_from_list(head) == [1]

  head = merge_lists(create_list_from_array([]), create_list_from_array([2]))
  assert get_array_from_list(head) == [2]

# Тестируем случаи, когда оба списка одной длины.
def test_merge_lists_same_len():
  for i in range(1, 21):
    x1 = sorted(create_random_array(i))
    x2 = sorted(create_random_array(i))
    expected_answer = sorted(x1 + x2)
    head = merge_lists(create_list_from_array(x1), create_list_from_array(x2))
    assert get_array_from_list(head) == expected_answer

# Тестируем случаи, когда два списки разной длины.
def test_merge_lists_different_len():
  # Первый всегда больше по длине
  for i in range(1, 21):
    for j in range(1, 10):
      x1 = sorted(create_random_array(i + j))
      x2 = sorted(create_random_array(i))
      expected_answer = sorted(x1 + x2)
      head = merge_lists(create_list_from_array(x1), create_list_from_array(x2))
      assert get_array_from_list(head) == expected_answer
  # Второй всегда больше по длине
  for i in range(1, 21):
    for j in range(1, 10):
      x1 = sorted(create_random_array(i))
      x2 = sorted(create_random_array(i + j))
      expected_answer = sorted(x1 + x2)
      head = merge_lists(create_list_from_array(x1), create_list_from_array(x2))
      assert get_array_from_list(head) == expected_answer

# Тестируем случаи, когда в списках есть одинаковые элементы.
def test_merge_lists_same_elemets():
  for i in range(1, 21):
    same_elements = random.randint(1, (i // 2) + 1)
    x1 = sorted(create_random_array(i))
    x2 = create_random_array(i)
    random_index = random.randint(0, i - 1)
    for j in range(0, same_elements):
      x2[j] = x1[random_index]
    x2.sort()
    expected_answer = sorted(x1 + x2)
    head = merge_lists(create_list_from_array(x1), create_list_from_array(x2))
    assert get_array_from_list(head) == expected_answer
    
def create_random_array(n):
  return [random.randint(0, 100) for _ in range(n)]