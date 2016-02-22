import timeit


def profiling():
    setup = '''
from algorithms.merge_sort_slow import merge_sort_slow
from __main__ import huge_list
import copy
huge = copy.copy(huge_list)
    '''
    print('merge_sort_slow time is:', timeit.timeit("merge_sort_slow(huge)",
                                                    setup=setup, number=10))
