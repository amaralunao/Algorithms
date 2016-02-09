import random
import timeit
import unittest
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from memory_profiler import profile


time_test_list_bubble = random.sample(range(1, 100), 10)
time_test_list_insertion = random.sample(range(1, 100), 10)


@profile
def profile_bubble_sort(alist):
    return bubble_sort(alist)


@profile
def profile_insertion_sort(alist):
    return insertion_sort(alist)

memory_test_list_bubble = random.sample(range(1, 100), 10)
memory_test_list_insertion = random.sample(range(1, 100), 10)

class TestSortingMethods(unittest.TestCase):

        def test_time(self):
            # Testing bubble_sort() time:
            print('\nbubble_sort time is:',
                  timeit.repeat("bubble_sort(time_test_list_bubble)",
                                number=3, globals=globals()))
            # Testing insertion_sort() time:
            print('insertion_sort time is:',
                  timeit.repeat("insertion_sort(time_test_list_insertion)",
                                number=3, globals=globals()))

if __name__ == '__main__':
    profile_bubble_sort(memory_test_list_bubble)
    profile_insertion_sort(memory_test_list_insertion)
    unittest.main()
