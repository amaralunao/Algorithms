
import unittest
import random
from algorithms.merge_sort_slow import merge_sort_slow
from .is_sorted_test import is_sorted


class TestSortingMethods(unittest.TestCase):

    def test_merge_sort_slow_random(self):
        random_list = random.sample(range(0, 200), 200)
        self.assertTrue(is_sorted(merge_sort_slow(random_list)))

    def test_merge_sort_slow_empty(self):
        empty_list = []
        self.assertTrue(is_sorted(merge_sort_slow(empty_list)))

    def test_merge_sort_slow_one(self):
        one_list = [1]
        self.assertTrue(is_sorted(merge_sort_slow(one_list)))

    def test_merge_sort_slow_sorted(self):
        sorted_list = list(range(200))
        self.assertTrue(is_sorted(merge_sort_slow(sorted_list)))

    def test_merge_sort_slow_reverse_sorted(self):
        reverse_sorted = list(reversed(range(200)))
        self.assertTrue(is_sorted(merge_sort_slow(reverse_sorted)))


if __name__ == '__main__':
    unittest.main()
