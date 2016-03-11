RED = "R"
BLACK = "B"


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

    def rb_minimum(self, node):
        while node.left is not self.sentinel:
            node = node.left
        return node

    def rb_maximum(self, node):
        while node.right is not self.sentinel:
            node = node.right
        return node

    def rb_transplant(self, u, v):
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
        print ('  ' * level + str(node.key)+node.color)
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

    def _insert(self, z):

        y = self.sentinel
        x = self.root
        while x != self.sentinel:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.sentinel:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.right = self.sentinel
        z.left = self.sentinel
        z.color = RED

    def _rb_insert_fixup(self, x):
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

    def rb_insert(self, x):
        self._insert(x)
        self._rb_insert_fixup(x)
        return True

    def _rb_delete_fixup(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.p.left:
                w = x.p.right
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self._left_rotate(x.p)
                    w = x.p.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.p
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self._right_rotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = BLACK
                    self._left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self._rotate_right(x.p)
                    w = x.p.left

                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.p
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self._rotate_left(w)
                        w = x.p.left

                    w.color = x.p.color
                    x.p.color = BLACK
                    w.left.color = BLACK
                    self._rotate_right(x.p)
                    x = self.root

        x.color = BLACK

    def rb_delete(self, z):
        if z is None or z == self.sentinel:
            return
        y = z
        y_original_color = y.color
        if z.left == self.sentinel:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.sentinel:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.rb_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == BLACK:
            self._rb_delete_fixup(x)


five_right = RBTree()
five_right.root = RBNode(3, BLACK)
five_right.root.p = five_right.sentinel
five_right.root.right = RBNode(5, BLACK)
five_right.root.right.p = five_right.root
five_right.root.left = RBNode(2, BLACK)
five_right.root.left.p = five_right.root
five_right.root.right.right = RBNode(7, RED)
five_right.root.right.right.p = five_right.root.right
five_right.root.right.left = RBNode(4, RED)
five_right.root.right.left.p = five_right.root.right

# five_right._print_tree_indented(five_right.root)
# five_right._left_rotate(five_right.root)
# five_right._print_tree_indented(five_right.root)


five_left = RBTree()
five_left.rb_insert(RBNode(5))
five_left.rb_insert(RBNode(7))
five_left.rb_insert(RBNode(3))
five_left.rb_insert(RBNode(4))
five_left.rb_insert(RBNode(2))
five_left.rb_insert(RBNode(9))

# five_left.root = RBNode(5, BLACK)
# five_left.root.p = five_left.sentinel
# five_left.root.right = RBNode(7, RED)
# five_left.root.right.p = five_left.root
#five_left.root.right.right = five_left.sentinel
#five_left.root.right.left = five_left.sentinel
#five_left.root.left = RBNode(3, RED)
#five_left.root.left.p = five_left.root
#five_left.root.left.right = RBNode(4, BLACK)
#five_left.root.left.right.p = five_left.root.left
#five_left.root.left.right.right = five_left.sentinel
#five_left.root.left.right.left = five_left.sentinel
#five_left.root.left.left = RBNode(2, BLACK)
#five_left.root.left.left.p = five_left.root.left
#five_left.root.left.left.left = five_left.sentinel
#five_left.root.left.left.right = five_left.sentinel

#five_left._print_tree_indented(five_left.root)
# five_left._right_rotate(five_left.root)
# five_left._print_tree_indented(five_left.root
#print(five_left.root.key)
#node = RBNode(9, RED)
# print(node.key)
#five_left.rb_insert(node)
# five_left._print_tree_indented(five_left.root)
five_left.rb_delete(five_left.root)
five_left._print_tree_indented(five_left.root)
# test_list = list(five_left.inorder())
# print(test_list)
# print(five_left.search(9))
# test_list2 = list(five_left.postorder())
# print(test_list2)
