import unittest
from algorithms.red_black_tree import RBNode, RBTree, RED, BLACK
import math
import random


def is_height_correct(tree):

    if tree._height(tree.root) <= 2*math.log2(tree._node_count(tree.root) + 1):
        return True
    else:
        return False


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

    def test_is_height_correct_one(self):
        self.assertTrue(is_height_correct(self.one))

    def test_is_height_correct_five_left(self):
        self.assertTrue(is_height_correct(self.five_left))

    def test_is_height_correct_five_right(self):
        self.assertTrue(is_height_correct(self.five_right))

    def test_insert_empty(self):
        self.assertTrue(self.empty.insert(5))
        self.assertEqual(self.empty.root.key, 5)
        self.assertEqual(self.empty.root.color, BLACK)

    def test_insert_right_one_BST(self):
        self.assertTrue(self.one.insert(7))
        self.assertEqual(self.one.root.right.key, 7)
        self.assertEqual(self.one.root.right.color, RED)

    def test_insert_left_one_BST(self):
        self.assertTrue(self.one.insert(3))
        self.assertEqual(self.one.root.left.key, 3)
        self.assertEqual(self.one.root.left.color, RED)

    def test_insert_case1_five_left(self):
        self.assertTrue(self.five_left.insert(1))
        self.assertEqual(self.five_left.root.left.left.left.key, 1)
        self.assertEqual(self.five_left.root.left.left.left.color, RED)
        self.assertEqual(self.five_left.root.color, BLACK)
        self.assertEqual(self.five_left.root.left.left.color, BLACK)
        self.assertEqual(self.five_left.root.left.right.color, BLACK)

    def test_insert_case3_five_left(self):
        self.five_left.insert(1)
        self.assertTrue(self.five_left.insert(0))
        self.assertEqual(self.five_left.root.left.left.left.key, 0)
        self.assertEqual(self.five_left.root.left.left.left.color, RED)
        self.assertEqual(self.five_left.root.left.left.key, 1)
        self.assertEqual(self.five_left.root.left.left.color, BLACK)

    def test_insert_case2_five_right(self):
        self.five_right.insert(8)
        self.assertTrue(self.five_right.insert(9))
        self.assertEqual(self.five_right.root.right.right.right.key, 9)
        self.assertEqual(self.five_right.root.right.right.right.color, RED)
        self.assertEqual(self.five_right.root.right.right.color, BLACK)
        self.assertEqual(self.five_right.root.right.right.key, 8)

    def test_delete_empty(self):
        with self.assertRaisesRegex(KeyError, "Key not found"):
            self.one.delete(0)

    def test_delete_case_1(self):
        self.empty.insert(1)
        self.empty.insert(2)
        self.assertTrue(self.empty.delete(1))
        self.assertEqual(self.empty.root.key, 2)
        self.assertEqual(self.empty.root.color, BLACK)
        self.assertTrue(is_height_correct(self.empty))

    def test_delete_case_1_2_left(self):
        nodes = [10, 15, 7, 8, 5, 6]
        for key in nodes:
            self.empty.insert(key)
        self.assertTrue(self.empty.delete(15))
        self.assertEqual(self.empty.root.color, BLACK)
        self.assertTrue(is_height_correct(self.empty))

    def test_delete_case_3_4_left(self):
        nodes = [10, 15, 7, 8, 5, 6]
        for key in nodes:
            self.empty.insert(key)
        self.assertTrue(self.empty.delete(7))
        self.assertEqual(self.empty.root.color, BLACK)
        self.assertTrue(is_height_correct(self.empty))

    def test_delete_case_1_2_right(self):
        nodes = [10, 9, 13, 11, 15, 12]
        for key in nodes:
            self.empty.insert(key)
        self.assertTrue(self.empty.delete(9))
        self.assertEqual(self.empty.root.color, BLACK)
        self.assertTrue(is_height_correct(self.empty))

    def test_delete_case_3_4_right(self):
        nodes = [10, 9, 13, 11, 15, 12]
        for key in nodes:
            self.empty.insert(key)
        self.assertTrue(self.empty.delete(10))
        self.assertEqual(self.empty.root.color, BLACK)
        self.assertTrue(is_height_correct(self.empty))

    def test_delete_huge_list(self):
        random_list = random.sample(range(0, 1000), 1000)
        red_black_tree = RBTree()
        for i in random_list:
            red_black_tree.insert(i)
        for i in random_list:
            self.assertTrue(red_black_tree.delete(i))
            self.assertTrue(is_height_correct(red_black_tree))
        

    def test_insert_huge_list(self):

        random_list = random.sample(range(0, 1000), 1000)
        red_black_tree = RBTree()
        for i in random_list:
            self.assertTrue(red_black_tree.insert(i))
            self.assertEqual(red_black_tree.root.color, BLACK)
            self.assertTrue(is_height_correct(red_black_tree))

    def test_search_huge_list(self):
        random_list = random.sample(range(0, 1000), 1000)
        red_black_tree = RBTree()
        for i in random_list:
            red_black_tree.insert(i)
        for i in random_list:
            self.assertEqual(red_black_tree.search(i), i)

if __name__ == '__main__':
    unittest.main()
