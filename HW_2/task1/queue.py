from node import Node

class Queue:
  def __init__(self):
      self.front = None
      self.back = None
      self.size = 0

  def push(self, value):
    new_node = Node(value, None) 
    if self.front == None and self.back == None:
      self.front = new_node
      self.back = new_node
    else:
       self.back.next = new_node
       self.back = new_node 
    self.size+=1

  def pop(self):
    if self.is_empty():
      raise IndexError("Попытка удалить элемент из пустой очереди")
    value = self.front.value
    self.front = self.front.next
    if self.front == None:
       self.back = None
    self.size-=1
    return value
  
  def peek(self):
    if self.is_empty():
       raise IndexError("Попытка достать элемент из пустой очереди")
    return self.front.value
  
  def get_size(self):
    return self.size
  
  def is_empty(self):
    return self.front is None and self.back is None


    


    