
import unittest
import random
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort


def is_sorted(alist):
    cnt = 0
    while cnt < len(alist) - 1:
        if alist[cnt] < alist[cnt+1]:
            cnt += 1
        else:
            return False
    return True


class TestSortingMethods(unittest.TestCase):
    # Testing is_sorted () output:
    def test_is_sorted_empty(self):
        empty_list = []
        self.assertTrue(is_sorted(empty_list))

    def test_is_sorted_one(self):
        one_list = [1]
        self.assertTrue(is_sorted(one_list))

    def test_is_sorted_sorted(self):
        sorted_list = list(range(200))
        self.assertTrue(is_sorted(sorted_list))

    # Testing bubble_sort() output:
    def test_bubble_sort_random(self):
        random_list = random.sample(range(1, 200), 100)
        self.assertTrue(is_sorted(bubble_sort(random_list)))

    def test_bubble_sort_empty(self):
        empty_list = []
        self.assertTrue(is_sorted(bubble_sort(empty_list)))

    def test_bubble_sort_one(self):
        one_list = [1]
        self.assertTrue(is_sorted(bubble_sort(one_list)))

    def test_bubble_sort_sorted(self):
        sorted_list = list(range(200))
        self.assertTrue(is_sorted(bubble_sort(sorted_list)))

    def test_bubble_sort_reverse_sorted(self):
        sorted_list = list(range(200))
        reverse_sorted = list(reversed(sorted_list))
        self.assertTrue(is_sorted(bubble_sort(reverse_sorted)))

    # Testing insertion_sort() output:

    def test_insertion_sort_random(self):
        random_list = random.sample(range(1, 200), 100)
        self.assertTrue(is_sorted(insertion_sort(random_list)))

    def test_insertion_sort_empty(self):
        empty_list = []
        self.assertTrue(is_sorted(insertion_sort(empty_list)))

    def test_insertion_sort_one(self):
        one_list = [1]
        self.assertTrue(is_sorted(insertion_sort(one_list)))

    def test_insertion_sort_sorted(self):
        sorted_list = list(range(200))
        self.assertTrue(is_sorted(insertion_sort(sorted_list)))

    def test_insertion_sort_reverse_sorted(self):
        reverse_sorted = list(reversed(range(200)))
        self.assertTrue(is_sorted(insertion_sort(reverse_sorted)))


if __name__ == '__main__':
    unittest.main()

# from skeleton run: python3 -m unittest tests/algorithms_tests.py
