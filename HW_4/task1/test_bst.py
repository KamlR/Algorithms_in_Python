from bst import BST

# ---------- Варианты деревьев ----------

def build_tree_right_heavy():
    """
    Полностью правое дерево:
        1
         \
          2
           \
            3
             ...
              \
               10
    """
    bst = BST()
    for v in range(1, 11):
        bst.insert(v)
    return bst


def build_tree_left_heavy():
    """
    Полностью левое дерево:
                10
               /
              9
             /
            ...
           /
          1
    """
    bst = BST()
    for v in range(10, 0, -1):
        bst.insert(v)
    return bst


def build_tree_mixed():
    """
    Смешанное дерево (не строгое):
             8
           /   \
          4     12
         / \   /  \
        2  6  10  14
           \
            7
    """
    bst = BST()
    for v in [8, 4, 12, 2, 6, 10, 14, 7]:
        bst.insert(v)
    return bst


# ---------- Тестируем на подготовленных данных каждый вариант обхода ----------

def test_preorder():
    bst = BST()
    assert bst.tree_traversal("preorder") == [] 

    bst.insert(10)
    assert bst.tree_traversal("preorder") == [10]              

    bst = build_tree_right_heavy()
    assert bst.tree_traversal("preorder") == list(range(1, 11))    

    bst = build_tree_left_heavy()
    assert bst.tree_traversal("preorder") == list(range(10, 0, -1)) 

    bst = build_tree_mixed()
    assert bst.tree_traversal("preorder") == [8, 4, 2, 6, 7, 12, 10, 14] 


def test_inorder():
    bst = BST()
    assert bst.tree_traversal("inorder") == []

    bst.insert(10)
    assert bst.tree_traversal("inorder") == [10]

    bst = build_tree_right_heavy()
    assert bst.tree_traversal("inorder") == list(range(1, 11))

    bst = build_tree_left_heavy()
    assert bst.tree_traversal("inorder") == list(range(1, 11))

    bst = build_tree_mixed()
    assert bst.tree_traversal("inorder") == [2, 4, 6, 7, 8, 10, 12, 14]


def test_postorder():
    bst = BST()
    assert bst.tree_traversal("postorder") == []

    bst.insert(10)
    assert bst.tree_traversal("postorder") == [10]

    bst = build_tree_right_heavy()
    assert bst.tree_traversal("postorder") == list(range(10, 0, -1))

    bst = build_tree_left_heavy()
    assert bst.tree_traversal("postorder") == list(range(1, 11))

    bst = build_tree_mixed()
    assert bst.tree_traversal("postorder") == [2, 7, 6, 4, 10, 14, 12, 8]


def test_reverse_preorder():
    bst = BST()
    assert bst.tree_traversal("reverse preorder") == []

    bst.insert(10)
    assert bst.tree_traversal("reverse preorder") == [10]

    bst = build_tree_right_heavy()
    assert bst.tree_traversal("reverse preorder") == list(range(1, 11))

    bst = build_tree_left_heavy()
    assert bst.tree_traversal("reverse preorder") == list(range(10, 0, -1))

    bst = build_tree_mixed()
    assert bst.tree_traversal("reverse preorder") == [8, 12, 14, 10, 4, 6, 7, 2]


def test_reverse_inorder():
    bst = BST()
    assert bst.tree_traversal("reverse inorder") == []

    bst.insert(10)
    assert bst.tree_traversal("reverse inorder") == [10]

    bst = build_tree_right_heavy()
    assert bst.tree_traversal("reverse inorder") == list(range(10, 0, -1))

    bst = build_tree_left_heavy()
    assert bst.tree_traversal("reverse inorder") == list(range(10, 0, -1))

    bst = build_tree_mixed()
    assert bst.tree_traversal("reverse inorder") == [14, 12, 10, 8, 7, 6, 4, 2]


def test_reverse_postorder():
    bst = BST()
    assert bst.tree_traversal("reverse postorder") == []

    bst.insert(10)
    assert bst.tree_traversal("reverse postorder") == [10]

    bst = build_tree_right_heavy()
    assert bst.tree_traversal("reverse postorder") == list(range(10, 0, -1))

    bst = build_tree_left_heavy()
    assert bst.tree_traversal("reverse postorder") == list(range(1, 11))

    bst = build_tree_mixed()
    assert bst.tree_traversal("reverse postorder") == [14, 10, 12, 7, 6, 2, 4, 8]
