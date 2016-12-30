import unittest
import random


def is_sorted(alist):
    cnt = 0
    while cnt < len(alist) - 1:
        if alist[cnt] < alist[cnt+1]:
            cnt += 1
        else:
            return False
    return True


class TestSortingMethods(unittest.TestCase):

    def test_is_sorted_empty(self):
        empty_list = []
        self.assertTrue(is_sorted(empty_list))

    def test_is_sorted_one(self):
        one_list = [1]
        self.assertTrue(is_sorted(one_list))

    def test_is_sorted_sorted(self):
        sorted_list = list(range(1000))
        self.assertTrue(is_sorted(sorted_list))

if __name__ == '__main__':
    unittest.main()
