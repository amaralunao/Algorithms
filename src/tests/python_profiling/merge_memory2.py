import copy
from algorithms.merge_sort2 import merge_sort2
from memory_profiler import profile


def profiling():
    from __main__ import huge_list
    huge = copy.copy(huge_list)
    return merge_sort2(huge, _memory=True)


if __name__ == '__main__':
    profiling()
