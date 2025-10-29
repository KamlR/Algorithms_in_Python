class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    # === Вспомогательные методы ===
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # === Общая функция для балансировки ===
    def _rebalance(self, node, key=None):
      balance = self.get_balance(node)

      # LL case
      if balance > 1 and self.get_balance(node.left) >= 0:
          return self._rotate_right(node)

      # LR case
      if balance > 1 and self.get_balance(node.left) < 0:
          node.left = self._rotate_left(node.left)
          return self._rotate_right(node)

      # RR case
      if balance < -1 and self.get_balance(node.right) <= 0:
          return self._rotate_left(node)

      # RL case
      if balance < -1 and self.get_balance(node.right) > 0:
          node.right = self._rotate_right(node.right)
          return self._rotate_left(node)

      return node


    # === Вставка ===
    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # дубликаты не вставляем

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return self._rebalance(node, key)

    def insert_key(self, key):
        self.root = self._insert(self.root, key)

    # === Удаление ===
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Узел найден
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return self._rebalance(node, key)

    def delete_key(self, key):
        self.root = self._delete(self.root, key)

    # === Поиск ===
    def _search(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def search_key(self, key):
        return self._search(self.root, key)

    # === Симметричный обход (для проверки) ===
    def inorder(self, node):
        if node:
            return self.inorder(node.left) + [node.key] + self.inorder(node.right)
        return []

avl = AVL()
avl.insert_key(10)
avl.insert_key(12)
avl.insert_key(8)
avl.insert_key(13)
print(avl.inorder(avl.root))

