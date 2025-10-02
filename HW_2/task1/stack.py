from task1.node import Node

class Stack:
    def __init__(self):
      self.top = None
      self.size = 0

    def push(self, value):
      new_node = Node(value, self.top)
      self.top = new_node
      self.size += 1

    def pop(self):
      if self.is_empty():
          raise IndexError("Попытка удалить элемент из пустого стека")
      value = self.top.value
      self.top = self.top.next
      self.size -= 1
      return value
    
    def peek(self):
        if self.is_empty():
          raise IndexError("Попытка получить элемент из пустого стека")
        return self.top.value
    
    def get_size(self):
      return self.size

    def is_empty(self):
        return self.top is None


