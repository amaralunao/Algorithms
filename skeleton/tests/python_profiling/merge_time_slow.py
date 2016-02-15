import copy
import timeit
from algorithms.merge_sort_slow import merge_sort_slow
from . import lists


test_list = copy.copy(lists.huge_list)


def time():
        print('merge_sort_slow time is:',
              timeit.repeat("merge_sort_slow(test_list)",
                            number=3, globals=globals()))


if __name__ == '__main__':
    time()
