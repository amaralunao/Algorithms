
import unittest
import random
from algorithms.merge_sort2 import merge_sort2
from .is_sorted_test import is_sorted


class TestSortingMethods(unittest.TestCase):

    def test_merge_sort2_random(self):
        random_list = random.sample(range(0, 1000), 1000)
        self.assertTrue(is_sorted(merge_sort2(random_list)))

    def test_merge_sort2_empty(self):
        empty_list = []
        self.assertTrue(is_sorted(merge_sort2(empty_list)))

    def test_merge_sort2_one(self):
        one_list = [1]
        self.assertTrue(is_sorted(merge_sort2(one_list)))

    def test_merge_sort2_sorted(self):
        sorted_list = list(range(1000))
        self.assertTrue(is_sorted(merge_sort2(sorted_list)))

    def test_merge_sort2_reverse_sorted(self):
        reverse_sorted = list(range(1000, 0, -1))
        self.assertTrue(is_sorted(merge_sort2(reverse_sorted)))


if __name__ == '__main__':
    unittest.main()
