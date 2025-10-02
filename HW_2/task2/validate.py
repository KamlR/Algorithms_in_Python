# В этой задаче использую написанный в task1 класс Stack
# Шаги с импортом чуть странные, по-другому не хотел импортировать
import sys
import os
hw2_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, hw2_path)
from task1.stack import Stack



def check_pushed_popped(pushed, popped):
  if len(pushed) == 0 or len(popped) == 0:
    return False
  s = Stack()
  s.push(pushed[0])
  i_pushed = 1
  i_pop = 0

  while True:
    while not s.is_empty() and s.peek() == popped[i_pop]:
      s.pop()
      i_pop+=1
    if i_pushed == len(pushed):
      break
    else:
      s.push(pushed[i_pushed])
      i_pushed+=1
  return s.is_empty()
  


if __name__ == "__main__":
  pushed_input = input("Введите элементы для pushed через пробел: ")
  pushed = list(map(int, pushed_input.split()))

  popped_input = input("Введите элементы для popped через пробел: ")
  popped = list(map(int, popped_input.split()))

  print(check_pushed_popped(pushed, popped))