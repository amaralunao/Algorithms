import copy
import timeit
from algorithms.merge_sort2 import merge_sort2
from . import lists


test_list = copy.copy(lists.huge_list)


def time():
        print('merge_sort time2 is:',
              timeit.repeat("merge_sort2(test_list)",
                            number=3, globals=globals()))


if __name__ == '__main__':
    time()
