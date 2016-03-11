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

"""
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
five_left.rb_insert(RBNode(2))

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
five_left._print_tree_indented(five_left.root)
"""
