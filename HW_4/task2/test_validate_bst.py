from validate_bst import validate_bst

# ========= Блок подготовки данных =========
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

"""
Класс BST для тестирования валидности бинарного дерева.
Тут реализовано два варината вставки: правильная и неправильная.
Комбинируя два варианта вставки, получаем invalid BST для теста.
"""
class BST:
  def __init__(self):
    self.root = None
  def insert(self, value, insert_type = None):
    if self.root == None:
      self.root = Node(value)
    else:
      if insert_type == None:
        self._insert(self.root, value)
      else:
        self.insidious_insert(self.root, value)

  # коварная вставка (неправильная)      
  def insidious_insert(self, node, value):
    if value < node.value:
      if node.right == None:
        node.right = Node(value)
      else:
        self._insert(node.right, value)
    elif value > node.value:
      if node.left == None:
        node.left = Node(value)
      else:
        self._insert(node.left, value)
    else:
      print("Такой элемент уже есть!")

  # обычная вставка (правильная) 
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


def test_validate_bst_true_first():
  """
  Будем вызывать assert после каждой вставки.
    10
    /  \
  8    14
    \   / \
    9 12  20
        \
        13

  """
  bst = BST()
  assert validate_bst(bst.root) == True

  bst.insert(10)
  assert validate_bst(bst.root) == True
  bst.insert(14)
  assert validate_bst(bst.root) == True
  bst.insert(8)
  assert validate_bst(bst.root) == True
  bst.insert(9)
  assert validate_bst(bst.root) == True
  bst.insert(20)
  assert validate_bst(bst.root) == True
  bst.insert(12)
  assert validate_bst(bst.root) == True
  bst.insert(13)
  assert validate_bst(bst.root) == True


def test_validate_bst_true_second():
  """
  Сделаем в дереве побольше поворотов, так как это будет чаще менять min_val и max_val.
                  10
               /      \
              5       20
             / \      /
            3   8     17
           / \ / \      \
          1  4 6  9     19
                \      /
                 7    18
                      
  """
  bst = BST()
  bst.insert(10)
  assert validate_bst(bst.root) == True
  bst.insert(20)
  assert validate_bst(bst.root) == True
  bst.insert(5)
  assert validate_bst(bst.root) == True
  bst.insert(8)
  assert validate_bst(bst.root) == True
  bst.insert(9)
  assert validate_bst(bst.root) == True
  bst.insert(17)
  assert validate_bst(bst.root) == True
  bst.insert(19)
  assert validate_bst(bst.root) == True
  bst.insert(18)
  assert validate_bst(bst.root) == True
  bst.insert(6)
  assert validate_bst(bst.root) == True
  bst.insert(7)
  assert validate_bst(bst.root) == True
  bst.insert(3)
  assert validate_bst(bst.root) == True
  bst.insert(4)
  assert validate_bst(bst.root) == True
  bst.insert(1)
  assert validate_bst(bst.root) == True


def test_validate_bst_false():
  """
  После всех вставок ниже (верных и неверных) получим вот такое дерево:
                  10
               /      \
              6       15
             /  \       \
            4    7       8
           /  \         / \
          16   5       9   3
            \             /
            14           4
  """

  bst = BST()
  # ====== блок валидного дерева начат ======
  bst.insert(10)
  bst.insert(15)
  bst.insert(6)
  bst.insert(7)
  bst.insert(4)
  bst.insert(5)
  assert validate_bst(bst.root) == True
  #====== блок валидного дерева закончен ======

  # ====== блок невалидного дерева начат ======
  bst.insert(8, "insidious")
  assert validate_bst(bst.root) == False
  bst.insert(9, "insidious")
  assert validate_bst(bst.root) == False
  bst.insert(16, "insidious")
  assert validate_bst(bst.root) == False
  bst.insert(14, "insidious")
  assert validate_bst(bst.root) == False
  bst.insert(3, "insidious")
  assert validate_bst(bst.root) == False
  bst.insert(4, "insidious")
  
