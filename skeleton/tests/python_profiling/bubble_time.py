import copy
import timeit
from algorithms.bubble_sort import bubble_sort
from . import lists


test_list = copy.copy(lists.huge_list)

def time():
    print('bubble_sort time is:',
          timeit.repeat("bubble_sort(test_list)",
                        number=3, globals=globals()))

if __name__ == '__main__':
    time()
