import copy
import timeit
from algorithms.insertion_sort import insertion_sort
from . import lists


test_list = copy.copy(lists.huge_list)


def time():
    print('insertion_sort time is:',
          timeit.repeat("insertion_sort(test_list)",
                        number=3, globals=globals()))

if __name__ == '__main__':
    time()
