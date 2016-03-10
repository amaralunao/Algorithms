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
        self.five_right.root.right = RBNode(5, RED)
        self.five_right.root.right.p = self.five_right.root
        self.five_right.root.left = RBNode(2, RED)
        self.five_right.root.left.p = self.five_right.root
        self.five_right.root.right.right = RBNode(7, BLACK)
        self.five_right.root.right.right.p = self.five_right.root.right
        self.five_right.root.right.left = RBNode(4, BLACK)
        self.five_right.root.right.left.p = self.five_right.root.right
        self.five_left = RBTree()
        self.five_left.root = RBNode(5, BLACK)
        self.five_left.root.right = RBNode(7, RED)
        self.five_left.root.right.p = self.five_left.root
        self.five_left.root.left = RBNode(7, RED)
        self.five_left.root.left.p = self.five_left.root
        self.five_left.root.left.right = RBNode(4, BLACK)
        self.five_left.root.left.right.p = self.five_left.root.left
        self.five_left.root.left.left = RBNode(2, BLACK)
        self.five_left.root.left.left.p = self.five_left.root.left

    def test_left_rotate_one(self):
        self.assertFalse(self.one.left_rotate(self.one.root))

    def test_right_rotate_one(self):
        self.assertFalse(self.one.right_rotate(self.one.root))

    def test_left_rotate_five_right(self):
        rotated = self.five_right.left_rotate(self.five_right.root)
        self.assertEquals(rotated.root.key, 3)
        #self.assertEquals(self.five_right.root.right.key, 5)
        #self.assertEquals(self.five_right.root.left.key, 2)
        #self.assertEquals(self.five_right.root.right.right.key, 7)
        #self.assertEquals(self.five_right.root.right.left.key, 4)

if __name__ == '__main__':
    unittest.main()
