import copy
from algorithms.merge_sort2 import merge_sort2
from memory_profiler import profile
from . import lists

test_list = copy.copy(lists.huge_list)

@profile
def memory():

    return merge_sort2(test_list)


if __name__ == '__main__':
    memory()
