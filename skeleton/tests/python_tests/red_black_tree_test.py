import unittest
from algorithms.red_black_tree import RBNode, RBTree, RED, BLACK

class RedBlackTest(unittest.TestCase):

    def setUp(self):
        self.empty = RBTree()
        self.one = RBTree()
        self.one.root = RBNode(5, BLACK)
        self.one.root.p = self.one.sentinel
        self.one.root.left = self.one.sentinel
        self.one.root.right = self.one.sentinel
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

    def test_search_empty(self):
        with self.assertRaisesRegex(KeyError, "Key not found"):
            self.empty.search(7)

    def test_search_found_one(self):
        self.assertEqual(self.one.search(5), self.one.root.key)

    def test_search_not_found_one(self):
        with self.assertRaisesRegex(KeyError, "Key not found"):
            self.one.search(7)

    def test_search_found_five_right(self):
        self.assertEqual(self.five_right.search(2),
                         self.five_right.root.left.key)

    def test_rb_insert_empty(self):
        self.assertTrue(self.empty.rb_insert(RBNode(5)))
        self.assertEqual(self.empty.root.key, 5)
        self.assertEqual(self.empty.root.color, BLACK)

    def test_rb_insert_right_one_BST(self):
        self.assertTrue(self.one.rb_insert(RBNode(7)))
        self.assertEqual(self.one.root.right.key, 7)
        self.assertEqual(self.one.root.right.color, RED)

    def test_rb_insert_left_one_BST(self):
        self.assertTrue(self.one.rb_insert(RBNode(3)))
        self.assertEqual(self.one.root.left.key, 3)
        self.assertEqual(self.one.root.left.color, RED)

    def test_insert_case1_five_left(self):
        self.assertTrue(self.five_left.rb_insert(RBNode(1)))
        self.assertEqual(self.five_left.root.left.left.left.key, 1)
        self.assertEqual(self.five_left.root.left.left.left.color, RED)
        self.assertEqual(self.five_left.root.color, BLACK)
        self.assertEqual(self.five_left.root.left.left.color, BLACK)
        self.assertEqual(self.five_left.root.left.right.color, BLACK)

    def test_rb_insert_case3_five_left(self):
        self.five_left.rb_insert(RBNode(1))
        self.assertTrue(self.five_left.rb_insert(RBNode(0)))
        self.assertEqual(self.five_left.root.left.left.left.key, 0)
        self.assertEqual(self.five_left.root.left.left.left.color, RED)
        self.assertEqual(self.five_left.root.left.left.key, 1)
        self.assertEqual(self.five_left.root.left.left.color, BLACK)

    def test_rb_insert_case2_five_right(self):
        self.five_right.rb_insert(RBNode(8))
        self.assertTrue(self.five_right.rb_insert(RBNode(9)))
        self.assertEqual(self.five_right.root.right.right.right.key, 9)
        self.assertEqual(self.five_right.root.right.right.right.color, RED)
        self.assertEqual(self.five_right.root.right.right.color, BLACK)
        self.assertEqual(self.five_right.root.right.right.key, 8)



if __name__ == '__main__':
    unittest.main()
