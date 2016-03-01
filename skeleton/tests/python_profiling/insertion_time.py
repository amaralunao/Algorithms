import timeit


def profiling():
    setup = '''
from algorithms.insertion_sort import insertion_sort
from __main__ import huge_list
import copy
huge = copy.copy(huge_list)
    '''
    print('insertion_sort time is:', timeit.timeit("insertion_sort(huge)",
                                                   setup=setup, number=10))
