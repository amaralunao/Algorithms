import copy
from algorithms.insertion_sort import insertion_sort
from memory_profiler import profile


def profiling():
    from __main__ import huge_list
    huge = copy.copy(huge_list)
    return insertion_sort(huge, _memory=True)


if __name__ == '__main__':
    profiling()
