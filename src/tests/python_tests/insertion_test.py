
import unittest
import random
from algorithms.insertion_sort import insertion_sort
from .is_sorted_test import is_sorted


class TestSortingMethods(unittest.TestCase):

    def test_insertion_sort_random(self):
        random_list = random.sample(range(0, 1000), 1000)
        self.assertTrue(is_sorted(insertion_sort(random_list)))

    def test_insertion_sort_empty(self):
        empty_list = []
        self.assertTrue(is_sorted(insertion_sort(empty_list)))

    def test_insertion_sort_one(self):
        one_list = [1]
        self.assertTrue(is_sorted(insertion_sort(one_list)))

    def test_insertion_sort_sorted(self):
        sorted_list = list(range(1000))
        self.assertTrue(is_sorted(insertion_sort(sorted_list)))

    def test_insertion_sort_reverse_sorted(self):
        reverse_sorted = list(range(1000, 0, -1))
        self.assertTrue(is_sorted(insertion_sort(reverse_sorted)))

if __name__ == '__main__':
    unittest.main()
