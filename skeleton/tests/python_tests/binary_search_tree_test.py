import unittest
from algorithms.binary_search_tree import BSTNode, BST

class BSTTests(unittest.TestCase):

    def setUp(self):

        self.empty_BST = BST()
        self.parent_BST = BST()
        self.parent_BST.root = BSTNode(5, None, None, None)
        self.parent_left_BST = BST()
        self.parent_left_BST.root = BSTNode(5, None, None, None)
        self.parent_left_BST.root.left = BSTNode(3, None, None, None)
        self.parent_left_BST.root.left.parent = self.parent_left_BST.root
        self.parent_right_BST = BST()
        self.parent_right_BST.root = BSTNode(5, None, None, None)
        self.parent_right_BST.root.right = BSTNode(7, None, None, None)
        self.parent_right_BST.root.right.parent = self.parent_right_BST.root
        self.parent_both_BST = BST()
        self.parent_both_BST.root = BSTNode(5, None, None, None)
        self.parent_both_BST.root.left = BSTNode(3, None, None, None)
        self.parent_both_BST.root.left.parent = self.parent_both_BST.root
        self.parent_both_BST.root.right = BSTNode(7, None, None, None)
        self.parent_both_BST.root.right.parent = self.parent_both_BST.root

    def test_search_empty_BST(self):
        with self.assertRaisesRegex(KeyError, "Key not found"):
            self.empty_BST.search(7)

    def test_search_found_parent_BST(self):
        self.assertEqual(self.parent_BST.search(5), self.parent_BST.root.key)

    def test_search_not_found_parent_BST(self):
        with self.assertRaisesRegex(KeyError, "Key not found"):
            self.parent_BST.search(7)

    def test_search_found_both_BST(self):
        self.assertEqual(self.parent_both_BST.search(3),
                         self.parent_both_BST.root.left.key)

    def test_insert_empty_BST(self):
        self.assertTrue(self.empty_BST.insert(5))
        self.assertEqual(self.empty_BST.root.key, 5)

    def test_insert_right_parent_BST(self):
        self.assertTrue(self.parent_BST.insert(7))
        self.assertEqual(self.parent_BST.root.right.key, 7)

    def test_insert_left_parent_BST(self):
        self.assertTrue(self.parent_BST.insert(3))
        self.assertEqual(self.parent_BST.root.left.key, 3)

    def test_insert_parent_both_BST_key_exists(self):
        with self.assertRaisesRegex(KeyError, "They key already exists"):
            self.parent_both_BST.insert(7)

    def test_delete_empty_BST(self):
        with self.assertRaisesRegex(KeyError, "Key not found"):
            self.empty_BST.delete(7)

    def test_delete_parent_BST(self):
        self.assertTrue(self.parent_BST.delete(5))
        self.assertIsNone(self.parent_BST.root)

    def test_delete_leaf_parent_both_BST(self):
        self.assertTrue(self.parent_both_BST.delete(7))
        self.assertIsNone(self.parent_both_BST.root.right)

    def test_delete_leaf_parent_both_BST_not_found(self):
        with self.assertRaisesRegex(KeyError, "Key not found"):
            self.assertTrue(self.parent_both_BST.delete(8))

    def test_delete_node_only_right_child_parent_right_BST(self):
        self.assertTrue(self.parent_right_BST.delete(5))
        self.assertEqual(self.parent_right_BST.root.key, 7)

    def test_delete_node_only_left_child_parent_left_BST(self):
        self.assertTrue(self.parent_left_BST.delete(5))
        self.assertEqual(self.parent_left_BST.root.key, 3)

    def test_delete_node_both_children_parent_both_BST(self):
        self.assertTrue(self.parent_both_BST.delete(5))
        self.assertEqual(self.parent_both_BST.root.key, 7)

    def test_preorder_not_empty(self):
        test_list = list(self.parent_both_BST.preorder())
        self.assertEqual(self.parent_both_BST.root.key, test_list[0])
        self.assertEqual(self.parent_both_BST.root.left.key, test_list[1])
        self.assertEqual(self.parent_both_BST.root.right.key, test_list[2])
        self.assertEqual(len(test_list), 3)

    def test_inorder_not_empty(self):
        test_list = list(self.parent_both_BST.inorder())
        self.assertEqual(self.parent_both_BST.root.key, test_list[1])
        self.assertEqual(self.parent_both_BST.root.left.key, test_list[0])
        self.assertEqual(self.parent_both_BST.root.right.key, test_list[2])
        self.assertEqual(len(test_list), 3)

    def test_inorder_not_empty(self):
        test_list = list(self.parent_both_BST.postorder())
        self.assertEqual(self.parent_both_BST.root.key, test_list[2])
        self.assertEqual(self.parent_both_BST.root.left.key, test_list[0])
        self.assertEqual(self.parent_both_BST.root.right.key, test_list[1])
        self.assertEqual(len(test_list), 3)

    def test_preorder_empty(self):
        test_list = list(self.empty_BST.preorder())
        self.assertEqual(len(test_list), 0)

    def test_inorder_empty(self):
        test_list = list(self.empty_BST.inorder())
        self.assertEqual(len(test_list), 0)

    def test_postorder_empty(self):
        test_list = list(self.empty_BST.postorder())
        self.assertEqual(len(test_list), 0)


if __name__ == '__main__':
    unittest.main()
