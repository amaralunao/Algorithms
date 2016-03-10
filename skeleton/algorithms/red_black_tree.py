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

    def left_rotate(self, x):
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

    def right_rotate(self, x):

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

    def rb_insert(self, key):
        x = RBNode(key)
        self._insert(x)
        x.color = RED
        while x != self.root and x.p.color == RED:
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
                        self.left_rotate(x)
                    x.p.color = BLACK
                    x.p.p.color = RED
                    self.right_rotate(x.p.p)
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
                        self.right_rotate(x)
                    x.p.color = BLACK
                    x.p.p.color = RED
                    self.left_rotate(x.p.p)
        self.root.color = BLACK

five_right = RBTree()
five_right.root = RBNode(3, BLACK)
five_right.root.p = five_right.sentinel
five_right.root.right = RBNode(5, RED)
five_right.root.right.p = five_right.root
five_right.root.left = RBNode(2, RED)
five_right.root.left.p = five_right.root
five_right.root.right.right = RBNode(7, BLACK)
five_right.root.right.right.p = five_right.root.right
five_right.root.right.left = RBNode(4, BLACK)
five_right.root.right.left.p = five_right.root.right

# five_right._print_tree_indented(five_right.root)
# five_right.left_rotate(five_right.root)
# five_right._print_tree_indented(five_right.root)


five_left = RBTree()
five_left.root = RBNode(5, BLACK)
five_left.root.p = five_left.sentinel
five_left.root.right = RBNode(7, RED)
five_left.root.right.p = five_left.root
five_left.root.left = RBNode(3, RED)
five_left.root.left.p = five_left.root
five_left.root.left.right = RBNode(4, BLACK)
five_left.root.left.right.p = five_left.root.left
five_left.root.left.left = RBNode(2, BLACK)
five_left.root.left.left.p = five_left.root.left

five_left._print_tree_indented(five_left.root)
five_left.right_rotate(five_left.root)
five_left._print_tree_indented(five_left.root)
