RED = "RED"
BLACK = "BLACK"


class NilNode:
    def __init__(self):
        self.color = BLACK


NIL = NilNode()     #leaf sentinel of the tree


class RBNode:
    def __init__(self, key, color=RED, left=NIL, right=NIL, p=NIL):

        self.color = color
        #color either RED or BLACK
        self.key = key
        self.left = left
        self.right = right
        self.p = p

class RBTree:
    def __init__(self, root=NIL):
        self.root = root
