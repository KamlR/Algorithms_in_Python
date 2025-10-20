from balanced_tree import is_balanced_bst

import sys
import os
hw4_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, hw4_path)
from task1.bst import BST

def test_balance():
  bst = BST()
  assert is_balanced_bst(bst.root) == True

  bst.insert(10)
  assert is_balanced_bst(bst.root) == True
  bst.insert(20)
  assert is_balanced_bst(bst.root) == True
  bst.insert(17)
  assert is_balanced_bst(bst.root) == False
  bst.insert(5)
  assert is_balanced_bst(bst.root) == True
  bst.insert(19)
  assert is_balanced_bst(bst.root) == False
  bst.insert(3)
  assert is_balanced_bst(bst.root) == False
  bst.insert(22)
  assert is_balanced_bst(bst.root) == True
  bst.insert(4)
  assert is_balanced_bst(bst.root) == False
  bst.insert(1)
  assert is_balanced_bst(bst.root) == False
  bst.insert(8)
  assert is_balanced_bst(bst.root) == True
  bst.insert(9)
  assert is_balanced_bst(bst.root) == True
  
  
  
 