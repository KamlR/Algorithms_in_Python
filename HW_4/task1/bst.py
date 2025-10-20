import sys
import os
hw4_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, hw4_path)
from task1.node import Node

class BST:
  def __init__(self):
    self.root = None
  def insert(self, value):
    if self.root == None:
      self.root = Node(value)
    else:
      self._insert(self.root, value)
  def _insert(self, node, value):
    if value > node.value:
      if node.right == None:
        node.right = Node(value)
      else:
        self._insert(node.right, value)
    elif value < node.value:
      if node.left == None:
        node.left = Node(value)
      else:
        self._insert(node.left, value)
    else:
      print("Такой элемент уже есть!")

  
  def preorder(self, node, result):
    """
      корень -> лево -> право
    """
    if node == None:
      return
    #print(node.value, end=" ")
    result.append(node.value)
    self.preorder(node.left, result)
    self.preorder(node.right, result)

  def inorder(self, node, result):
    """
      лево -> корень -> право
    """
    if node == None:
      return
    self.inorder(node.left, result)
    #print(node.value, end=" ")
    result.append(node.value)
    self.inorder(node.right, result)
  
  def postorder(self, node, result):
    """
      лево -> право -> корень
    """
    if node == None:
      return
    self.postorder(node.left, result)
    self.postorder(node.right, result)
    #print(node.value, end=" ")
    result.append(node.value)
  
  def reverse_preorder(self, node, result):
    """
       корень -> право -> лево
    """
    if node == None:
      return
    #print(node.value, end=" ")
    result.append(node.value)
    self.reverse_preorder(node.right, result)
    self.reverse_preorder(node.left, result)

  def reverse_postorder(self, node, result):
    """
      право -> лево -> корень
    """
    if node == None:
      return
    self.reverse_postorder(node.right, result)
    self.reverse_postorder(node.left, result)
    #print(node.value, end=" ")
    result.append(node.value)

  
  def reverse_inorder(self, node, result):
    """
      право -> корень -> лево
    """
    if node == None:
      return
    self.reverse_inorder(node.right, result)
    #print(node.value, end=" ")
    result.append(node.value)
    self.reverse_inorder(node.left, result)


  def tree_traversal(self, traversal_type):
    traversals = {
        "preorder": self.preorder,
        "inorder": self.inorder,
        "postorder": self.postorder,
        "reverse preorder": self.reverse_preorder,
        "reverse postorder": self.reverse_postorder,
        "reverse inorder": self.reverse_inorder
    }
    result = []
    traversal_func = traversals.get(traversal_type)
    if traversal_func:
        traversal_func(self.root, result)
        return result
    else:
        print("Был передан неизвестный тип обхода")
