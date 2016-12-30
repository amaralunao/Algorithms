import timeit


def profiling():
    setup = '''
from algorithms.merge_sort2 import merge_sort2
from __main__ import huge_list
import copy
huge = copy.copy(huge_list)
    '''
    print('merge_sort2 time is:', timeit.timeit("merge_sort2(huge)",
                                                setup=setup, number=10))
