import copy
from algorithms.bubble_sort import bubble_sort


def profiling():
    from __main__ import huge_list
    huge = copy.copy(huge_list)
    return bubble_sort(huge, _memory=True)

if __name__ == '__main__':
    profiling()
