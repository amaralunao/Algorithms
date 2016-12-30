import timeit


def profiling():
    setup = '''
from algorithms.bubble_sort import bubble_sort
from __main__ import huge_list
import copy
huge = copy.copy(huge_list)
    '''
    print('bubble_sort time is:', timeit.timeit("bubble_sort(huge)",
                                                setup=setup, number=10))
