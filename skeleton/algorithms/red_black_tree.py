RED = 0
BLACK = 1


class RBNode:
    def __init__(self, key=None, color=RED, left=None, right=None, p=None):

        self.color = color
        # color either RED or BLACK
        self.key = key
        self.left = left
        self.right = right
        self.p = p


class RBTree:
    def __init__(self):
        self.sentinel = RBNode()
        self.sentinel.color = BLACK
        self.root = self.sentinel

    def _find_iterative(self, current_node, key):
        while current_node is not self.sentinel:

            if key == current_node.key:
                break

            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if current_node is not self.sentinel:
            return current_node
        else:
            raise KeyError("Key not found")

    def _height(self, node):
        if node == self.sentinel:
            return 0
        return max(1 + self._height(node.left), 1 + self._height(node.right))

    def _node_count(self, node):
        if node == self.sentinel:
            return 0
        return 1 + self._node_count(node.left) + self._node_count(node.right)

    def _rb_minimum(self, node):
        while node.left is not self.sentinel:
            node = node.left
        return node

    def _rb_maximum(self, node):
        while node.right is not self.sentinel:
            node = node.right
        return node

    def _rb_transplant(self, u, v):
        if u.p == self.sentinel:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def search(self, key):

        current_node = self._find_iterative(self.root, key)
        return key

    def _preorder_generator(self, node):
        if node is None:
            return
        yield node.key
        if node.left is not self.sentinel:
            yield from self._preorder_generator(node.left)
        if node.right is not self.sentinel:
            yield from self._preorder_generator(node.right)

    def preorder(self):
        yield from self._preorder_generator(self.root)

    def _inorder_generator(self, node):
        if node is None:
            return
        if node.left is not self.sentinel:
            yield from self._inorder_generator(node.left)
        yield node.key
        if node.right is not self.sentinel:
            yield from self._inorder_generator(node.right)

    def inorder(self):
        yield from self._inorder_generator(self.root)

    def _postorder_generator(self, node):
        if node is None:
            return
        if node.left is not self.sentinel:
            yield from self._postorder_generator(node.left)
        if node.right is not self.sentinel:
            yield from self._postorder_generator(node.right)
        yield node.key

    def postorder(self):
        yield from self._postorder_generator(self.root)

    def _print_tree_indented(self, node, level=0):
        if node is None:
            return
        self._print_tree_indented(node.right, level+1)
        print ('  ' * level + str(node.key)+'-'+str(node.color))
        self._print_tree_indented(node.left, level+1)

    def _left_rotate(self, x):
        if x.right == self.sentinel:
            return False
        else:
            y = x.right
            x.right = y.left
            if y.left != self.sentinel:
                y.left.p = x
            y.p = x.p
            if x.p == self.sentinel:
                self.root = y
            elif x == x.p.left:
                x.p.left = y
            else:
                x.p.right = y
            y.left = x
            x.p = y

    def _right_rotate(self, x):

        if x.left == self.sentinel:
            return False
        else:
            y = x.left
            x.left = y.right
            if y.right != self.sentinel:
                y.right.p = x
            y.p = x.p
            if x.p == self.sentinel:
                self.root = y
            elif x == x.p.right:
                x.p.right = y
            else:
                x.p.left = y
            y.right = x
            x.p = y

    def _insert(self, node, current):

        y = self.sentinel
        while current != self.sentinel:
            y = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right
        node.p = y
        if y == self.sentinel:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        node.right = self.sentinel
        node.left = self.sentinel
        node.color = RED
        self._insert_fixup(node)

    def _insert_fixup(self, x):
        while x.p.color == RED:
            if x.p == x.p.p.left:
                y = x.p.p.right
                if y.color == RED:
                    x.p.color = BLACK
                    y.color = BLACK
                    x.p.p.color = RED
                    x = x.p.p
                else:
                    if x == x.p.right:
                        x = x.p
                        self._left_rotate(x)
                    x.p.color = BLACK
                    x.p.p.color = RED
                    self._right_rotate(x.p.p)
            else:
                y = x.p.p.left
                if y.color == RED:
                    x.p.color = BLACK
                    y.color = BLACK
                    x.p.p.color = RED
                    x = x.p.p
                else:
                    if x == x.p.left:
                        x = x.p
                        self._right_rotate(x)
                    x.p.color = BLACK
                    x.p.p.color = RED
                    self._left_rotate(x.p.p)
        self.root.color = BLACK

    def insert(self, key):
        if self.root:
            self._insert(RBNode(key), self.root)
        else:
            self.root = RBNode(key)
        return True

    def _rb_delete_fixup(self, current):
        while current != self.root and current.color == BLACK:
            if current == current.p.left:
                w = current.p.right
                if w.color == RED:
                    w.color = BLACK
                    current.p.color = RED
                    self._left_rotate(current.p)
                    w = current.p.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    current = current.p
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self._right_rotate(w)
                        w = current.p.right
                    w.color = current.p.color
                    current.p.color = BLACK
                    w.right.color = BLACK
                    self._left_rotate(current.p)
                    current = self.root
            else:
                w = current.p.left
                if w.color == RED:
                    w.color = BLACK
                    current.p.color = RED
                    self._right_rotate(current.p)
                    w = current.p.left

                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    current = current.p
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self._left_rotate(w)
                        w = current.p.left

                    w.color = current.p.color
                    current.p.color = BLACK
                    w.left.color = BLACK
                    self._right_rotate(current.p)
                    current = self.root

        current.color = BLACK

    def rb_delete(self, current):
        y = current
        y_original_color = current.color
        if current.right == self.sentinel:
            x = current.left
            self._rb_transplant(current, current.left)
        elif current.left == self.sentinel:
            x = current.right
            self._rb_transplant(current, current.right)
        else:
            successor = self._rb_minimum(current.right)
            y_original_color = successor.color
            x = successor.right
            if successor.p == current:
                x.p = successor
            else:
                self._rb_transplant(successor, successor.right)
                successor.right = current.right
                successor.right.p = successor
            self._rb_transplant(current, successor)
            successor.left = current.left
            successor.left.p = successor
            successor.color = current.color

        if y_original_color == BLACK:
            self._rb_delete_fixup(x)

    def delete(self, key):
        node = self._find_iterative(self.root, key)
        if node:
            self.rb_delete(node)
        return True
