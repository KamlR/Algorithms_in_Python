# Основная функция в этом файле - merge_lists.
# Остальные функции созданы для удобства работы с merge_lists.

import sys
import os
hw2_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, hw2_path)
from task1.node import Node

def merge_lists(list1, list2):
  curr = None
  head = None
  while list1 != None or list2 != None:
    if list2 == None or (list1 != None and list1.value < list2.value):
      new_node = Node(list1.value, None)
      list1 = list1.next
    elif list1 == None or list1.value >= list2.value:
      new_node = Node(list2.value, None)
      list2 = list2.next
    if curr == None:
      curr = new_node
      head = new_node
    else:
      curr.next = new_node
      curr = curr.next
  return head

def create_list_from_array(array):
  curr = None
  head = None
  for num in array:
    new_node = Node(num, None)
    if curr == None:
      curr = new_node
      head = new_node
    else:
      curr.next = new_node
      curr = curr.next
  return head

def get_array_from_list(head):
  curr = head
  answer = []
  while curr != None:
    answer.append(curr.value)
    curr = curr.next
  return answer

if __name__ == "__main__":
  x1 = input("Введите элементы для 1 последовательности: ")
  list1 = create_list_from_array(list(map(int, x1.split())))

  x2 = input("Введите элементы для 2 последовательности: ")
  list2 = create_list_from_array(list(map(int, x2.split())))

  print(get_array_from_list(merge_lists(list1, list2)))







