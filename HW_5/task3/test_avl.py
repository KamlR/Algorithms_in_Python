from avl import AVL

def test_insert_left_rotations():
  avl = AVL()
  avl.insert_key(10)
  avl.insert_key(14)
  avl.insert_key(7)
  assert avl.inorder(avl.root) == [7, 10, 14]

  avl.insert_key(18)
  # левый поворот
  avl.insert_key(22)
  assert avl.inorder(avl.root) == [7, 10, 14, 18, 22]

 # левый поворот
  avl.insert_key(24)
  assert avl.inorder(avl.root) == [7, 10, 14,18, 22, 24]

  avl.insert_key(8)
  # левый поворот
  avl.insert_key(9)
  assert avl.inorder(avl.root) == [7, 8, 9,10, 14, 18, 22, 24]


def test_insert_right_rotations():
  avl = AVL()
  avl.insert_key(10)
  avl.insert_key(14)
  avl.insert_key(7)
  avl.insert_key(3)
  # правый поворот 
  avl.insert_key(2)
  assert avl.inorder(avl.root) == [2, 3, 7, 10, 14]
  # правый поворот
  avl.insert_key(1)
  assert avl.inorder(avl.root) == [1, 2, 3, 7, 10, 14]

def test_insert_left_right_rotations():
  avl = AVL()
  avl.insert_key(10)
  avl.insert_key(20)
  avl.insert_key(5)
  avl.insert_key(7)
  avl.insert_key(3)
  # левый, правый поворот
  avl.insert_key(9)
  assert avl.inorder(avl.root) == [3, 5, 7, 9, 10, 20]

def test_insert_right_left_rotations():
  avl = AVL()
  avl.insert_key(40)
  avl.insert_key(20)
  avl.insert_key(60)
  avl.insert_key(50)
  avl.insert_key(70)
  # правый, левый поворот
  avl.insert_key(55)
  assert avl.inorder(avl.root) == [20, 40, 50, 55, 60, 70]
  avl.insert_key(70)
  avl.insert_key(65)
  avl.insert_key(80)
  # правый, левый поворот
  avl.insert_key(64)
  assert avl.inorder(avl.root) == [20, 40, 50, 55, 60, 64, 65, 70, 80]


def test_delete_right():
    avl = AVL()
    for key in [30, 20, 40, 10]:
        avl.insert_key(key)
    # Структура перед удалением:
    #        30
    #       /  \
    #     20   40
    #    /
    #  10
    #
    # Удаляем 40 → дисбаланс у 30 (+2), выполняется правый поворот
    avl.delete_key(40)
    assert avl.inorder(avl.root) == [10, 20, 30]


def test_delete_left_rotation():
    avl = AVL()
    for key in [10, 5, 20, 15, 30]:
        avl.insert_key(key)
    # Структура перед удалением:
    #       10
    #      /  \
    #     5    20
    #         /  \
    #       15    30
    #
    # Удаляем 5 → дисбаланс у 10 (-2), выполняется левый поворот
    avl.delete_key(5)
    assert avl.inorder(avl.root) == [10, 15, 20, 30]


def test_delete_left_right_rotation():
    avl = AVL()
    for key in [50, 20, 60, 10, 30, 25]:
        avl.insert_key(key)
    # Структура:
    #        50
    #       /  \
    #     20    60
    #    /  \
    #  10   30
    #       /
    #     25
    #
    # Удаляем 60 → у 50 баланс +2, у левого поддерева (20) баланс -1
    avl.delete_key(60)
    assert avl.inorder(avl.root) == [10, 20, 25, 30, 50]


def test_delete_right_left_rotation():
    avl = AVL()
    for key in [10, 5, 30, 25, 40, 35]:
        avl.insert_key(key)
    # Структура:
    #        10
    #       /  \
    #      5    30
    #          /  \
    #        25    40
    #              /
    #            35
    #
    # Удаляем 5 → дисбаланс у 10 (-2), у правого поддерева (30) баланс +1 → RL
    avl.delete_key(5)
    assert avl.inorder(avl.root) == [10, 25, 30, 35, 40]



  
