import unittest
from algorithms.red_black_tree import RBNode, RBTree, RED, BLACK

class RedBlackTest(unittest.TestCase):

    def setUp(self):
        self.empty = RBTree()
        self.one = RBTree()
        self.one.root = RBNode(5)
        self.five_right = RBTree()
        self.five_right.root = RBNode(3, BLACK)
        self.five_right.root.p = self.five_right.sentinel
        self.five_right.root.right = RBNode(5, BLACK)
        self.five_right.root.right.p = self.five_right.root
        self.five_right.root.left = RBNode(2, BLACK)
        self.five_right.root.left.p = self.five_right.root
        self.five_right.root.left.right = self.five_right.sentinel
        self.five_right.root.left.left = self.five_right.sentinel
        self.five_right.root.right.right = RBNode(7, RED)
        self.five_right.root.right.right.p = self.five_right.root.right
        self.five_right.root.right.right.right = self.five_right.sentinel
        self.five_right.root.right.right.left = self.five_right.sentinel
        self.five_right.root.right.left = RBNode(4, RED)
        self.five_right.root.right.left.p = self.five_right.root.right
        self.five_right.root.right.left.right = self.five_right.sentinel
        self.five_right.root.right.left.left = self.five_right.sentinel
        self.five_left = RBTree()
        self.five_left.root = RBNode(5, BLACK)
        self.five_left.root.p = self.five_left.sentinel
        self.five_left.root.right = RBNode(7, BLACK)
        self.five_left.root.right.p = self.five_left.root
        self.five_left.root.right.right = self.five_left.sentinel
        self.five_left.root.right.left = self.five_left.sentinel
        self.five_left.root.left = RBNode(3, BLACK)
        self.five_left.root.left.p = self.five_left.root
        self.five_left.root.left.right = RBNode(4, RED)
        self.five_left.root.left.right.p = self.five_left.root.left
        self.five_left.root.left.right.right = self.five_left.sentinel
        self.five_left.root.left.right.left = self.five_left.sentinel
        self.five_left.root.left.left = RBNode(2, RED)
        self.five_left.root.left.left.p = self.five_left.root.left
        self.five_left.root.left.left.right = self.five_left.sentinel
        self.five_left.root.left.left.left = self.five_left.sentinel

    

if __name__ == '__main__':
    unittest.main()
