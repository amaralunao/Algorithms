import unittest
import random
from algorithms.singly_list import Node, UnorderedList


class TestLists(unittest.TestCase):

    def setUp(self):
        self.empty_list = UnorderedList()
        self.two_elements = UnorderedList()
        self.two_elements._head = Node(1)
        self.two_elements._head.next = Node(2)
        self.two_elements._length = 2
        self.two_elements._tail = Node(2)

    def test_len_empty(self):
        self.assertEqual(self.empty_list.__len__(), 0)

    def test_len_two_elements(self):
        self.assertEqual(self.two_elements.__len__(), 2)

    def test_is_empty_empty(self):
        self.assertTrue(self.empty_list.is_empty())

    def test_is_empty_two_elements(self):
        self.assertFalse(self.two_elements.is_empty())

    def test__get_index_empty(self):
        with self.assertRaises(IndexError):
            self.empty_list._get_index(0)

    def test__get_index_handled_two_elements(self):
        self.assertEqual(self.two_elements._get_index(1),
                         (self.two_elements._head,
                          self.two_elements._head.next))

    def test__get_index_unhandled_two_elements(self):
        with self.assertRaises(IndexError):
            self.two_elements._get_index(3)

    def test__getitem__empty(self):
        with self.assertRaises(IndexError):
            self.empty_list.__getitem__(0)

    def test__getitem__handled_two_elements(self):
        self.assertEqual(self.two_elements.__getitem__(1),
                         (self.two_elements._tail.data))

    def test__getitem__unhandled_two_elements(self):
        with self.assertRaises(IndexError):
            self.two_elements.__getitem__(3)

    def test__setitem__empty(self):
        with self.assertRaises(IndexError):
            self.empty_list.__setitem__(0, 10)

    def test__getitem__handled_two_elements(self):
        self.two_elements[0] = 10
        self.assertEqual(self.two_elements._head.data, 10)

    def test__getitem__unhandled_two_elements(self):
        with self.assertRaises(IndexError):
            self.two_elements.__setitem__(3, 10)

    def test__search_empty(self):
        with self.assertRaises(ValueError):
            self.empty_list._search()

    def test__search_found_two_elements(self):
        self.assertEqual(self.two_elements._search(2),
                         (self.two_elements._head,
                         self.two_elements._head.next))

    def test__search_not_found_two_elements(self):
        with self.assertRaises(ValueError):
            self.two_elements._search(3)

    def test_push_empty(self):
        self.empty_list.push(3)
        self.assertEqual(self.empty_list._head.data, 3)
        self.assertEqual(self.empty_list.__len__(), 1)

    def test_push_two_elements(self):
        self.two_elements.push(3)
        self.assertEqual(self.two_elements._head.data, 3)
        self.assertEqual(self.two_elements.__len__(), 3)

    def test_remove_empty(self):
        with self.assertRaises(ValueError):
            self.empty_list.remove(0)

    def test_remove_found_two_elements(self):
        self.two_elements.remove(2)
        self.assertIsNone(self.two_elements._head.next)
        self.assertEqual(self.two_elements.__len__(), 1)

    def test_remove_not_found_two_elements(self):
        with self.assertRaises(ValueError):
            self.two_elements.remove(3)

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.empty_list.pop(3)

    def test_pop_handled_two_elements(self):
        self.assertEqual(self.two_elements.pop(0), 1)
        self.assertIsNone(self.two_elements._head.next)
        self.assertEqual(self.two_elements.__len__(), 1)

    def test_pop_indexNone_two_elements(self):
        self.assertEqual(self.two_elements.pop(), 2)
        self.assertIsNone(self.two_elements._head.next)
        self.assertEqual(self.two_elements.__len__(), 1)

    def test_pop_unhandled_two_elements(self):
        with self.assertRaises(IndexError):
            self.two_elements.pop(3)

    def test_append_empty(self):
        self.empty_list.append(1)
        self.assertEqual(self.empty_list._head.data, 1)
        self.assertEqual(self.empty_list.__len__(), 1)

    def test_append_two_elements(self):
        self.two_elements.append(3)
        self.assertEqual(self.two_elements._tail.data, 3)
        self.assertEqual(self.two_elements.__len__(), 3)

    def test_insert_handled_empty(self):
        self.empty_list.insert(0, 3)
        self.assertEqual(self.empty_list._head.data, 3)
        self.assertEqual(self.empty_list.__len__(), 1)

    def test_insert_unhandled_empty(self):
        with self.assertRaises(IndexError):
            self.empty_list.insert(1, 3)

    def test_insert_handled_two_elements(self):
        self.two_elements.insert(1, 3)
        self.assertEqual(self.two_elements._head.next.data, 3)
        self.assertEqual(self.two_elements.__len__(), 3)

    def test_insert_unhandled_two_elements(self):
        with self.assertRaises(IndexError):
            self.two_elements.insert(2, 3)

if __name__ == '__main__':
    unittest.main()
