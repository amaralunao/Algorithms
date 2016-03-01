import unittest
import random
from algorithms.quick_sort import quick_sort
from .is_sorted_test import is_sorted


class TestSortingMethods(unittest.TestCase):

    def test_quick_sort_random(self):
        random_list = random.sample(range(0, 1000), 1000)
        self.assertTrue(is_sorted(quick_sort(random_list)))

    def test_quick_sort_empty(self):
        empty_list = []
        self.assertTrue(is_sorted(quick_sort(empty_list)))

    def test_quick_sort_one(self):
        one_list = [1]
        self.assertTrue(is_sorted(quick_sort(one_list)))

    def test_quick_sort_sorted(self):
        sorted_list = list(range(1000))
        self.assertTrue(is_sorted(quick_sort(sorted_list)))

    def test_quick_sort_reverse_sorted(self):
        reverse_sorted = list(range(1000, 0, -1))
        self.assertTrue(is_sorted(quick_sort(reverse_sorted)))


if __name__ == '__main__':
    unittest.main()
