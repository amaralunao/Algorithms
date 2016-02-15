import copy
from algorithms.merge_sort_slow import merge_sort_slow
from memory_profiler import profile
from . import lists

test_list = copy.copy(lists.huge_list)

@profile
def memory():

    return merge_sort_slow(test_list)


if __name__ == '__main__':
    memory()
