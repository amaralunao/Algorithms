import timeit


def profiling():
    setup = '''
from algorithms.quick_sort import quick_sort
from __main__ import huge_list
import copy
huge = copy.copy(huge_list)
    '''
    print('quick_sort time is:', timeit.timeit("quick_sort(huge)",
                                               setup=setup, number=10))
